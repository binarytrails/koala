from kivy.app import App
from custom.Error import Errors
import custom.Utilities as utils
import downloader.Utilities as ytutils
from Beat import Beat

from threading import Thread
from time import sleep
from threading import RLock

import re, Queue

"""
@todo: 
Indicate if wifi connection.
Indicate internet speed
Indicate mp4 to download size
Estimate time for the downloading
"""

def synchronized_with_attr(lock_name):
    def decorator(method):
        def synced_method(self, *args, **kws):
            lock = getattr(self, lock_name)
            """
            @attention: 
            The 'if "owner=None" in str(lock):' to let 
            the others threads go in queue.
            """
            if "owner=None" in str(lock):
                with lock:
                    return method(self, *args, **kws)
        return synced_method
    return decorator

class KivyApp(App):
    
    __wtitle = "AwesomeKoalaBeat"
    __ofolder = ""
    __vformat = "mp4"
    __downloadQueue = Queue.Queue()
    __conversionQueue = Queue.Queue()
    __lock = RLock()

    def build(self):
        App.title = self.__wtitle
        Thread(target = self._downloader, args=[]).start()
        Thread(target = self._converter, args=[]).start()
        self.kivyView.build(self)
        return self.kivyView
    
    def setYoutubeDownloader(self, downloader):
        self.youtube = downloader
    
    def setDownloaderView(self, kivyView):
        self.kivyView = kivyView
    
    def setWindowTitle(self, wtitle):
        self.__wtitle = wtitle

    def setOutputFolder(self, ofolder):
        self.__ofolder = ofolder

    def getOutputFolder(self):
        return self.__ofolder

    def setVideoFormat(self, vformat):
        self.__vformat = vformat
        
    def buildMp3FromYoutubeLink(self, url, title, artist, album, year):
        code, error, url = self._validateYoutubeURL(url)
        if code is 1:
            self.kivyView.showPopup(error)
            return
        
        beat = Beat(url, title, artist, album, year)
        self.__downloadQueue.put(beat)

    def updateProgress(self, bytes_received, file_size):
        percent = float(bytes_received) / float(file_size) * 100
        self.kivyView.setDownloadProgress(percent)

    def _downloader(self):
        """
        Listens the __downloadQueue
        Downloads youtube video with the highest mp4 resolution
        """
        while True:
            try:
                beat = self.__downloadQueue.get()
                self.kivyView.setStatusLabelText("Downloading")
                self.youtube.url = beat.getUrl()
                self.youtube.filename = beat.getTitle()
                #get the video highest resolution
                video = self.youtube.filter(self.__vformat)[-1]

                video.download(self.__ofolder, beat,
                    on_progress=self.updateProgress,
                    on_finish=self.notifyDownloadCompleted)

            except Queue.Empty:
                pass

    def notifyDownloadCompleted(self, fullpath, beat):
        self.__conversionQueue.put(beat)

    #@synchronized_with_attr("lock")
    def _converter(self):
        """
        Listens the __conversionQueue
        Converts mp4 to mp3 from __conversionQueue
        """
        while True:
            try:
                beat = self.__conversionQueue.get()
                self.kivyView.setStatusLabelText("Converting")

                mp4 = beat.getTitle() + ".mp4"
                mp3 = beat.getTitle() + ".mp3"
                
                if utils.fileExists(self.__ofolder+mp4) is False:
                    self.kivyView.showPopup(Errors.CONVERSION_FAILED[0])
                    return
                elif utils.fileExists(self.__ofolder+mp3):
                    #@TODO offer choice to the user.
                    utils.deleteFile(self.__ofolder+mp3)
                """
                :Case
                The file uploading was intereptuded, but the file lenght stays the initial.

                :Problem
                Progressbar wont show the right progression because the mp4 duration
                isnt right, so the efsize isnt estimated proprelly.

                :Solution
                This function wont be called if the downloading was interruped.
                """
                secs = utils.getFFmpegFileDurationInSeconds(self.__ofolder + mp4)
                efsize = utils.estimateFFmpegMp4toMp3NewFileSizeInBytes(secs, 320000)
                utils.convertMp4ToMp3(mp4, mp3, self.__ofolder, 320000, efsize, beat,
                                      self.updateProgress, self.notifyConversionCompleted)
            except Queue.Empty:
                pass

    def notifyConversionCompleted(self, fullpath, beat):
        self.kivyView.setStatusLabelText("Saving Beat Information")
        utils.writeMP3Metadata(fullpath, beat)

        utils.deleteFile(self.__ofolder + beat.getTitle()+".mp4")

        self.kivyView.setStatusLabelText("Completed!")
        self.kivyView.enableDownloadButton()
    
    def _simulateDownload(self):
        self.kivyView.setStatusLabelText("Downloading")
        self.kivyView.disableDownloadButton()
        self.kivyView.setDownloadProgress(0)
        for progress in range(1, 101):
            sleep(0.01)
            self.kivyView.setDownloadProgress(progress)
        self.kivyView.enableDownloadButton()
        self.kivyView.setStatusLabelText("Downloaded")

    def _validateYoutubeURL(self, url):
        """
         0: valid link
         1: error
        """
        error = Errors.INVALID_LINK
        code = 1
        youtube_regex = (
        r'(https?://)?(www\.)?'
        '(youtube|youtu|youtube-nocookie)\.(com|be)/'
        '(watch\?v=|embed/|v/|.+\?v=)?([^&=%\?]{11})|([^&=%\?]{11})')

        youtubeFormat = re.match(youtube_regex, url)
        if youtubeFormat:
            video_id = ytutils.get_youtube_video_id(url)
            #check if exists
            url = "http://www.youtube.com/watch?v=" + str(video_id)
            video = None
            try:
                self.youtube.url = url
                #get the video with highest resolution available of our format
                video = self.youtube.filter(self.__vformat)
            #Video doesnt exists.
            except Exception:
                #TODO: Better exception
                pass
            if video:
                return 0, None, url
        return code, str(error[0]), url

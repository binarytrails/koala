from Beat import Beat
from kivy.app import App

import Utilities as utils
from ErrorMessages import Errors

from threading import Thread
from threading import RLock
from time import sleep

import threading, traceback, re, Queue

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
    
    __lock = RLock()
    _beatToDownload = Queue.Queue()
    _beatToConvert = Queue.Queue()
    
    _stopDownloaderThread = threading.Event()
    _stopConverterThread = threading.Event()
    
    # Fired when the App has finished running.
    def on_stop(self):
        self.root.stop.set()
        self._stopDownloaderThread.set()
        self._stopConverterThread.set()

    def _init_threads(self):
        self._downloaderThread = Thread(target = self._downloader,
                args=[self._stopDownloaderThread])
        self._converterThread = Thread(target = self._converter, 
                args=[self._stopConverterThread])

    def build(self):
        App.title = self.__wtitle
        self._init_threads()
        self.kivyView.build(self)
        return self.kivyView
    
    def setYoutubeDownloader(self, downloader):
        pass
        #self.youtube = downloader
    
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
        self._beatToDownload.put(beat)

    def updateProgress(self, bytes_received, file_size):
        percent = float(bytes_received) / float(file_size) * 100
        self.kivyView.setDownloadProgress(percent)

    def notifyDownloadCompleted(self, beat):
        self._beatToConvert.put(beat)

    def _downloader(self, stopEvent):
        """
            Downloads the beat that arrives to _beatToDownload.
        """
        while (not stopEvent.is_set()):
            try:
                beat = self._beatToDownload.get()
                self.kivyView.setStatusLabelText("Downloading")
                
                #self.youtube.url = beat.getUrl()
                #self.youtube.filename = beat.getTitle()
                #get the video highest resolution
                #video = self.youtube.filter(self.__vformat)[-1]

                #video.download(self.__ofolder, beat,
                #    on_progress=self.updateProgress,
                #    on_finish=self.notifyDownloadCompleted)

                # temp
                sleep(2)
                self.notifyDownloadCompleted(beat)

            except Queue.Empty:
                pass
    
    def notifyConversionCompleted(self, fullpath, beat):
        self.kivyView.setStatusLabelText("Saving Beat Information")
        utils.writeMP3Metadata(fullpath, beat)

        utils.deleteFile(self.__ofolder + beat.getTitle()+".mp4")

        self.kivyView.setStatusLabelText("Completed!")
        self.kivyView.enableDownloadButton()

    #@synchronized_with_attr("lock")
    def _converter(self, stopEvent):
        """
            Converts the MP4 to MP3 that arrives in _beatToConvert.
        """
        while (not stopEvent.is_set()):
            try:
                beat = self._beatToConvert.get()
                self.kivyView.setStatusLabelText("Converting")

                mp4 = beat.getTitle() + ".mp4"
                mp3 = beat.getTitle() + ".mp3"
                
                if utils.fileExists(self.__ofolder+mp4) is False:
                    self.kivyView.showPopup(Errors.CONVERSION_FAILED[0])
                    return
                elif utils.fileExists(self.__ofolder+mp3):
                    #@TODO offer choice to the user.
                    utils.deleteFile(self.__ofolder+mp3)
                
                secs = utils.getFFmpegFileDurationInSeconds(self.__ofolder + mp4)
                efsize = utils.estimateFFmpegMp4toMp3NewFileSizeInBytes(secs, 320000)
                utils.convertMp4ToMp3(mp4, mp3, self.__ofolder, 320000, efsize, beat,
                                      self.updateProgress, self.notifyConversionCompleted)
            except Queue.Empty:
                pass
 
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
            video_id = utils.getYoutubeVideoId(url)
            url = "http://www.youtube.com/watch?v=" + str(video_id)
            video = None 
            try:
                pass
                #self.youtube.url = url
                # get the highest resolution
                #video = self.youtube.filter(self.__vformat) 
            except Exception:
                print traceback.format_exc()

            if video:
                return 0, None, url

        return code, Errors.INVALID_LINK, url


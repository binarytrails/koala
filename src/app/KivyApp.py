from kivy.app import App
from threading import Thread
from time import sleep
from threading import RLock

from custom.Error import YoutubeURL

from urlparse import parse_qs
from urlparse import urlparse
import os, re

def synchronized_with_attr(lock_name):
    def decorator(method):
        def synced_method(self, *args, **kws):
            lock = getattr(self, lock_name)
            """
            Remove the 'if' to let the others threads go in queue.
            Case: user forgot to disable the trigger of this action.
            Consequences: overload of downloads in queue.
            """
            if "owner=None" in str(lock):
                with lock:
                    return method(self, *args, **kws)
        return synced_method
    return decorator

class KivyApp(App):
    
    def build(self):
        self.lock = RLock()
        App.title = self.windowTitle
        self.acceptedVideoFormat = "mp4"
        self.kivyView.build(self)
        return self.kivyView
    
    def setYoutubeDownloader(self, downloader):
        self.youtube = downloader
    
    def setDownloaderView(self, kivyView):
        self.kivyView = kivyView
    
    def setDefaults(self, windowTitle, defaultFolder):
        self.windowTitle = windowTitle
        self.defaultFolder = defaultFolder
    
    def downloadAndConvert(self, url, title):
        code, error, url = self._validateYoutubeURL(url)
        if code is 1:
            self.kivyView.showPopup(error)
            return
        thread = Thread(target = self._downloadAndConvertVideoToMp3, args=[url, title])
        thread.start()
    
    @synchronized_with_attr("lock")
    def _downloadAndConvertVideoToMp3(self, url, title):
        self.kivyView.setStatusLabelText("Downloading")
        self.kivyView.disableDownloadButton()
        
        self.youtube.url = url
        self.youtube.filename = title
        #get the video with highest resolution available of our format
        video = self.youtube.filter(self.acceptedVideoFormat)[-1]
        
        video.download(self.defaultFolder, on_progress=self.updateDownloadStatus)
        self.kivyView.enableDownloadButton()
        self.kivyView.setStatusLabelText("Downloaded")
        
        #do convert
        #ffmpeg -i prentend\ its\ a\ video\ game.mp4  -f mp3 -ab 320000 -vn music.mp3
        
        #os.remove(self.defaultFolder + title + ".mp4")
    
    @synchronized_with_attr("lock")
    def _simulateDownload(self):
        self.kivyView.setStatusLabelText("Downloading")
        self.kivyView.disableDownloadButton()
        self.kivyView.setDownloadProgress(0)
        for progress in range(1,101):
            sleep(0.01)
            self.kivyView.setDownloadProgress(progress)
        self.kivyView.enableDownloadButton()
        self.kivyView.setStatusLabelText("Downloaded")
        
    def updateDownloadStatus(self, bytes_received, file_size):
        percent = bytes_received * 100. / file_size
        self.kivyView.setDownloadProgress(percent)
        
    
    def _get_youtube_video_id(self, url):
        query = urlparse(url)
        if query.hostname == 'youtu.be':
            return query.path[1:]
        if query.hostname in ('www.youtube.com', 'youtube.com'):
            if query.path == '/watch':
                p = parse_qs(query.query)
                return p['v'][0]
            if query.path[:7] == '/embed/':
                return query.path.split('/')[2]
            if query.path[:3] == '/v/':
                return query.path.split('/')[2]
        return None

    def _validateYoutubeURL(self, url):
        """
         0: valid link
         1: error
        """
        error = YoutubeURL.INVALID_LINK
        code = 1
        youtube_regex = (
        r'(https?://)?(www\.)?'
        '(youtube|youtu|youtube-nocookie)\.(com|be)/'
        '(watch\?v=|embed/|v/|.+\?v=)?([^&=%\?]{11})|([^&=%\?]{11})')

        youtubeFormat = re.match(youtube_regex, url)
        if youtubeFormat:
            video_id = self._get_youtube_video_id(url)
            #check if exists
            url = "http://www.youtube.com/watch?v=" + str(video_id)
            video = None
            try:
                self.youtube.url = url
                #get the video with highest resolution available of our format
                video = self.youtube.filter(self.acceptedVideoFormat)
            #Video doesnt exists.
            except Exception:
                #TODO: Better exception
                pass
            if video:
                return 0, None, url
        return code, str(error[0]), url

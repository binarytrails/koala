from kivy.app import App
from threading import Thread
from time import sleep
from threading import RLock

import os

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
        thread = Thread(target = self._downloadAndConvertVideoToMp3, args=[url, title])
        thread.start()
    
    @synchronized_with_attr("lock")
    def _downloadAndConvertVideoToMp3(self, url, title):
        self.kivyView.setStatusLabelText("Downloading")
        self.kivyView.disableDownloadButton()
        
        self.youtube.url = url
        #get highest resolution available for .mp4 
        video = self.youtube.filter("mp4")[-1]
        self.youtube.filename = title
        
        video.download(self.defaultFolder, on_progress=self.__updateDownloadStatus)
        self.kivyView.enableDownloadButton()
        self.kivyView.setStatusLabelText("Downloaded")
        
        #do convert
        
        os.remove(self.defaultFolder + title + ".mp4")
    
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
        
    def __updateDownloadStatus(self, bytes_received, file_size):
        percent = bytes_received * 100. / file_size
        self.kivyView.setDownloadProgress(percent)

from threading import Thread
from time import sleep

class TkinterApp(object):
    def __init__(self, windowTitle, outputFolder):
        self.windowTitle = windowTitle
        self.outputFolder = outputFolder
    
    def setDownloaderView(self, view):
        self.downloaderView = view
    
    def getFileTitle(self, url, logText):
        pass
                  
    def download(self, url, title):
        thread = Thread(target = self._simulateDownload, args=[])
        thread.start()

    def _youtubeDownload(self, url, title):
        pass
    
    def updateDownloadStatus(self, bytes_received, file_size):
        percent = bytes_received * 100. / file_size
        self.downloaderView.updateDownloadProgressText(percent)
        
    def _simulateDownload(self):
        for p in range(0, 100):
            self.updateDownloadStatus(p, 100)
            sleep(0.01)
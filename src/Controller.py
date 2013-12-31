from view.TkinterView import DownloaderView
from downloader import Youtube
from Tkinter import END

from threading import Thread
from time import sleep

class Controller(object):
    def __init__(self, output):
        self.name = "KoalaBeatzHunter"
        self.output = output
        self.downloaderView = DownloaderView(self, self.output)
    
    def getFileTitle(self, url, logText):
        pass
                  
    def downloadFileThread(self, url, title):
#         yt = Youtube.YouTube()
#         #doesnt take http://youtu.be/
#         yt.url = "http://www.youtube.com/watch?v=VeTMsLp_puY"
#         video = yt.get("flv")
#         video.download(TMP_FOLDER, on_progress=self.updateDownloadStatus)
        for p in range(0, 100):
            self.updateDownloadStatus(p, 100)
            sleep(0.01)
    
    def updateDownloadStatus(self, progress, file_size):
        percent = progress * 100. / file_size
        self.downloaderView.updateDownloadProgressText(percent)

'''
TESTING
'''
TMP_FOLDER = "../tmp/"
def testProgressbar():
    c = Controller(TMP_FOLDER)
    #controller.downloaderView.updateDownloadProgressbar(10)
    
    thread = Thread(target = c.downloadFileThread, args=["",""])
    thread.start()
    
    c.downloaderView.root.mainloop()


if __name__ == "__main__":
    testProgressbar()

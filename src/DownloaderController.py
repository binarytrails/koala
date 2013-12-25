import DownloaderTkinterView
import commands

class DownloaderController(object):

    def __init__(self):
        self.viewDownloader = DownloaderTkinterView.DownloaderView(self)
    
    def getFileTitle(self, url, logText):
        
        return commands.getstatusoutput("youtube-dl --get-filename  -o '%(title)s.%(ext)s' " +
                  url + " --restrict-filenames 2>&1")
                  
    def downloadFile(self, url, title):
        return commands.getstatusoutput("youtube-dl --output " + title +
            "-w -c --audio-format mp3 --extract-audio " + url)
        
        
        
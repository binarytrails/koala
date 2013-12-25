import DownloaderTkinterView
import commands

class DownloaderController(object):

    def __init__(self, outputLocation):
        self.viewDownloader = DownloaderTkinterView.DownloaderView(self, outputLocation)
    
    def getFileTitle(self, url, logText):
        
        return commands.getstatusoutput("youtube-dl --get-filename  -o '%(title)s.%(ext)s' " +
                  url + " --restrict-filenames 2>&1")
                  
    def downloadFile(self, url, loc, title):
        return commands.getstatusoutput("youtube-dl --output " + loc + title +
            "-w -c --audio-format mp3 --extract-audio " + url)
        
        
        
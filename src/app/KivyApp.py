from kivy.app import App

from threading import Thread
from time import sleep

class KivyApp(App):
    def build(self):
        App.title = self.windowTitle
        self.kivyView.build(self)
        return self.kivyView
    
    def setDownloaderView(self, kivyView):
        self.kivyView = kivyView
    
    def setDefaults(self, windowTitle, defaultFolder):
        self.windowTitle = windowTitle
        self.defaultFolder = defaultFolder
    
    def download(self, progressBar, url, title):
        thread = Thread(target = self._simulateDownload, args=[progressBar])
        thread.start()
    
    def _simulateDownload(self, progressBar):
        progressBar.value = 0
        for i in range(1,101):
            sleep(0.1)
            progressBar.value += i
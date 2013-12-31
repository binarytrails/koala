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
        
    def _simulateDefaults(self):
        for i in range(1,101):
            sleep(0.1)
            self.progressBar.value += i
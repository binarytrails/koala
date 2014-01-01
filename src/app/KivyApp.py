from kivy.app import App

from threading import Thread
from time import sleep
from threading import RLock

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
    
    def setDownloaderView(self, kivyView):
        self.kivyView = kivyView
    
    def setDefaults(self, windowTitle, defaultFolder):
        self.windowTitle = windowTitle
        self.defaultFolder = defaultFolder
    
    def download(self, url, title):
        thread = Thread(target = self._simulateDownload, args=[])
        thread.start()
    
    @synchronized_with_attr("lock")
    def _simulateDownload(self):
        self.kivyView.disableDownloadButton()
        self.kivyView.setDownloadProgress(0)
        for progress in range(1,101):
            sleep(0.01)
            self.kivyView.setDownloadProgress(progress)
        self.kivyView.enableDownloadButton()

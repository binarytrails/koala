from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager
Builder.load_string("""
<KivyView@ScreenManager>:
    progressBar: _progressBar
    destination: _destinationText
    Screen:
        name: 'main'
        BoxLayout:
            orientation: 'vertical'
            GridLayout:
                cols: 2
                Label:
                    text: 'Youtube URL'
                    size_hint: 0.5, 1
                TextInput:
                    id: _urlText
                    text: 'http://youtu.be/YaG5SAw1n0c'
                    size_hint: 0.5, 1
                Label:
                    text: 'Output folder'
                TextInput:
                    id: _destinationText
                    text: '../tmp/'
            ProgressBar:
                id: _progressBar
                max: 100
            GridLayout:
                cols: 2
                Button:
                    text: 'Menu'
                    on_press: root.current = 'menu'
                Button:
                    text: 'Download'
                    # You can do the opertion directly
                    on_press: root.download()
                Button:
                    text: 'update test'
                    on_press: _urlText.text = _destinationText.text
    Screen:
        name: 'menu'
        Button:
            size_hint: .3,.1
            center: self.parent.center
            text: 'Welcome to KoalaBeatzHunter'
            on_press: root.current = 'main'
""")

class KivyView(ScreenManager):
    """
    Only user communicate here
    """
    def build(self, root):
        self.root = root
    
    # define the multiplication of a function
    def startDownload(self):
        pass

    def updateDownloadStatus(self, value):
        print self.progressBar
        self.progressBar.value = value
        
    def updateDestinationFolder(self):
        self.destination.text = 'Mordor'
    
"""
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager
Builder.load_string('''
<DownloaderUI@ScreenManager>:
    progressBar: _progressBar
    destination: _destinationText
    Screen:
        name: 'main'
        BoxLayout:
            orientation: 'vertical'
            GridLayout:
                cols: 2
                Label:
                    text: 'Youtube URL'
                    size_hint: 0.5, 1
                TextInput:
                    id: _urlText
                    text: 'http://youtu.be/YaG5SAw1n0c'
                    size_hint: 0.5, 1
                Label:
                    text: 'Output folder'
                TextInput:
                    id: _destinationText
                    text: '../tmp/'
            ProgressBar:
                id: _progressBar
                max: 100
            GridLayout:
                cols: 2
                Button:
                    text: 'Menu'
                    on_press: root.current = 'menu'
                Button:
                    text: 'Download'
                    # You can do the opertion directly
                    on_press: root.download()
                Button:
                    text: 'update test'
                    on_press: _urlText.text = _destinationText.text
    Screen:
        name: 'menu'
        Button:
            size_hint: .3,.1
            center: self.parent.center
            text: 'Welcome to KoalaBeatzHunter'
            on_press: root.current = 'main'
''')

class DownloaderUI(ScreenManager):
    def build(self, root):
        self.root = root
    
    # define the multiplication of a function
    def startDownload(self):
        thread = Thread(target=self._simulateDownload, args=[])
        thread.start()

    def updateDownloadStatus(self, value):
        print self.progressBar
        self.progressBar.value = value
        
    def _simulateDownload(self):
        for i in range(1,101):
            sleep(0.1)
            self.progressBar.value += i
        
    def updateDestinationFolder(self):
        self.destination.text = 'Mordor'
        
from threading import Thread
from time import sleep

class DownloaderApp(App):
    def build(self):
        #self.controller = controller
        App.title = "chateua"#self.controller.windowTitle
        self.downloaderUI = DownloaderUI()
        self.downloaderUI.build(self)
        return self.downloaderUI
        
# def callOut(who):
#     who.updateDestinationFolder()
#     print "Called out"
#     
# def callIn(who):
#     sleep(1)
#     who.updateDestinationFolder()
#     who.updateDownloadStatus(49)
#     print "CallIn woked up. who.destination.text: "+str(who.destination.text)
    


if __name__ == '__main__':
    DownloaderApp().run()
"""
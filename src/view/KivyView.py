from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager
Builder.load_string("""
<KivyView@ScreenManager>:
    downloadButton: _downloadButton
    progressBar: _progressBar
    destination: _destination
    url: _url
    Screen:
        name: 'menu'
        canvas.before:
            BorderImage:
                source: '../res/img/bg.jpeg'
                border: 10, 10, 10, 10
                pos: self.pos
                size: self.size
        Button:
            size_hint: .3, .1
            center: self.parent.center
            text: 'Welcome Koala!'
            background_down: '../res/img/bg.jpeg'
            on_press: root.current = 'main'
    Screen:
        name: 'main'
        #background image
        canvas.before:
            BorderImage:
                source: '../res/img/bg.jpeg'
                border: 10, 10, 10, 10
                pos: self.pos
                size: self.size
        BoxLayout:
            orientation: 'vertical'
            Button:
                text: 'Back To Menu'
                size_hint: 0.2, 0.1
                on_press: root.current = 'menu'
            GridLayout:
                cols: 2
                Label:
                    color: 0,0,0
                    text: 'Youtube URL'
                TextInput:
                    id: _url
                    text: 'http://youtu.be/YaG5SAw1n0c'
                Label:
                    text: 'Koala Home'
                TextInput:
                    id: _destination
                Label:
                    text: 'Song Title'
                TextInput:
                    id: _title
                Button:
                    text: 'Convert'
                    disabled: True
                    on_press: root.convert()
                Button:
                    id: _downloadButton
                    text: 'Download'
                    on_press: root.download()
            ProgressBar:
                size_hint: 1, 0.1
                id: _progressBar
                max: 100
""")

class KivyView(ScreenManager):
    """
    User communication
    """
    def build(self, root):
        self.root = root
        self.destination.text = self.root.defaultFolder
        
    def on_touch_down(self, touch):
        print super(ScreenManager, self).on_touch_down(touch)
        if self.transition.is_active:
            return False
        return super(ScreenManager, self).on_touch_down(touch)
    
    # define the multiplication of a function
    def download(self):
        self.root.download(self.url, "FooBarTitle")
        
    def convert(self):
        pass

    def getDownloadProgress(self):
        return self.progressBar.value

    def setDownloadProgress(self, value):
        self.progressBar.value = value
        
    def disableDownloadButton(self):
        self.downloadButton.disabled = True
    
    def enableDownloadButton(self):
        self.downloadButton.disabled = False
        

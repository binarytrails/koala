from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager
Builder.load_string("""
<KivyView@ScreenManager>:
    statusLabel: _statusLabel
    downloadButton: _downloadButton
    progressBar: _progressBar
    titleInput: _titleInput
    destInput: _destInput
    urlInput: _urlInput
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
                    text: 'Youtube URL (doesnt take "http://youtu.be/" links)'
                TextInput:
                    id: _urlInput
                    text: 'http://www.youtube.com/watch?v=jics5IrlDWk'
                Label:
                    text: 'Koala Home'
                TextInput:
                    id: _destInput
                Label:
                    text: 'Song Title'
                TextInput:
                    id: _titleInput
                    text: 'AwesomeKoalaBeat'
                Label:
                    id: _statusLabel
                    text: 'Status'
                Button:
                    id: _downloadButton
                    text: 'Download'
                    on_press: root.downloadAndConvert()
            ProgressBar:
                size_hint: 1, 0.1
                id: _progressBar
                max: 100
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
""")

class KivyView(ScreenManager):
    """
    User communication
    """
    def build(self, root):
        self.root = root
        self.destInput.text = self.root.defaultFolder
    
    #todo: detect background touch?
    def on_touch_down(self, touch):
        if self.transition.is_active:
            return False
        return super(ScreenManager, self).on_touch_down(touch)
    
    # define the multiplication of a function
    def downloadAndConvert(self):
        self.root.downloadAndConvert(self.urlInput.text, self.titleInput.text)

    def getDownloadProgress(self):
        return self.progressBar.value

    def setDownloadProgress(self, value):
        self.progressBar.value = value
        
    def disableDownloadButton(self):
        self.downloadButton.disabled = True
    
    def enableDownloadButton(self):
        self.downloadButton.disabled = False
        
    def setStatusLabelText(self, text):
        self.statusLabel.text = text

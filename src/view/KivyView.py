from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager
from kivy.uix.popup import Popup
from kivy.uix.label import Label

Builder.load_string("""
<KivyView@ScreenManager>:
    statusLabel: _statusLabel
    downloadButton: _downloadButton
    menuButton: _menuButton
    progressBar: _progressBar
    titleInput: _titleInput
    destInput: _destInput
    urlInput: _urlInput
    Screen:
        name: 'menu'
        #Giant button, easier than detect bg touch
        ModalView:
            Button:
                id: _menuButton
                center: self.parent.center
                markup: True
                background_normal: '../res/img/bg_middle_3.jpg'
                on_press: root.current = 'main'
    Screen:
        name: 'main'
        #background image
        canvas.before:
            BorderImage:
                id: _mainBorderImage
                source: '../res/img/bg_north_west_3.jpg'
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
                    text: 'Koala Home'
                TextInput:
                    id: _destInput
                Label:
                    text: 'Youtube URL'
                TextInput:
                    id: _urlInput
                    text: 'http://youtu.be/dY7G8HwQaAQ'
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
""")

class KivyView(ScreenManager):
    """
    User communication
    """
    def build(self, root):
        self.root = root
        self.destInput.text = self.root.defaultFolder
    
    # define the multiplication of a function
    def downloadAndConvert(self):
        self.root.downloadAndConvert(self.urlInput.text, self.titleInput.text)

    def showPopup(self, text):
        popup = Popup(title='Attention!',
                      content=Label(text=text, 
                                    markup=True), 
                      size_hint=(0.4, 0.4))
        popup.open()
    
    def setUrlInput(self, url):
        self.urlInput.text = url
    
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

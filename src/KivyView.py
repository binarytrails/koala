from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager
from kivy.uix.popup import Popup
from kivy.uix.label import Label

import threading, time

Builder.load_string("""
<KivyView@ScreenManager>:
    urlInput: _urlInput
    titleInput: _titleInput
    artistInput: _artistInput
    albumInput: _albumInput
    destInput: _destInput
    yearInput: _yearInput
    downloadButton: _downloadButton
    progressBar: _progressBar
    statusLabel: _statusLabel
    Screen:
        name: 'main'
        #background image
        canvas.before:
            BorderImage:
                id: _mainBorderImage
                source: '../res/img/bg.jpeg'
                border: 10, 10, 10, 10
                pos: self.pos
                size: self.size
        BoxLayout:
            orientation: 'vertical'
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
                    text: 'http://youtu.be/YaG5SAw1n0c'
                Label:
                    text: 'Title'
                TextInput:
                    id: _titleInput
                    text: 'AwesomeKoalaBeat'
                Label:
                    text: 'Artist'
                TextInput:
                    id: _artistInput
                    text: 'P. cinereus'
                Label:
                    text: 'Album'
                TextInput:
                    id: _albumInput
                    text: 'Phascolarctidae'
                Label:
                    text: 'Year'
                TextInput:
                    id: _yearInput
                    text: '1817'
                    disabled: True
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
    
    stop = threading.Event()
    
    def build(self, root):
        self.root = root
        self.destInput.text = self.root.getOutputFolder()
    
    def downloadAndConvert(self):
        self.root.buildMp3FromYoutubeLink(self.urlInput.text,
                                          self.titleInput.text,
                                          self.artistInput.text,
                                          self.albumInput.text,
                                          self.yearInput.text)

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

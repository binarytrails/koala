from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager
from kivy.uix.popup import Popup
from kivy.uix.label import Label

import os, threading

Builder.load_string("""
#:import FadeTransition kivy.uix.screenmanager.FadeTransition

<KivyView@ScreenManager>:
    url: _url
    title: _title
    artist: _artist
    album: _album
    dest: _dest
    year: _year
    downloadButton: _downloadButton
    progressBar: _progressBar
    status: _status

    transition: FadeTransition()
    
    Screen:
        name: 'Home'
        ModalView:
            Button:
                id: _homeButton
                center: self.parent.center 
                background_normal: root.getHomeBackground()
                text: 'Welcome to Koala'
                font_size: 30
                on_press:
                    #root.transition.direction = 'down'
                    root.current = 'Downloader'
    Screen:
        name: 'Downloader'
        canvas.before:
            BorderImage:
                id: _downloaderBackground
                source: root.getDownloaderBackground()
                border: 10, 10, 10, 10
                pos: self.pos
                size: self.size
        BoxLayout:
            orientation: 'vertical'
            GridLayout:
                cols: 2
                Label:
                    text: 'Home'
                TextInput:
                    id: _dest
                Label:
                    text: 'URL'
                TextInput:
                    id: _url
                    text: ''
                Label:
                    text: 'Title'
                TextInput:
                    id: _title
                    text: ''
                Label:
                    text: 'Artist'
                TextInput:
                    id: _artist
                    text: ''
                Label:
                    text: 'Album'
                TextInput:
                    id: _album
                    text: ''
                Label:
                    text: 'Year'
                TextInput:
                    id: _year
                    text: ''
                    disabled: True
                Label:
                    id: _status
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

    _ressourcesDir = os.path.join(os.path.abspath(os.pardir), "res/")
    _imagesDir = os.path.join(_ressourcesDir, "images")

    def moqDevelopmentValues(self):
        self.url.text = "http://youtu.be/YaG5SAw1n0c"
        self.title.text = "Beautiful Koala"
        self.artist.text = "P. Cinereus"
        self.album.text = "Phascolarctidae"
        self.year.text = "Not Supported."

    def build(self, root):
        self.root = root
        self.moqDevelopmentValues()
        self.dest.text = self.root.getOutputFolder()
    
    def enableDownloadButton(self):
        self.downloadButton.disabled = False
    
    def disableDownloadButton(self):
        self.downloadButton.disabled = True

    def getHomeBackground(self):
        return os.path.join(self._imagesDir, "blue_background.jpg")

    def getDownloaderBackground(self):
        return os.path.join(self._imagesDir, "blue_background.jpg")

    def getDownloadProgress(self):
        return self.progressBar.value

    def setUrl(self, url):
        self.url.text = url
    
    def setStatusLabelText(self, text):
        self.status.text = text
    
    def setDownloadProgress(self, value):
        self.progressBar.value = value    
    
    def downloadAndConvert(self):
        self.root.buildMp3FromYoutubeLink(self.url.text,
                                          self.title.text,
                                          self.artist.text,
                                          self.album.text,
                                          self.year.text)

    def showPopup(self, text):
        popup = Popup(title='Attention!',
                      content=Label(text = text, markup = True), 
                      size_hint=(0.4, 0.4))
        popup.open()
        

from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager
Builder.load_string("""
<KivyView@ScreenManager>:
    progressBar: _progressBar
    destination: _destinationText
    url: _urlText
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
    User communication
    """
    def build(self, root):
        self.root = root
        self.destination.text = self.root.defaultFolder
    
    # define the multiplication of a function
    def download(self):
        self.root.download(self.progressBar, self.url, "FooBarTitle")

    def updateDownloadStatus(self, value):
        print self.progressBar
        self.progressBar.value = value

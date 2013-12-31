import Tkinter as tk
import tkMessageBox

class DownloaderView():
    def __init__(self, controller, ouput):
        self.controller = controller
        self.ouput = ouput
        
        self.root = tk.Tk()
        self.root.title(self.controller.name)
        self._center_window(505, 100)
        self.root.resizable(tk.FALSE, tk.FALSE)
        self.mainFrame = tk.Frame(bd=2, relief=tk.SUNKEN)
        self.root.option_add('*Dialog.msg.font', 'Helvetica 10')

        self._makeUrlControls()
        self._makeOutputControls()
        self._makedownloadProgressControls()
        self._makeDownloadAction()
        self.mainFrame.pack(fill=tk.BOTH, expand=True)
        
    def _makeUrlControls(self):
        self.lblURL = tk.Label(self.mainFrame, text="Youtube url")
        self.lblURL.grid(row=0, column=0, sticky=tk.W)
        
        self.urlEntry = tk.Entry(self.mainFrame)
        self.urlEntry.grid(row=0, column=1)
        self.urlEntry.config(width=50)
        self.urlEntry.insert(0, "http://youtu.be/YaG5SAw1n0c")
    
    def _makeOutputControls(self):
        self.destinationLabel = tk.Label(self.mainFrame, text="Output folder")
        self.destinationLabel.grid(row=1, column=0)
         
        self.destinationEntry = tk.Entry(self.mainFrame)
        self.destinationEntry.grid(row=1, column=1)
        self.destinationEntry.config(width=50)
        self.destinationEntry.insert(0, self.ouput)
    
    def _makedownloadProgressControls(self):
        self.downloadProgressLabel = tk.Label(self.mainFrame, text="Download")
        self.downloadProgressLabel.grid(row=2, column=0)
         
        self.downloadProgressEntry = tk.Entry(self.mainFrame)
        self.downloadProgressEntry.grid(row=2, column=1)
        self.downloadProgressEntry.config(width=50)#, state='readonly')
    
    def _makeDownloadAction(self):
        self.downloadButton = tk.Button(
            self.mainFrame, text="Download",
            command=lambda:self.download()
        )
        self.downloadButton.grid(row=3, column=1, sticky=tk.E)

    def _center_window(self, w, h):
        """
        Make the window of the desired size and
        aligns it in the center on your window.
        Arguments:
        w: width
        h: height
        """
        ws = self.root.winfo_screenwidth()
        hs = self.root.winfo_screenheight()
        
        x = (ws/2) - (w/2)
        y = (hs/2) - (h/2)
        
        self.root.geometry('%dx%d+%d+%d' % (w, h, x, y))

    def download(self):
        pass
#         confirmed = tkMessageBox.askokcancel(
#             "Confirm", "Video title: " + title,
#             parent=self.root)
    
    def updateDownloadProgressText(self, value):
        """
        Updates progress in downloadProgressbar
        Arguments: value: digit between 0-100
        """
        value = value + 1
        self.downloadProgressEntry.delete(0, tk.END)
        self.downloadProgressEntry.insert(0, chr(8) * (int(value)*57/100))
        if int(value) is 100:
            self.downloadProgressEntry.delete(0, tk.END)
            tkMessageBox.askokcancel(self.controller.name, "Downloading completed!")

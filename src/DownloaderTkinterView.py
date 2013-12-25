import Tkinter as tk
import tkMessageBox

class DownloaderView():

    def __init__(self, controller, outputLocation):
        self.controller = controller
        self.outputLocation = outputLocation
        
        self.root = tk.Tk()
        self.root.option_add('*Dialog.msg.font', 'Helvetica 10')
        self.makeDownloaderView()
        
        self.root.mainloop()

    def makeDownloaderView(self):
        self.root.title("Ytube2Mp3")
        self.center_window(505, 160)
        self.root.resizable(tk.FALSE, tk.FALSE)
        self.frameMain = tk.Frame(bd=2, relief=tk.SUNKEN)
        
        self.lblURL = tk.Label(self.frameMain, text="Youtube url")
        self.lblURL.grid(row=0, column=0, sticky=tk.W)
        
        self.inputURL = tk.Entry(self.frameMain)
        self.inputURL.grid(row=0, column=1)
        self.inputURL.config(width=50)
        self.inputURL.insert(0, "http://youtu.be/YaG5SAw1n0c")
        
        self.lblDest = tk.Label(self.frameMain, text="Output folder")
        self.lblDest.grid(row=1, column=0, sticky=tk.W)
         
        self.inputDest = tk.Entry(self.frameMain)
        self.inputDest.grid(row=1, column=1)
        self.inputDest.config(width=50)
        self.inputDest.insert(0, self.outputLocation)
         
        self.lblOutput = tk.Label(self.frameMain, text="System output")
        self.lblOutput.grid(row=2, column=0, sticky=tk.W)
         
        self.txtOutput = tk.Text(self.frameMain, width=57, height=5)
        self.txtOutput.grid(row=2, column=1)
        
        self.btnDownload = tk.Button(
        self.frameMain, text="Download",
             command=lambda:self.confirmDownload(self.inputURL.get()))
        self.btnDownload.grid(row=3, column=1, sticky=tk.E)
 
        self.frameMain.pack(fill=tk.BOTH, expand=True)
         
    def confirmDownload(self, url):
        code, msg = self.controller.getFileTitle(url, self)
        if code is not 0:
            self.txtOutput.insert(tk.END, "\n" + msg)
            return
        
        title = msg
        confirmed = tkMessageBox.askokcancel(
            "Confirm", "Video title: " + title,
            parent=self.root)
        
        if confirmed:
            self.txtOutput.insert(tk.END, "\nDownloading... Go eat a cookie.")
            code, msg = self.controller.downloadFile(url, self.outputLocation, title)
            if code is not 0:
                self.txtOutput.insert(tk.END, "\nError " + str(code) + " " + msg)
                return
            self.txtOutput.insert(tk.END, "\nFinished!")

    def center_window(self, w, h):
        ws = self.root.winfo_screenwidth()
        hs = self.root.winfo_screenheight()
        
        x = (ws/2) - (w/2)
        y = (hs/2) - (h/2)
        
        self.root.geometry('%dx%d+%d+%d' % (w, h, x, y))

#!/usr/bin/python
from app.TkinterApp import TkinterApp
from view.TkinterView import TkinterView
from app.KivyApp import KivyApp
from view.KivyView import KivyView

import sys, getopt
from enum import Enum

HELP_MESSAGE = "KoalaBeatzHunter.py -o <outputfolder>"
WINDOW_TITLE = "KoalaBeatzHunter"
DEFAULT_FOLDER = "../../tmp/"

class UI(Enum):
    KIWI=0,
    TKINTER=1

def main(argv):
    #TODO write default location depending on OS
    output = DEFAULT_FOLDER
    ui = UI.KIWI

    try:
        opts, args = getopt.getopt(argv, "hi:o:",["ofolder="])
        if args.__len__() != 0:
            pass
        
    except getopt.GetoptError:
        print HELP_MESSAGE
        sys.exit(2)
    
    for opt, arg in opts:
        if opt == '-h':
            print HELP_MESSAGE
            sys.exit()
        elif opt in ("-o", "--ofolder"):
            output = arg
    print output
    
    if ui == UI.TKINTER:
        app = TkinterApp(WINDOW_TITLE, DEFAULT_FOLDER)
        view = TkinterView(app)
        app.setDownloaderView(view)
        view.root.mainloop()
        
    elif ui == UI.KIWI:
        app = KivyApp()
        view = KivyView()
        
        app.setDownloaderView(view)
        app.setDefaults(WINDOW_TITLE, DEFAULT_FOLDER)
        
        app.run()
        app.root.mainloop()
    
if __name__ == "__main__":
    main(sys.argv[1:])

#!/usr/bin/python
from app.TkinterApp import TkinterApp
from view.TkinterView import TkinterView
from app.KivyApp import KivyApp
from view.KivyView import KivyView
from Default import *

import sys, getopt
from enum import Enum

class UI(Enum):
    NONE=0,
    KIVY=1,
    TKINTER=1

def main(argv):
    output = DEFAULT_FOLDER
    ui = UI.KIVY
    '''
    The below options will be there if you remove Kivy imports.
    Otherwise Kivy help overrides them.
    '''
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
    
    if ui == UI.TKINTER:
        app = TkinterApp(WINDOW_TITLE, output)
        view = TkinterView(app)
        app.setDownloaderView(view)
        view.root.mainloop()
        
    elif ui == UI.KIVY:
        app = KivyApp()
        view = KivyView()
        app.setDownloaderView(view)
        app.setDefaults(WINDOW_TITLE, DEFAULT_FOLDER)
        app.run()
        app.root.mainloop()
     
if __name__ == "__main__":
    main(sys.argv[1:])

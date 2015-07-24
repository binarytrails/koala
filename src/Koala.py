#!/usr/bin/python2.7

from KivyApp import KivyApp
from KivyView import KivyView
from ShellMenu import *

import sys

DESTINATION = DEFAULT_DESTINATION
PREFERRED_UI = DEFAULT_UI

def checkKoalaLaunchOptions(args):
    for arg in args:
        if LaunchOptions.HELP[0] in arg:
            print HELP_MESSAGE
            exit(0)
        
        elif LaunchOptions.DESTINATION[0] in arg:
            global DESTINATION
            DESTINATION = arg[len(LaunchOptions.DESTINATION[0]):]
        
        elif LaunchOptions.K[0] in arg:
            global PREFERRED_UI
            PREFERRED_UI = UI.KIVY
        
        else:
            print HELP_MESSAGE
            exit(0)

if __name__ == "__main__":
    checkKoalaLaunchOptions(sys.argv[1:])
    
    if PREFERRED_UI == UI.KIVY:
        app = KivyApp()
        view = KivyView()
        app.setDownloaderView(view)
        app.setOutputFolder(DESTINATION)
        #app.setYoutubeDownloader()
        app.run()
        #app.root.mainloop()


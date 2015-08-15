#!/usr/bin/python2.7

'''
    __                      __
 .-'  `'.._...-----..._..-'`  '-.
/                                \

|  ,   ,'                '.   ,  |
 \  '-/                    \-'  /
  '._|          _           |_.'
     |    /\   / \    /\    |
     |    \/   | |    \/    |
      \        \"/         /
       '.    =='^'==     .'
        `'--------------'
              Koala


Usage:
    koala.py [-v -o <output> -g <gui>]

Opitons:
    -v, --verbose       Show relevant output during the program execution.
    -o, --output=DIR    Output music to this directory [default: ~/Music].
    -g, --gui=<gui>     Use one of the GUIs from the following: (kivy,) [default: kivy].

Author: Vsevolod Ivanov
Project: https://github.com/sevaivanov/koala
'''

import sys
from docopt import docopt
from enum import Enum

# Goes before Kivy imports to overwrite Kivy --help.
args = docopt(__doc__, version='Koala 0.1')
# Removes them to avoid passing them to Kivy
sys.argv = sys.argv[0]

from KivyApp import KivyApp
from KivyView import KivyView

if __name__ == "__main__":
   
    output = args['--output']
    gui = args['--gui']

    if gui and gui not in ['kivy']:
        sys.exit('The %s GUI is not available. See --help.' % gui)
    
    if gui == 'kivy':
        app = KivyApp()
        view = KivyView()
        app.setDownloaderView(view)
        app.setOutputFolder(output)
        #app.setYoutubeDownloader()
        app.run()


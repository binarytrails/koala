from enum import Enum

class UI(Enum):
    KIVY=0,
    TKINTER=1

class LaunchOptions(Enum):
    H = "h?",
    D = "des=",
    T = "tk",
    K = "kivy"
    
WINDOW_TITLE = "KoalaBeatzHunter"
DEFAULT_DEST = "../../tmp/"
DEFAULT_UI = UI.KIVY
HELP_MESSAGE = """
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
         KoalaBeatzHunter

Usage: ./KoalaBeatzHunter.py des=folder

The default UI is Kivy, to change do:
$ ./KoalaBeatzHunter.py tk

Basic options:
    h?            <koala help message>
    d=            <destination folder>
    tk            <launches tkinter ui>
    kivy          <launches kivy ui>

(C) Koala from the north"""

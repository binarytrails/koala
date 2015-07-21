from enum import Enum

class UI(Enum):
    KIVY=0,
    TKINTER=1

class LaunchOptions(Enum):
    H = "h?",
    D = "d=",
    T = "tk",
    K = "kivy"
    
WINDOW_TITLE = "KoalaBeatzHunter"
DEFAULT_DEST = "~/Music/"
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

Author: Vsevolod Ivanov
Project: https://github.com/sevaivanov/koalabeatzhunter"""

from enum import Enum

class UI(Enum):
    KIVY=0

class LaunchOptions(Enum):
    HELP = "h?",
    DESTINATION = "d=",
    
WINDOW_TITLE = "Koala"
DEFAULT_UI = UI.KIVY
DEFAULT_DESTINATION = "~/Music/"
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
              Koala

Usage: ./Koala.py des=folder

Basic options:
    h?            <koala help message>
    d=            <destination folder>

Author: Vsevolod Ivanov
Project: https://github.com/sevaivanov/koala"""

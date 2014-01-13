import eyed3
from threading import Thread
"""
Eyed3 207kB

Issue:
Doesnt works in multithread.

Solution:
Works with Clock event of Kivy.
http://kivy.org/docs/_modules/kivy/clock.html

"""
filename = "../../tmp/AwesomeKoalaBeat.mp3"

def mainfunc():
    af = eyed3.load(filename)
    af.initTag()
    af.tag.artist = u"Koala"
    af.tag.album = None
    af.tag.title = u"I Am a Girlfriend"
    af.tag.track_num = 4
    af.tag.save()
    
    print af.tag.artist
    print af.tag.album
    print af.tag.title
    print af.tag.track_num

mainfunc()
"""
attempting to use libmagic on multiple threads will end in SEGV
"""
# thread = Thread(target = mainfunc, args=[])
# thread.start()

import src.app.custom.Utilities as utils
print utils.fileExists(filename)
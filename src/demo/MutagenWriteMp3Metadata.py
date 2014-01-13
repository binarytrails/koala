from mutagen.easyid3 import EasyID3
from threading import Thread
from mutagen.id3 import ID3, TIT2, TYER
"""
Mutagen 813kB

Issue:
Cant handle the album neither.

"""
filename = "../../tmp/AwesomeKoalaBeat.mp3"

def mainfunc(filename, title, artist, album, year):
    mp3f = EasyID3(filename)
    mp3f["year"] = unicode(year)
    mp3f.save()
    #OR
    tags = ID3()
    tags['TIT2'] = TIT2(encoding=3, text=u'just a title') #title
    tags['TYER'] = TYER(encoding=3, text=u'2000')  #year
    tags.save(filename)
    #BOTH doenst works for the year, GOD DAMN IT.

thread = Thread(target = mainfunc, args=[filename, "AwesomeKoalaBeat", "Koala", "AlbumKoala", "2000"])
thread.start()
import uuid

class Beat(object):
    '''
    Beat object, used in downloading & conversion queues
    '''
    __uid = uuid.uuid4()
    __url = None
    __title = None
    __artist = None
    __album = None
    __year = 0

    def __init__(self, url, title, artist, album, year):
        self.__url = url
        self.__title = title
        self.__artist = artist
        self.__album = album
        self.__year = year

    def Beat(self):
        return self

    def getId(self):
        return self.__uid

    def getUrl(self):
        return self.__url

    def getTitle(self):
        return self.__title

    def getArtist(self):
        return self.__artist

    def getAlbum(self):
        return self.__album

    def getYear(self):
        return self.__year
import unittest
from src.app.KivyApp import KivyApp
from src.downloader import Youtube
from src.app.custom.Error import YoutubeURL


class Test(unittest.TestCase):
    """
    Important: Popular video like the miley cyrus one, wont work.
    Cause: signature problem in get_video in the downloader.
    Ex: http://youtu.be/LrUvu1mlWco
    """
    def setUp(self):
        self.app = KivyApp()
        self.app.setYoutubeDownloader(Youtube.YouTube())
        
        self.app.acceptedVideoFormat = "mp4"
        self.valid_id = "Bc2sfKn0FOA"
        self.valid_url = "http://www.youtube.com/watch?v=" + self.valid_id

    def tearDown(self):
        pass
    
    def test_validateYoutubeURL_with_valid_short_url(self):
        #Arrange
        url  = "http://youtu.be/" + self.valid_id
        #Act
        code, error, url = self.app._validateYoutubeURL(url)
        #Assert
        self.assertTrue(code is 0)
        self.assertTrue(url == self.valid_url)
        self.assertTrue(error is None)
    
    def test_validateYoutubeURL_with_valid_embeded_url(self):
        #Arrange
        url  = "http://www.youtube.com/embed/" + self.valid_id
        #Act
        code, error, url = self.app._validateYoutubeURL(url)
        #Assert
        self.assertTrue(code is 0)
        self.assertTrue(url == self.valid_url)
        self.assertTrue(error is None)
        
    def test_validateYoutubeURL_with_valid_featured_url(self):
        #Arrange
        url  = "http://www.youtube.com/watch?v=" + self.valid_id + "&feature=feedu"
        #Act
        code, error, url = self.app._validateYoutubeURL(url)
        #Assert
        self.assertTrue(code is 0)
        self.assertTrue(url == self.valid_url)
        self.assertTrue(error is None)
        
    def test_validateYoutubeURL_with_valid_vesioned_url(self):
        #Arrange
        url = "http://www.youtube.com/v/" + self.valid_id + "?version=3&amp;hl=en_US"
        #Act
        code, error, url = self.app._validateYoutubeURL(url)
        #Assert
        self.assertTrue(code is 0)
        self.assertTrue(url == self.valid_url)
        self.assertTrue(error is None)
        
    def test_validateYoutubeURL_with_invalid_url(self):
        #Arrange
        wrong_id = "XXXXXXXXXXX"
        wrong_url = "http://www.youtube.com/watch?v=" + wrong_id
        #Act
        code, error, url = self.app._validateYoutubeURL(wrong_url)
        #Assert
        self.assertTrue(code is 1)
        self.assertTrue(url == wrong_url)
        self.assertTrue(error is str(YoutubeURL.INVALID_LINK[0]))

if __name__ == "__main__":
    t = unittest.main()

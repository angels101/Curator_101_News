import unittest
from models import news_source
Source = news_source.Source

class SourceTest(Unittest.TestCase):
    '''
    Test class to test the behaviour of source class
    '''
    def setUp(self):
        '''
        Set up method that will run before every test
        '''
        self.new_source = Source("bbc-news","BBC News","Use BBC News for up-to-the-minute news, breaking news, video, audio and feature stories. BBC News provides trusted World and UK news as well as local and regional perspectives. Also entertainment, business, science, technology and health news","http://www.bbc.co.uk/news","general","gb")

    def test_instance(self):
        self.assertTrue(isinstance(self.new_source,Source))

    
if __name__=='__main__':
    unittest.main() 
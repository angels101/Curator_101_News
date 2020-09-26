import unittest
from app.models import Articles

class ArticlesTest(unittest.TestCase):
    '''
    Test class to test the behaviour of the article class
    '''
    def setUp(self):
        '''
        set up method that will run before every Test
        '''
        self.new_article=Articles((32,"Abc news","T.W.Jones","Review","Frozen 2 soundtrack struggles in shadow of first","https://www.movie-zone.com","https:www.BMW.com/wecc/3fcx/wsx.jpg","23-Jan-2019",'Various artists, Frozen 2')


    def test_instance(self):
        self.assertTrue(isinstance(self.new_article,Articles))
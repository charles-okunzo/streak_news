import unittest

from app.models import News


class TestNews(unittest.TestCase):
  '''
  TestNews test class that defines the behaviour of the news class
  '''
  def setUp(self):
    '''
        setup class that will be run before any unit tests
    '''
    self.new_news_article = News('BBC News', 'Iraq dust storm', 'BBC News', 'A dust storm that has covered Iraq in an orange sheet is expected to continue into Monday.', "http://www.bbc.co.uk/news/world-61292334", "https://ichef.bbci.co.uk/news/1024/branded_news/16375/production/_124379909_gettyimages-1240370372.jpg", "2022-05-01T18:52:17.9429909Z")


  def test_instance(self):
    self.assertTrue(isinstance(self.new_news_article, News))

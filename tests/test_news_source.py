import unittest

from app.models import News_Source

class TestNewsSource(unittest.TestCase):
  '''
  TestNewsSource test class that defines behaviours of NewsSource class
  '''

  def setUp(self):

    '''
    setup class that will be run before any unit tests
    '''
    self.new_news_source = News_Source('abc-news', 'ABC News', "Your trusted source for breaking news, analysis, exclusive interviews, headlines, and videos at ABCNews.com.", "https://abcnews.go.com")

  def test__init__(self):
    self.assertEqual(self.new_news_source.id, 'abc-news')
    self.assertEqual(self.new_news_source.name, 'ABC News')

import urllib.request, json
from .models import News_Source, News

#getting api key
api_key = None
#getting base url
base_url = None

#getting sources url
source_url = None

def configure_request(app):
  global api_key, base_url, source_url

  api_key = app.config['NEWS_API_KEY']
  base_url = app.config['NEWS_BASE_URL']
  source_url = app.config['NEWS_SOURCES_URL']


def get_news_sources():
  '''
  get_news_sources function that returns a list of all news sources
  '''
  news_url = base_url.format(api_key)

  with urllib.request.urlopen(news_url) as news_source:
    news_source_data = news_source.read()
    news_source_response = json.loads(news_source_data)

    news_source_results = None

    if news_source_response['sources']:
      news_source_list = news_source_response['sources']
      news_source_results = process_results(news_source_list)

  return news_source_results

  
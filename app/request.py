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

  with urllib.request.urlopen("https://newsapi.org/v2/top-headlines/sources?apiKey=70c8875846af4ec9b0b97c2c7b52e327") as news_source:
    news_source_data = news_source.read()
    news_source_response = json.loads(news_source_data)

    news_source_results = None

    if news_source_response['sources']:
      news_source_list = news_source_response['sources']
      news_source_results = process_results(news_source_list)

  return news_source_results


def process_results(response_list):
  '''
  process results function that processes results and returns news source objects
  '''
  news_source_results = []
  for response in response_list:
    id = response.get('id')
    name = response.get('name')
    description = response.get('description')
    url = response.get('url')

    if response.get('language') == 'en':
      news_source_obj = News_Source(id, name, description, url)

      news_source_results.append(news_source_obj)

  return news_source_results



def get_news(id):
  '''
  get news function that returns a list of news from a sources
  '''
  get_news_url = source_url.format(id, api_key)


  with urllib.request.urlopen(get_news_url) as news:
    news_data = news.read()
    news_response = json.loads(news_data)


    news_results = None

    if news_response['articles']:
      news_list = news_response['articles']
      news_results = process_news_results(news_list)

  return news_results



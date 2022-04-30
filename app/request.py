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
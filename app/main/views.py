from flask import render_template

from app.request import get_news_sources
from . import main


@main.route('/')
def index():
  '''
  Index view function tat returns News Sources and their details
  '''
  title = 'Welcome to Streak News - All your favourite news sources in one place'
  news_sources = get_news_sources()
  return render_template('index.html', title = title, sources = news_sources)
from flask import render_template,request,redirect,url_for

from app.request import get_news, get_news_sources
from . import main


@main.route('/')
def index():
  '''
  Index view function tat returns News Sources and their details
  '''
  title = 'Welcome to Streak News - All your favourite news sources in one place'
  news_sources = get_news_sources()

  search_name = request.args.get('news_query')
  if search_name:
    return redirect(url_for('main.search', source_name = search_name))
  else:
    return render_template('index.html', title = title, sources = news_sources)


@main.route('/news/<news_id>')
def news(news_id):
  '''
  news function that return a list of articles from a news source
  '''
  news = get_news(news_id)
  title = f'Trending news articles'
  return render_template('news.html', news = news, title = title, news_id = news_id)



@main.route('/news/search/<source_name>')
def search(source_name):
  source_name_list = source_name.lower().split(' ')
  source_name_format = '-'.join(source_name_list)
  news_articles = get_news(source_name_format)
  return render_template('search_news.html', news = news_articles, source_name = source_name)

from flask import render_template
from . import main


@main.route('/')
def index():
  '''
  Index view function tat returns News Sources and their details
  '''
  title = 'Welcome to Streak News - All your favourite news sources in one place'
  return render_template('index.html')
from flask import Flask
from config import config_options



def create_app(config_name):
  app = Flask(__name__)


  #create app configurations
  app.config.from_object(config_options[config_name])

  #initialise extensions

  #register the blueprint
  from .main import main as main_blueprint
  app.register_blueprint(main_blueprint)


  #add views,forms, error

  return app

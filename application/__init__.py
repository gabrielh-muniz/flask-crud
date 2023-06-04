from flask import Flask
from .routes import create_routes
from .utils.profile_api import import_profiles, record

def create_app():
  app = Flask(__name__)

  create_routes(app)

  #record(import_profiles())
  
  return app

from . import user_view

def create_routes(app):
  app.register_blueprint(user_view.view, url_prefix='/')

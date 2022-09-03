from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'feowpkfok123910249030dans'

    from .views import views
    from .auth_views import auth_views

    app.register_blueprint(views, url_prefix="/")
    app.register_blueprint(auth_views, url_prefix="/auth/")

    return app
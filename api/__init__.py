from flask import Flask
from api.auth import blueprint as auth_blueprint


def create_app():
    app = Flask(__name__)
    app.register_blueprint(auth_blueprint)
    return app

# app/__init__.py
from flask import Flask

from app.views.about.routes import about_blueprint
from app.views.assistant.routes import assistant_blueprint
from app.views.index.routes import index_blueprint
from app.views.our_team.routes import our_team_blueprint
from app.views.weather.routes import weather_blueprint
from config import Config


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Register blueprints
    app.register_blueprint(index_blueprint)
    app.register_blueprint(weather_blueprint)
    app.register_blueprint(assistant_blueprint)
    app.register_blueprint(about_blueprint)
    app.register_blueprint(our_team_blueprint)

    return app

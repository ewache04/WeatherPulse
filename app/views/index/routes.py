# app/views/index/index.py
import os
from flask import redirect, session

from app.urls.urls_patterns.set_urls_patterns import initialize_urls_patterns
from app.views.index import index_blueprint
from utils.sessions.session_utils import create_session, clear_session


@index_blueprint.route('/')
def index():
    # Clear the session if session already exist
    if session:
        clear_session()

    # Initialize URL patterns
    url_patterns = initialize_urls_patterns()

    # Ensure url_patterns is not None
    if not session.get('url_patterns'):
        raise ValueError("Failed to initialize or store URL patterns in session.")

    # Store URL patterns in the session
    create_session('url_patterns', url_patterns)

    # Set the application name in the session if not already present
    if not session.get('app_name'):
        app_name = os.getenv('APP_NAME', 'Weather App')
        create_session('app_name', app_name)

    # Initialize the 'weather_processing' session variable
    create_session('weather_processing', True)

    # Safely retrieve the weather route from the session's URL patterns
    weather_route = url_patterns.get('weather', {}).get('redirect', '/')

    # Redirect to the weather route or the default route if not found
    return redirect(weather_route)

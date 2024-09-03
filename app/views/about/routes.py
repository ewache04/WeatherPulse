# app/about/routes.py
from flask import render_template, session

from app.views.about import about_blueprint
from utils.assistant.assistant_mode.assistant_mode import inactivate_assistant_mode
from utils.sessions.session_utils import update_session


@about_blueprint.route('/about')
def about():
    
    # Update session data
    update_session('weather_processing', False)

    # Get URL patterns from session
    url_patterns = session.get('url_patterns', {})

    # Get the path to the about template
    about_template = url_patterns.get('about', {}).get('render')

    # Prepare context to pass to the template
    context = {
        'url_patterns': url_patterns,
    }

    # Update assistant mode to inactive
    inactivate_assistant_mode()

    # Pass URL patterns and other context to the template
    return render_template(
        about_template,
        **context
    )

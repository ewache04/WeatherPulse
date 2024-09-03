# app/views/assistant/routes.py
from flask import render_template, session
from app.views.assistant import assistant_blueprint
from utils.assistant.assistant_mode.assistant_mode import activate_assistant_mode
from utils.assistant.text_response.assistant_text_response import assistant_text_response
from utils.auth.assistant.client import authenticate_client
from utils.sessions.session_utils import update_session


@assistant_blueprint.route('/assistant')
def assistant():

    # Update session data
    update_session('weather_processing', False)

    # Fetch the API client
    client = authenticate_client()

    # Get weather data from session
    weather_data = session.get('weather_data')

    # Generate assistant text response
    responses = assistant_text_response(client, weather_data)

    # Retrieve responses and error messages from the returned object
    assistant_text_reply = responses.get('assistant_text_response')
    assistant_detailed_response = responses.get('assistant_detailed_response')
    assistant_error = responses.get('assistant_error_response')

    # Get URL patterns from session
    url_patterns = session.get('url_patterns', {})

    # Get the path to the assistant template
    assistant_template = url_patterns.get('assistant', {}).get('render', 'default_assistant_template.html')

    # Prepare context to pass to the template
    context = {
        'url_patterns': url_patterns,
        'assistant_text_response': assistant_text_reply,
        'assistant_detailed_response': assistant_detailed_response,
        'assistant_error': assistant_error,
    }

    # Make assistant mode active
    activate_assistant_mode()

    # Render and return the assistant template with context
    return render_template(assistant_template, **context)

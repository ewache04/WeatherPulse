# app/weather/routes.py
from flask import render_template, request, session

from app.views.weather import weather_blueprint
from utils.assistant.assistant_mode.assistant_mode import inactivate_assistant_mode
from utils.location.get_user_location import get_user_ip_location
from utils.sessions.session_utils import update_session, create_session
from utils.weather.process_weather_data import process_weather_data


@weather_blueprint.route('/weather', methods=['GET', 'POST'])
def weather():
    city = None
    state = None
    country = None
    number_of_days = 5  # Default value if not specified

    # Update session data
    update_session('weather_processing', True)

    if request.method == 'POST':
        city = request.form.get('city')

        state = request.form.get('state')
        try:
            update_session('state', state)
        except:
            create_session('state', state)

        country = request.form.get('country')
        number_of_days = int(request.form.get('number_of_days', 1))
        number_of_days = min(max(number_of_days, 1), 5)  # Ensure within range

        # Process weather data based on user input
        process_weather_data(city, state, country, number_of_days)

    else:
        location_data = get_user_ip_location()

        # Fetch location based on IP if no POST data
        if location_data:
            ip_address = location_data.get('ip', 'Unknown')
            city = location_data.get('city', 'Unknown')
            state = location_data.get('region', 'Unknown')
            country = location_data.get('country', 'Unknown')
            create_session('country', country)
            latitude = location_data.get('latitude', 'Unknown')
            longitude = location_data.get('longitude', 'Unknown')

        # Process weather data based on detected location
        process_weather_data(city, state, country, number_of_days)

    # Get weather data and colors from session
    weather_data = session.get('weather_data')
    day_colors = session.get('day_colors', {})

    # Get URL patterns from session
    url_patterns = session.get('url_patterns', {})
    weather_template = url_patterns.get('weather', {}).get('render')

    context = {
        'weather_data': weather_data,
        'day_colors': day_colors,
        'region': state,
        'country': country,
        'url_patterns': url_patterns
    }

    # Update assistant mode to inactive
    inactivate_assistant_mode()

    return render_template(weather_template, **context)

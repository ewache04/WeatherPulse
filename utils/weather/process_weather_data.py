# app/views/weather/utils.py

from utils.sessions.session_utils import create_session, update_session
from utils.weather.get_weather_data import get_weather_data
from utils.weather.assign_colors_to_dates import assign_colors_to_dates


def process_weather_data(city, state, country, number_of_days):
    # Retrieve weather data with city, state, and country
    weather_data = get_weather_data(city, state, country, number_of_days)
    print(weather_data)

    if weather_data:
        # Create or update sessions for weather data, city, country, number of days, and day colors
        create_or_update_session('weather_data', weather_data)
        create_or_update_session('city', weather_data.get('city', {}).get('name', ''))
        create_or_update_session('country', weather_data.get('city', {}).get('country', ''))
        create_or_update_session('number_of_days', number_of_days)

        # Apply the color assignment function
        day_colors = assign_colors_to_dates(weather_data.get('forecast', []))
        create_or_update_session('day_colors', day_colors)
    else:
        create_session('error', 'Unable to retrieve weather data.')


def create_or_update_session(key, value):
    """Helper function to create or update session values."""
    try:
        # Attempt to create the session value
        create_session(key, value)
    except KeyError:
        # If a KeyError occurs, update the session value
        update_session(key, value)
    except Exception as e:
        # Log any other exceptions
        print(f"An error occurred while managing session '{key}': {e}")
        # Optionally, handle additional actions or notifications

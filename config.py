# config.py
import os


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'mysecretkey')
    WEATHER_API_KEY = os.environ.get('WEATHER_SOURCE_API_KEY')
    WEATHER_BASE_URL = f"http://api.openweathermap.org/data/2.5/forecast"
    LOCATION_IP_BASE_URL = "https://api64.ipify.org?format=json"
    OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY')


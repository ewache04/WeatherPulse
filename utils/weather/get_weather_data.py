# utils/weather/get_weather_data.py
import requests
from config import Config
from datetime import datetime, timedelta


def get_weather_data(city=None, state=None, country=None, number_of_days=None):
    total_intervals = number_of_days * 8  # 8 intervals per day of 3 hours

    # Construct the location query parameter
    location_query = city
    if state:
        location_query += f",{state}"
    if country:
        location_query += f",{country}"

    try:
        response = requests.get(Config.WEATHER_BASE_URL, params={
            'q': location_query,
            'appid': Config.WEATHER_API_KEY,
            'units': 'metric',
            'cnt': total_intervals
        })

        # Check if the request was successful
        if response.status_code != 200:
            print(f"Failed to retrieve data: {response.status_code}, {response.text}")
            return None

        data = response.json()

        if 'list' not in data or 'city' not in data:
            print(f"Unexpected API response structure: {data}")
            return None

        forecast = []
        # Adjust today to match the API's timezone (assuming UTC)
        today = datetime.utcnow().date()
        end_date = today + timedelta(days=number_of_days)

        for item in data.get('list', []):
            dt_txt = item.get('dt_txt')
            if dt_txt:
                forecast_datetime = datetime.strptime(dt_txt, '%Y-%m-%d %H:%M:%S')
                forecast_date = forecast_datetime.date()

                # Include only the forecast for today and the specified number of days
                if today <= forecast_date < end_date:
                    forecast.append({
                        'date': dt_txt,
                        'temperature': item['main'].get('temp', 'N/A'),
                        'description': item['weather'][0].get('description', 'N/A'),
                        'sea_level': item['main'].get('sea_level', 'N/A'),
                        'ground_level': item['main'].get('grnd_level', 'N/A'),
                        'humidity': item['main'].get('humidity', 'N/A'),
                        'pressure': item['main'].get('pressure', 'N/A'),
                        'wind_speed': item['wind'].get('speed', 'N/A'),
                        'clouds': item['clouds'].get('all', 'N/A'),
                        'visibility': item.get('visibility', 'N/A'),
                        'temp_max': item['main'].get('temp_max', 'N/A'),
                        'temp_min': item['main'].get('temp_min', 'N/A'),
                        'sunrise': datetime.fromtimestamp(data['city'].get('sunrise', 0)).strftime('%Y-%m-%d %H:%M:%S'),
                        'sunset': datetime.fromtimestamp(data['city'].get('sunset', 0)).strftime('%Y-%m-%d %H:%M:%S'),
                    })

        if forecast:
            # Calculate the number of full days covered
            days_covered = len(set(item['date'].split(' ')[0] for item in forecast))

            return {
                'city': {
                    'name': data['city']['name'],
                    'country': data['city']['country'],
                    'population': data['city'].get('population', 'N/A')
                },
                'days_covered': days_covered,
                'forecast': forecast
            }
        else:
            print("No forecast data found for the given period.")
            return None

    except Exception as e:
        print(f"An error occurred: {e}")
        return None

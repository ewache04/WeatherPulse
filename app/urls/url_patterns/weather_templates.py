# app/url_patterns/weather_templates.py
def get_weather_templates(ext='html'):
    return {
        "weather": {
            'render': f'weather_templates/weather.{ext}',
            'redirect': 'weather'
        },
        "weather_form": {
            'render': f'weather_templates/weather_form.{ext}',
        },
        "weather_details": {
            'render': f'weather_templates/weather_details.{ext}',
        },
    }

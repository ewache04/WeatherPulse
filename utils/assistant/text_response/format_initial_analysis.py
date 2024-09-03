# utils/assistant/text_response/format_weather_output.py

def format_initial_analysis():
    return """
Here is a comprehensive analysis of the weather data for Hartford, US for the next 5 days:

1. Day 1 (Enter date here. eg. August 31, 2024):
   - Weather: [Provide weather description with temperature range.]
   - Precipitation: [Describe any expected precipitation.]
   - Wind: [Specify wind speed and conditions.]
   - Precautions: [Give advice on what to carry or how to prepare.]

2. Day 2 (Enter date here. eg. September 1, 2024):
   - Weather: [Provide weather description with temperature range.]
   - Precipitation: [Describe any expected precipitation.]
   - Wind: [Specify wind speed and conditions.]
   - Precautions: [Give advice on what to carry or how to prepare.]

3. Day 3 (Enter date here. eg. September 2, 2024):
   - Weather: [Provide weather description with temperature range.]
   - Wind: [Specify wind speed and conditions.]
   - Precautions: [Give advice on what to carry or how to prepare.]

4. Day 4 (Enter date here. eg. September 3, 2024):
   - Weather: [Provide weather description with temperature range.]
   - Wind: [Specify wind speed and conditions.]
   - Precautions: [Give advice on what to carry or how to prepare.]

5. Day 5 (Enter date here. eg. September 4, 2024):
   - Weather: [Provide weather description with temperature range.]
   - Wind: [Specify wind speed and conditions.]
   - Precautions: [Give advice on what to carry or how to prepare.]

Overall, it is advisable to check the weather forecast regularly for any updates and to dress appropriately for the changing weather conditions. Stay prepared for rain on some days and enjoy the clear skies on others.
    """

# utils/assistant/text_response/instructions_prompt.py
def instructions_prompt(weather_data=None):
    message = f""" I am providing you with a weather forecast. Please analyze this weather data in detail, 
    considering any necessary precautions for both indoor and outdoor activities. Here is the dataset:

    {weather_data}

    Your analysis should be comprehensive and consider the main aspects of the weather data that a typical person 
    would be interested in."""
    return message

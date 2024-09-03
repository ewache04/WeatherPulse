# utils/assistant/text_response/generate_weather_activity_guidance.py
def generate_weather_activity_guidance(assistant_text_response=None):
    message = f"""
    Based on the following weather forecast:

    {assistant_text_response}

    Please provide detailed guidance on how to adjust daily activities such as:
    - Clothing choices
    - Commuting and transportation
    - Outdoor activities and sports
    - Work and school routines
    - Health and wellness considerations
    - Food and dietary preferences
    - Energy usage at home
    - Gardening and agriculture
    - Mood and mental health
    - Travel plans
    - Home maintenance tasks
    - Exercise routines
    - Social activities and events

    Your advice should be specific, practical, and consider both indoor and outdoor settings. Address any potential 
    risks and offer precautions where necessary."""
    return message

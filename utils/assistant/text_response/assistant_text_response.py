# utils/assistant/text_response/assistant_text_response.py

from utils.assistant.text_response.format_detailed_guidance import format_detailed_guidance
from utils.assistant.text_response.format_initial_analysis import format_initial_analysis
from utils.assistant.text_response.generate_weather_activity_guidance import generate_weather_activity_guidance
from utils.assistant.text_response.instructions_prompt import instructions_prompt
from utils.sessions.session_utils import session, create_session  # Assuming session utility is imported


def assistant_text_response(client, weather_data=None):
    if not client:
        return {
            'assistant_text_response': None,
            'assistant_detailed_response': None,
            'assistant_error_response': "Client API key not found."
        }

    try:
        model = 'gpt-3.5-turbo'
        temperature = 0.2
        max_tokens = 3600

        # Retrieve city and country from session
        city = session.get('city')
        country = session.get('country')

        if not city or not country:
            return {
                'assistant_text_response': None,
                'assistant_detailed_response': None,
                'assistant_error_response': "City or country information is missing in session."
            }

        # First Query: Generate Initial Weather Analysis
        instructions = instructions_prompt(weather_data)
        preferred_format = format_initial_analysis()

        response = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "user", "content": "You are an expert in analyzing weather data and providing weather-based "
                                            "advice. Can you help me?"},
                {"role": "assistant", "content": "Yes! What do you need?"},
                {"role": "user", "content": f'Here is what I want you to do: {instructions}'},
                {"role": "user", "content": f'Please ensure the measurement metric is tailored to what is mostly used '
                                            f'in {city}, {country}.'},
                {"role": "user", "content": f'Preferred Format: {preferred_format}'},
                {"role": "assistant", "content": "Ok."},
            ],
            max_tokens=max_tokens,
            temperature=temperature,
        )

        # Check response structure
        if response.choices and response.choices[0].message:
            assistant_reply = response.choices[0].message.content or 'No content found'
        else:
            return {
                'assistant_text_response': None,
                'assistant_detailed_response': None,
                'assistant_error_response': "Unexpected response format from initial analysis."
            }

        # Second Query: Generate Detailed Guidance Based on Initial Analysis
        detailed_instructions = generate_weather_activity_guidance(assistant_reply)
        preferred_format = format_detailed_guidance()

        response = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "user", "content": "Based on your previous analysis, please provide further guidance."},
                {"role": "user", "content": f'Previous Analysis: {detailed_instructions}'},
                {"role": "assistant", "content": "Sure, here's my detailed advice."},
                {"role": "user", "content": f'Preferred Format: {preferred_format}'},
                {"role": "user", "content": f'Please ensure the measurement metric is tailored to what is mostly used '
                                            f'in {city}, {country}.'},
                {"role": "user", "content": "Please ensure the Detailed Guidance covers all the days."},
                {"role": "assistant", "content": "Ok."},
            ],
            max_tokens=max_tokens,
            temperature=temperature,
        )

        # Check response structure
        if response.choices and response.choices[0].message:
            detailed_reply = response.choices[0].message.content or 'No content found'

            return {
                'assistant_text_response': assistant_reply,
                'assistant_detailed_response': detailed_reply,
                'assistant_error_response': None,

            }
        else:
            return {
                'assistant_text_response': assistant_reply,
                'assistant_detailed_response': None,
                'assistant_error_response': "Unexpected response format from detailed guidance."
            }

    except Exception as e:
        # Enhanced error handling with more context
        error_message = f"Error in processing the request: {str(e)}"
        return {
            'assistant_text_response': None,
            'assistant_detailed_response': None,
            'assistant_error_response': error_message
        }

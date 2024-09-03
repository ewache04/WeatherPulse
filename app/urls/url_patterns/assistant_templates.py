# app/url_patterns/weather_templates.py
def get_assistant_templates(ext='html'):
    return {
        "assistant": {
            'render': f'assistant_templates/assistant.{ext}',
            'redirect': '/assistant'
        },

    }

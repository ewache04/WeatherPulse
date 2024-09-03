# utils/auth/assistant/api_key.py
import openai
from openai import OpenAI

from config import Config


# Function to authenticate the OpenAI client
def authenticate_client(api_key=None):
    if api_key is None:
        api_key = Config.OPENAI_API_KEY

    if api_key is None:
        raise ValueError("API key is required but not provided.")

    return OpenAI(api_key=api_key)

# Example usage (uncomment to use)
# if __name__ == '__main__':
#     client = authenticate_client()
#     print(client)

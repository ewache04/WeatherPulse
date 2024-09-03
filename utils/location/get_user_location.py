# utils/location/get_user_location.py
import requests
from config import Config


def get_ip():
    """
    Fetch the IP address of the user from the configured base URL.
    """
    try:
        response = requests.get(Config.LOCATION_IP_BASE_URL)
        response.raise_for_status()
        return response.json().get("ip")
    except requests.RequestException as e:
        print(f"Error fetching IP address: {e}")
        return None


def get_user_ip_location():
    """
    Retrieve the user's full location details based on their IP address.
    """
    try:
        # Get the user's IP address
        ip_address = get_ip()

        if ip_address is None:
            return None

        # Fetch location details using the IP address
        response = requests.get(f'https://ipapi.co/{ip_address}/json/')
        response.raise_for_status()

        # Return the full set of location data
        return response.json()

    except requests.RequestException as e:
        print(f"Error occurred while fetching location data: {e}")
        return None


if __name__ == "__main__":
    location_data = get_user_ip_location()

    if location_data:
        # Only print the selected fields
        print(f"IP Address: {location_data['ip']}")
        print(f"City: {location_data['city']}")
        print(f"Region: {location_data['region']}")
        print(f"Country: {location_data['country_name']}")
        print(f"Latitude: {location_data['latitude']}")
        print(f"Longitude: {location_data['longitude']}")
    else:
        print("Failed to retrieve location data.")

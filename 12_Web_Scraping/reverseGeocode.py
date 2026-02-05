# This script uses the Positionstack Reverse Geocoding API to convert latitude and longitude
# coordinates into a human-readable address. It sends a request with the provided API key,
# retrieves the first result, and returns the formatted address label, with basic error handling.

import requests


def get_address_from_coords(lat, lon, api_key):
    url = "http://api.positionstack.com/v1/reverse"
    params = {
        'access_key': api_key,
        'query': f"{lat},{lon}",
        'limit': 1
    }

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()  # Raise exception for HTTP errors
        data = response.json()

        # Extract the first address in the array
        if data.get('data'):
            return data['data'][0]['label']
        else:
            return "No address found for these coordinates."

    except Exception as e:
        return f"An error occurred: {e}"


# Usage
result = get_address_from_coords(6.6778, 3.1654, 'YOUR_API_KEY_HERE')
print(result)


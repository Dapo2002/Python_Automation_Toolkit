# umbrella_reminder.py - Queries OpenWeatherMap API for Abuja's forecast and triggers an
# SMS alert if precipitation is detected

import json
import requests
from textMyself import textMyself

APPID = 'YOUR_API_KEY_HERE'

location = 'Abuja'

# Download the JSON data from OpenWeatherMap.org's APi.
url = f'https://api.openweathermap.org/data/2.5/forecast?q={location}&cnt=3&APPID={APPID}'
response = requests.get(url)
response.raise_for_status()

# Uncomment to see the raw JSON text:
# pprint.pprint(response.text)

# Load JSON data into a Python variable.
weatherData = json.loads(response.text)

# Print weather descriptions.
w = weatherData['list']
print(f'Current weather in {location}')
forecast = w[0]['weather'][0]['main'] + ' - ' + w[0]['weather'][0]['description']
print(forecast)
print()
if 'rain' in forecast:
    print('Sending SMS...')
    textMyself('Carry an Umbrella')
else:
    print('umbrella not needed')

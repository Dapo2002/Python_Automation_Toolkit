#! python3
# getOpenWeather.py - Prints the weather for a location from the command line.

import json
import requests
import sys

APPID = 'YOUR_API_KEY_HERE'

# Compute location from command line argument
if len(sys.argv) < 2:
    print('Usage: getOpenWeather.py city_name, 2-letter_country_code')
    sys.exit()
location = ' '.join(sys.argv[1:])

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
print(w[0]['weather'][0]['main'], '-', w[0]['weather'][0]['description'])
print()
print('Tomorrow:')
print(w[1]['weather'][0]['main'], '-', w[1]['weather'][0]['description'])
print()
print('Day after tomorrow:')
print(w[2]['weather'][0]['main'], '-', w[2]['weather'][0]['description'])

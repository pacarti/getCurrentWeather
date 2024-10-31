#! python3
# Gets the necessary lat and lon data from location(1st result) for the updated API request of OpenWeatherMap

import json, requests, sys

APPID = sys.argv[1]

if len(sys.argv) < 2:
        print('Usage: getOpenWeateher.py APP_ID city_name')
        sys.exit()

location = ' '.join(sys.argv[2:])

# Download the JSON data from OpenWeatherMap.org's API.
url = 'https://api.openweathermap.org/geo/1.0/direct?q=%s&appid=%s' % (location, APPID)
response = requests.get(url)
response.raise_for_status()

# See the JSON data:
# print(response.text)

# Load JSON data into a Python variable
geocodingData = json.loads(response.text)

# Get lat and lon:
lat = geocodingData[0]['lat']
lon = geocodingData[0]['lon']

# print(type(geocodingData[0]['lat']))
# print(geocodingData[0]['lon'])

# Print lat and lon:
print('Latitude of %s: %s' % (location, str(lat)))
print('Longitude of %s: %s' % (location, str(lon)))

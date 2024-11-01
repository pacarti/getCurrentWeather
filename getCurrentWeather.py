#! python3
# Prints out the current weather data from location given as second sys arguemnt(in command line)

import json, requests, sys, pprint

if len(sys.argv) < 2:
        print('Usage: getOpenWeateher.py APP_ID city_name')
        sys.exit()

APPID = sys.argv[1]

location = ' '.join(sys.argv[2:])

# Download the JSON data from OpenWeatherMap.org's API.
url = 'https://api.openweathermap.org/geo/1.0/direct?q=%s&appid=%s' % (location, APPID)
response = requests.get(url)
# 401 HTTP Error will be most likely caused by wrong API key hence the exception:
try: 
        response.raise_for_status()
except requests.exceptions.HTTPError:
        print("Incorrect API key!")
        exit()

# See the JSON data:
# print(response.text)

# Load JSON data into a Python variable
geocodingData = json.loads(response.text)

# Get lat and lon:
try:
        lat = geocodingData[0]['lat']
except IndexError:
        print("Incorrect city name\n(or it doesn't exist in OpenWeatherMap database, if so, please enter the nearest city name).")
        exit()
lon = geocodingData[0]['lon']

# print(type(geocodingData[0]['lat']))
# print(geocodingData[0]['lon'])

# Print lat and lon:
# print('Latitude of %s: %s' % (location, str(lat)))
# print('Longitude of %s: %s' % (location, str(lon)))

weather_url = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={APPID}'
# w_response - weather response
w_response = requests.get(weather_url)
w_response.raise_for_status()

weatherData = json.loads(w_response.text)

# Print weather data:
# pprint.pprint(weatherData)

# Get temperature:
tempKelvin = weatherData['main']['temp']
feelsLikeK = weatherData['main']['feels_like']

# Convert Kelvin temperature to Celsius:
tempCelsius = round(tempKelvin - 272.15, 2)
feelsLikeC = round(feelsLikeK- 272.15, 2)

pressure = weatherData['main']['pressure']
humidity = weatherData['main']['humidity']

windSpeed = weatherData['wind']['speed']
windSpeedMH = windSpeed * 3600
windSpeedKMH = windSpeedMH / 1000

# Print weather info:
print('Current weather in %s:' % (location))
print(weatherData['weather'][0]['description'])

print('Temperature: ', end='')
print(str(tempCelsius) + ' ' + '\N{DEGREE SIGN}C')

print('Feels like: ', end = '')
print(str(feelsLikeC) + ' ' + '\N{DEGREE SIGN}C')

print('Humidity: ' + str(humidity) + ' %')

print('Pressure: ' + str(pressure) + ' hPa')

# print('Wind speed: ' + str(windSpeed) + ' m/s')
# print('Wind speed: ' + str(windSpeedMH) + ' m/h')
print('Wind speed: ' + str(windSpeedKMH) + ' km/h')

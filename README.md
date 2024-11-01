# getCurrentWeather
The script fetches the current weather of given location and prints it on the screen. The data in JSON format is retrieved from openweathermap.org through API call.


**Important**: The script needs an API key to make a call. You can obtain it for free from openweathermap.org, you have just to create a free account. Then, you can obtain it at:
https://home.openweathermap.org/api_keys

The script first uses Geocoding API(https://openweathermap.org/api/geocoding-api) to translate the location name into its latitude and longitude(this only functionality is also available in the getLatLon.py script - it prints lat and lon on the screen). This is needed to avoid using deprecated "Direct geocoding" which is unmaintained anymore and is less precise for finding the geolocation data.

After retrieving the necessary data, the script prints out the following current weather data of given location:
* Current weather description
* Temperature(in °C)
* Feels like temperature(in °C)
* Humidity
* Pressure(in hPa)
* Wind speed(in km/h)

## Usage
Give execution permission to the script:

<code>chmod +x getCurrentWeather</code>

<br/>
### How to run
<code>./getCurrentWeather <API_key> \<location\></code>

<br/>
Location is the name of the city for which you want to print out the current weather.
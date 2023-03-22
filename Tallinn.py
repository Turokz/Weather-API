import requests
import datetime

# Tallinn coordinates
latitude = 59.4370
longitude = 24.7536

# Set the Yo.no API endpoint for the weather forecast
api_endpoint = f"https://api.met.no/weatherapi/locationforecast/2.0/compact?lat={latitude}&lon={longitude}"

# Send HTTP GET request to the API endpoint
response = requests.get(api_endpoint, headers={'User-Agent': 'Weather API/Turok'})

# Get JSON data from the API response
data = response.json()

# Get current date and time
now = datetime.datetime.now()

# Current temperature
current_temperature = data['properties']['timeseries'][0]['data']['instant']['details']['air_temperature']

# Temperature data for the next 3 hours
temperature_data = data['properties']['timeseries'][:3]

# Labels for each hour
labels = {
    1: "1 hour",
    2: "2 hours",
    3: "3 hours"
}

print(f"Current temperature is {current_temperature} C") # Print the current temperature

for i, temp in enumerate(temperature_data): # enumerate() returns the index and the value of the item in the list
    temperature = temp['data']['instant']['details']['air_temperature'] # Get the temperature
    timestamp = temp['time'] # Get the timestamp
    newLabel = labels[i + 1] # Get the label for the current hour 
    print(f"In {newLabel}, the temperature will be {temperature} C") # Print the temperature for the current hour
 
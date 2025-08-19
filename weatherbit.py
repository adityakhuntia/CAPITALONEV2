#API=5e5d67bec4584892bf0c531997974a87

import requests
from opencage.geocoder import OpenCageGeocode


import os
from dotenv import load_dotenv

load_dotenv()
OPENCAGE = os.getenv("OPENCAGE")
WEATHERBIT=os.getenv("WEATHERBIT")
TWILIO_AUTH = os.getenv("TWILIO_AUTH")


def get_lat_lon(location, api_key):
    geocoder = OpenCageGeocode(api_key)
    result = geocoder.geocode(location)
    if result:
        lat = result[0]['geometry']['lat']
        lon = result[0]['geometry']['lng']
        return lat, lon
    else:
        print(f"Location '{location}' not found.")
        return None, None

def get_ag_weather_forecast(lat, lon, weatherbit_api_key):
    url = f"https://api.weatherbit.io/v2.0/forecast/agweather"
    params = {
        'lat': lat,
        'lon': lon,
        'key': weatherbit_api_key,
        'units': 'M'  # Metric units (Celsius, m/s, mm)
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error fetching data: {response.status_code}")
        return None

def weatherdet(location):

    open_cage_api_key = OPENCAGE
    weatherbit_api_key = WEATHERBIT

    lat, lon = get_lat_lon(location, open_cage_api_key)
    if lat and lon:
        forecast = get_ag_weather_forecast(lat, lon, weatherbit_api_key)
        if forecast:
            print(f"Weather forecast for {location}:")
            return forecast
        else:
            return "Failed to retrieve weather forecast."
    else:
        return "Invalid location."
    



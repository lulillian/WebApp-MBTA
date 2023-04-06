# Your API KEYS (you need to use your own keys - very long random characters)
import urllib.request
import json
import requests
from pprint import pprint



# Useful URLs (you need to add the appropriate parameters for your requests)
MAPBOX_BASE_URL = "https://api.mapbox.com/geocoding/v5/mapbox.places"
MBTA_BASE_URL = "https://api-v3.mbta.com/stops"
MAPBOX_TOKEN='pk.eyJ1IjoibGx1MSIsImEiOiJjbGZ2bzBhNnYwN3diM2x0c2I2N21lejFqIn0.bcxBv8L3Dt77gayTgFlvWw'
MBTA_API_KEY='2c89154874d04963af236fa9fd38f514'


# A little bit of scaffolding if you want to use it


def get_json(url: str) -> dict:
    """
    Given a properly formatted URL for a JSON web API request, return a Python JSON object containing the response to that request.

    Both get_lat_long() and get_nearest_station() might need to use this function.
    """
    # f=urllib.request.urlopen(url)
    # response_text=f.read().decode('utf-8')
    # response_data=json.loads(response_text)
    # return (response_data)
    response = requests.get(url)
    data = response.json()
    return data



def get_city(place_name: str) -> tuple[str, str]:
    """
    Given a place name or address, return a (latitude, longitude) tuple with the coordinates of the given place.

    See https://docs.mapbox.com/api/search/geocoding/ for Mapbox Geocoding API URL formatting requirements.
    """
    url=f'https://api.mapbox.com/geocoding/v5/mapbox.places/{place_name}.json?access_token={MAPBOX_TOKEN}'
    data=get_json(url)
    # print(data)
    city=data['features'][1]['context'][2]['text']
    return city
    # print (city)


get_city('Fenway Park')


def get_temp(place_name: str) -> float:
    """
    Returns the current temperature in Farenheit of a certain city
    """
    APIKEY='ada48657851c101cb5c56f796ed3195e'
    city=get_city(place_name)
    url=f'http://api.openweathermap.org/data/2.5/weather?q={city},us&APPID={APIKEY}'

    # print(url)

    f=urllib.request.urlopen(url)
    response_text=f.read().decode('utf-8')
    response_data=json.loads(response_text)
    # print(response_data)
    temp_kel=response_data['main']['temp']
    temp_far=1.8*(float(temp_kel)-273.15)+32
    print(f'The current temperature at {place_name} in {city} is {temp_far} degrees Farenheit.')

# get_temp('Boston Commons')
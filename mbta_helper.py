# Your API KEYS (you need to use your own keys - very long random characters)
import urllib.request
import json
import requests
from pprint import pprint
import math 



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



def get_lat_long(place_name: str) -> tuple[str, str]:
    """
    Given a place name or address, return a (latitude, longitude) tuple with the coordinates of the given place.

    See https://docs.mapbox.com/api/search/geocoding/ for Mapbox Geocoding API URL formatting requirements.
    """
    url=f'https://api.mapbox.com/geocoding/v5/mapbox.places/{place_name}.json?access_token={MAPBOX_TOKEN}'
    data=get_json(url)
    lat_long=data['features'][0]['geometry']['coordinates']
    lat_long_tup= (lat_long[1],lat_long[0])
    return lat_long_tup


#print(get_lat_long('Boston Commons'))


def get_nearest_station(latitude: str, longitude: str) -> tuple[str, bool]:
    """
    Given latitude and longitude strings, return a (station_name, wheelchair_accessible) tuple for the nearest MBTA station to the given coordinates.

    See https://api-v3.mbta.com/docs/swagger/index.html#/Stop/ApiWeb_StopController_index for URL formatting requirements for the 'GET /stops' API.
    """
    url=f'https://api-v3.mbta.com/stops?sort=distance&filter%5Blatitude%5D={latitude}&filter%5Blongitude%5D={longitude}'
    data_dict=get_json(url)
    stopdict = data_dict['data'][0]
    nearest_station=stopdict['attributes']['name']
    wheelchair=stopdict['attributes']['wheelchair_boarding']
    if wheelchair>=1:
        wheelchair= True
    else:
        wheelchair= False
        
    # print(nearest_station)
    # print(wheelchair)
    result=(nearest_station,wheelchair)
    return result

# print(get_nearest_station('42.355628831221196', '-71.06576851534196'))



def find_stop_near(place_name: str) -> tuple[str, bool]:
    """
    Given a place name or address, return the nearest MBTA stop and whether it is wheelchair accessible.

    This function might use all the functions above.
    """
    coordinates_tuples=get_lat_long(place_name)
    # print(coordinates_tuples)
    lat=coordinates_tuples[0]
    long=coordinates_tuples[1]
    final_result=get_nearest_station(lat,long)
    return final_result

# print(find_stop_near('Fenway Park'))


def get_city(place_name: str):
    """
    Given a place name or address, return a (latitude, longitude) tuple with the coordinates of the given place.

    See https://docs.mapbox.com/api/search/geocoding/ for Mapbox Geocoding API URL formatting requirements.
    """
    url=f'https://api.mapbox.com/geocoding/v5/mapbox.places/{place_name}.json?access_token={MAPBOX_TOKEN}'
    data=get_json(url)
    # print(data)
    # city=data['features'][2]['context'][2]['text']
    city=data['features'][0]['context'][2]['text']
    return city
    # print (city)

# get_city('Harvard Univeristy')


def get_temp(city: str):
    """
    Returns the current temperature in Farenheit of a certain city
    """
    APIKEY='ada48657851c101cb5c56f796ed3195e'
    # city=get_city(place_name)
    url=f'http://api.openweathermap.org/data/2.5/weather?q={city},us&APPID={APIKEY}'

    # print(url)

    f=urllib.request.urlopen(url)
    response_text=f.read().decode('utf-8')
    response_data=json.loads(response_text)
    # print(response_data)
    temp_kel=response_data['main']['temp']
    temp_far=math.floor(1.8*(float(temp_kel)-273.15)+32)
    # print(temp_far)
    return temp_far
    # print(f'The current temperature at {place_name} in {city} is {temp_far} degrees Farenheit.')

get_temp('Boston')

# def main():
#     place_name='Fenway Park'
#     stop_result=find_stop_near(place_name)
#     print(stop_result)




# if __name__ == '__main__':
#     main()

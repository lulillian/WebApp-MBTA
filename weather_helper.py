import urllib.request
import json


def get_temp(city: str) -> float:
    """
    Returns the current wind speed in meters per second for the given city from OpenWeatherMap.

    Parameters:
    city -- the name of the city (str)
    country -- the two-letter country code for the city (str)
    """
    APIKEY='ada48657851c101cb5c56f796ed3195e'
    url=f'http://api.openweathermap.org/data/2.5/weather?q={city},us&APPID={APIKEY}'

    # print(url)

    f=urllib.request.urlopen(url)
    response_text=f.read().decode('utf-8')
    response_data=json.loads(response_text)
    # print(response_data)
    temp=response_data['main']['temp']
    print(temp)

# if __name__=="__main__":
print(get_temp('wellesley'))

    



# When you've completed your function, uncomment the following lines and run this file to test.

# print(get_wind_speed('wellesley', 'us')) # you can replace the arguments with your hometown city and country code. If there are two (or more) words in the city name, you need to add '+' or '%20' between words, i.e. if you are from New York, the first arugment should be converted to "new+york" or "new%20york".

## Expected output - of course the wind speed in your hometown might be different:
# 12.0
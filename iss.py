import numpy as np
import requests
import json
from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent='geolocate.py')
from datetime import datetime

# Function to find the lat and long of inputted country
def geolocate(country):   
    # find the country
    try:
        loc = geolocator.geocode(country)
        # return lat and long
        lat = loc.latitude
        lon = loc.longitude
        return (lat, lon)
    # otherwise
    except:
        return np.nan


location = input('Please enter your country to find out when the ISS will pass over your given country: ')

# invoke the geolate function on the user's country
geocode = geolocate(location)
latitude = geocode[0]
longitude = geocode[1]

# print(geocode)
# print(latitude)
# print(longitude)


parameters = {
    'lat': latitude,
    'lon': longitude
}

# Requesting data from Open-notify API
request = requests.get('http://api.open-notify.org/iss-pass.json', params=parameters)
# print(request.status_code)

def jprint(obj):
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)
    
response = request.json()
# print(response)

# print(jprint(response))

# rqst = response['request']
# # print(rqst)

pass_time = response['response']

risetime = []
for d in pass_time:
    time_stamp = d['risetime']
    risetime.append(time_stamp)
# print(risetime)

# Converting to current time
times = []

for rt in risetime:
    time = datetime.fromtimestamp(rt)
    print(time)
    




    

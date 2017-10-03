import csv
import requests
import json

api_key = 'AIzaSyA4yS3tPdlWbGyR44z_O2lkRAaY8ASLfkg'
file_name = 'asd_lat_lng.txt'
school_locations = {}

with open('asd_schools.csv', 'rt') as csvfile:
    school_names = csv.reader(csvfile)
    for row in school_names:
        print(row)
        school_name = row
        url = 'https://maps.googleapis.com/maps/api/geocode/json?address={school_name},+Anchorage,+AK&key={key}'.format(
            school_name=row,
            key=api_key
        )
        response = requests.get(url)
        response_json = response.json()['results'][0]
        location = response_json['geometry']['location']
        lng = location['lng']
        lat = location['lat']
        school_locations[row[0]] = {}
        school_locations[row[0]]['lng'] = lng
        school_locations[row[0]]['lat'] = lat

with open(file_name, 'w') as fd:
    json.dumps(school_locations, fd)


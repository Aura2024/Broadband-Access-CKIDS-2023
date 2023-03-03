import requests
from bs4 import BeautifulSoup
import csv
from csv import reader
import pandas
cols = ['Zipcode', 'Street', 'Unit', 'City', 'Lat', 'Long']
csv_file = 'LA_City.csv'

lines = (line for line in open(csv_file, 'r'))
header = next(lines)
for row in lines:
    row = row.split(',')
    lat = row[4]
    long = row[5]
    url = 'https://geocoding.geo.census.gov/geocoder/locations/coordinates?parameters'
    params = {
        "returntype": "locations",
        "searchtype": "coordinates",
        "benchmark": "Public_AR_Current",
        "vintage": "Current_Current",
        "x": long,
        "y" : lat,
        "format": "html"
        }
    response = requests.get(url, params=params)
    soup = BeautifulSoup(response.content, "html.parser")
    targets = soup.find_all("span", class_="resultItem", text = "GEOID: ")
    entries = dict()
    for target in targets:
        entries.update({target.next_sibling: ""})
    for entry in entries.keys():
        if len(entry) >= 14:
            with open('blockID.csv', 'a') as f_out:
                f_out.write(entry + '\n')
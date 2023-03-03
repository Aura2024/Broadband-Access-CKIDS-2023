import requests
from bs4 import BeautifulSoup

index =len(open('blockID.csv', 'r').readlines())

addresses = (line for line in open('reverse_addresses.csv', 'r'))
for i in range(index):
    next(addresses)

with open('blockID.csv', 'a') as f_out:
    for line in addresses:
        address = line.strip().split(',')
        lat = address[4]
        long = address[5]

        url = 'https://geocoding.geo.census.gov/geocoder/geographies/coordinates'
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
        heading = soup.find_all("span", class_="resultHeading", text = "2020 Census Blocks: ")

        for i in heading:
            next_sibling = i.next_sibling
            while len(next_sibling) < 14:
                next_sibling = next_sibling.next_sibling
            print(next_sibling)
            address.append(next_sibling)
        f_out.write(",".join(address)+ '\n')

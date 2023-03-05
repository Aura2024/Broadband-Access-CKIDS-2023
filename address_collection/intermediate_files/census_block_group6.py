import requests
from bs4 import BeautifulSoup



def get_blockID(in_file, out_file):
    addresses = (line for line in open(in_file, 'r'))
    index = len(open(out_file, 'r').readlines())

    for i in range(index):
        next(addresses)


    with open(out_file, 'a') as f_out:
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



file_six = 'LA_City_6.csv'

file_six_out = 'LA_City_6_out.csv'

get_blockID(file_six, file_six_out)


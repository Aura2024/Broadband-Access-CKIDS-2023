# import required module
import os
import json

# read directory
directory = 'ca'
# write directory
end_directory = 'All County Addresses Unique'

# create write directory
try:
    os.mkdir(end_directory)
except OSError as error:
    pass

# iterate over files in that directory
for filename in os.listdir(directory):
    # check for only geojson files
    if ".meta" not in filename:
        # check for only addresses files
        if "-addresses-" in filename:
            print(filename)
            # create a csv file with the same name as the geojson file
            all_addresses = []
            csv_file = filename.replace("geojson", "csv")
            # create a path variable for opening files
            path = "ca/" + filename
            end_path = end_directory + "/" + csv_file
            # open csv file for the county in write
            with open(end_path, "w", encoding='utf-8') as outfile:
                # Write the header
                outfile.write('Street, Unit, City,Zipcode\n')
                # Add each address to the csv file
                count = 0
                for line in open(path, encoding='utf-8'):
                    line = json.loads(line)
                    number = line['properties']['number'].replace(",", "")
                    street = line['properties']['street'].replace(",", "")
                    unit = line['properties']['unit'].replace(",", "")
                    city = line['properties']['city'].rstrip(", CA")
                    zipcode = line['properties']['postcode'][0:5]
                    address = number + ' ' + street + ',' + unit + ',' + city + ',' + zipcode
                    new_address = address.split(',')
                    new_address.pop(1)
                    # We will not use this address if zipcode is missing
                    if len(zipcode) == 5 and number != "-1" and number.isdigit() == True and number != "0" and street != "" and "/" not in number:
                        # Remove duplicates
                        if new_address not in all_addresses:
                            all_addresses.append(new_address)
                            outfile.write(address + '\n')
                            count += 1
                            if len(all_addresses) == 100:
                                all_addresses = all_addresses[95:]
                print(end_path + " has " + str(count) + " addresses")
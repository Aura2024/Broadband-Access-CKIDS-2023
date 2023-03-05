
file_start = 'LA_City_'
file_end = '_out.csv'
with open('Main_LA_City.csv', 'w') as out_file:
    header = 'Zip,Address,Unit,City,Latitude,Longitude,Block ID'
    out_file.write(header + '\n')
    for i in range(1, 10):
        with open(file_start + str(i) + file_end, 'r') as in_file:
            for line in in_file:
                out_file.write(line)


main_file = 'LA_City.csv'


with open(main_file, 'r') as in_file:
    i = 0
    for line in in_file:
        print(i)
        copy = line.strip().split(',')
        if len(copy) == 7:
            copy.pop(2)
            line = ",".join(copy) + '\n'


        if i/110898 < 1:
            with open('LA_City_1.csv', 'w') as out_file:
                out_file.write(line)
                i += 1
        elif i/110898 < 2:
            with open('LA_City_2.csv', 'w') as out_file:
                out_file.write(line)
                i += 1
        elif i/110898 < 3:
            with open('LA_City_3.csv', 'w') as out_file:
                out_file.write(line)
                i += 1
        elif i/110898 < 4:
            with open('LA_City_4.csv', 'w') as out_file:
                out_file.write(line)
                i += 1
        elif i/110898 < 5:
            with open('LA_City_5.csv', 'w') as out_file:
                out_file.write(line)
                i += 1
        elif i/110898 < 6:
            with open('LA_City_6.csv', 'w') as out_file:
                out_file.write(line)
                i += 1
        elif i/110898 < 7:
            with open('LA_City_7.csv', 'w') as out_file:
                out_file.write(line)
                i += 1
        elif i/110898 < 8:
            with open('LA_City_8.csv', 'w') as out_file:
                out_file.write(line)
                i += 1
        else:
            with open('LA_City_9.csv', 'w') as out_file:
                out_file.write(line)
                i += 1


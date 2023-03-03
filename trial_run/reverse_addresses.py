content = [line.strip().split(',') for line in open('LA_City.csv', 'r')]
header = content[0]
content = content[1:]
reverse_content = []

while len(content) > 0:
    reverse_content.append(content[-1])
    content.pop(-1)


with open('reverse_addresses.csv', 'w') as f_out:
    f_out.write(",".join(header) + '\n')
    for line in reverse_content:
        f_out.write(",".join(line) + '\n')
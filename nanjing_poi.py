line_new_list = []
with open('nanjing_poi.txt') as f:
    for line in f:
        item = line.rsplit(',')
        x = item[1]
        y = item[2]
        if len(x) > 10:
            x = x[:10]
            y = y[:9] + '\n'
        line_new = item[0] + ',' + x + ',' + y
        line_new_list.append(line_new)
with open('nanjing_poi2.txt','w') as f:
    for line in line_new_list:
        f.write(line)
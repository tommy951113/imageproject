prop_result_list = []
with open('prop_result.txt') as f:
    for line in f:
        item = {}
        item['id'] = line.rsplit(',')[0]
        item['prop'] = line.rsplit(',')[1]
        prop_result_list.append(item)

panoid_result_list = []
with open('panoid_ruijinlu.txt') as f:
    for line in f:
        item = {}
        item['x'] = line.rsplit(',')[0]
        item['y'] = line.rsplit(',')[1]
        item['id'] = line.rsplit(',')[2] 
        panoid_result_list.append(item)
    
for item in prop_result_list:
    for (index, item2) in enumerate(panoid_result_list):
        if item['id'] == item2['id'][:-1]:
            panoid_result_list[index]['prop'] = item['prop']

# print(panoid_result_list)
with open('xyprop_result.txt','w') as f:
    for item in panoid_result_list:
        f.write(item['x'])
        f.write(',')
        f.write(item['y'])
        f.write(',')
        f.write(item['prop'])

poi_list = []
with open('nanjing_poi2.txt') as f:
    for line in f:
        poi_list.append(line.rsplit(',')[0])
poi2_list = []

item_new_list = []
with open('nanjing_poi3.txt') as f:
    for i,line in enumerate(f):
        # 切分成数组
        item = line.rsplit(',')
        item_new = ''
        item_new += poi_list[i] + ',' + item[0][:10] + ',' + item[1][:9]
        item_new_list.append(item_new + '\n')

with open('nanjing_poi4.txt','w') as f:
    for line in item_new_list:
        f.write(line)
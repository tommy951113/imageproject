import codecs

poi_list = []
with codecs.open('nanjing.csv','r','utf-8') as f:
    for line in f:
        line_list = line.rsplit(',')
        poi = line_list[0]
        x = line_list[-6]
        y = line_list[-5]
        item = poi + ',' + x + ',' + y + '\n'
        poi_list.append(item)
with codecs.open('nanjing_poi.txt','w','utf-8') as f:
    for poi in poi_list:
        f.write(poi)

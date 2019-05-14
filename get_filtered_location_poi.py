# -*- coding: utf-8 -*-
import codecs
# 获得通过缓冲区分析得到的签到点所对应的Poi
DIR = 'G:\\research_data\\nanjing\\checkin_poi_filtered.txt'
DIR2 = 'nanjing_poi4.txt'  
fid_list = []

# 获取fid列表
with codecs.open(DIR,'r','utf-8') as f:
    for line in f:
        fid = line.rsplit(',')[-3]
        fid_list.append(fid)

poiid_list = []

for fid in fid_list:
    with open(DIR2) as f:
        for index, line in enumerate(f):
            if index + 1 == int(fid):
                poiid_list.append(line)
                break

with open('poiid_filterd.txt','w') as f:
    for poi in poiid_list:
        f.write(poi)
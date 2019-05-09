# 提取出citycode为0025的记录
import codecs
city_list = []
i = 0
with codecs.open('jiangsu.csv','r','utf-8') as f:
    for line in f:
        i+=1
        print(i)
        item_list = line.rsplit(',')
        if len(item_list) >= 9 and item_list[-4] == '0025':
            city_list.append(line)

with codecs.open('nanjing.csv','w','utf-8') as f:
    for line in city_list:
        f.write(line)
# -*- coding: utf-8 -*-
import requests
import codecs
import re 
import time

API_URL = 'https://m.weibo.cn/api/container/getIndex?containerid=100101'
TAIL = '_-_weibofeed'

def remove_links(text):
    # 移除带链接的文字
    text = re.sub(r'<.+>','',text)
    return text

# 获取单个poi的所有微博内容
def get_weibo(poiid):
    i = 0
    weibo_list = []
    # 分页读取微博内容
    while True:
        flag = 0
        time.sleep(0.2)
        i += 1
        r = requests.get(API_URL + poiid + TAIL + '&page=' + str(i))
        result = r.json()
        # 排除返回空网址，或返回此点已经删除的情况
        if result['ok'] == 0:
            break
        if result['data']['pageInfo']['page_title'] == '此点已经删除':
            break
        card_group = result['data']['cards'][0]['card_group']
        for card in card_group:
            if card['card_type'] == 9:
                text = card['mblog']['text']
                text = remove_links(text)
                if text:
                    weibo_list.append(text)
            else:
                flag = 1
                break
        if flag == 1:
            break
    
    if i == 1:
        with open('weiboresult.txt','a') as f:
            f.write(poiid + '\n')
    else:
        with codecs.open('weiboresult.txt','a','utf-8') as f:
            f.write(poiid + ',')
            for weibo in weibo_list:
                f.write(weibo + ';')
            f.write('\n')

# 批量读取poiid并获取微博数据
poi_list = []
with open('poiid_fillterd4.txt') as f:
    for line in f:
        poiid = line.rsplit(',')[0]
        poi_list.append(poiid)

poi_list = poi_list[119:]

for poiid in poi_list:
    get_weibo(poiid)

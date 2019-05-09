import requests
import codecs
import re 

poi_list = []
POI_ID = 'B2094655D665A4FC4792'
API_URL = 'https://m.weibo.cn/api/container/getIndex?containerid=100101' + POI_ID
TAIL = '_-_weibofeed'

def remove_links(text):
    # 移除带链接的文字
    text = re.sub(r'<.+>','',text)
    return text

# 获取单个poi的所有微博内容
i = 0
weibo_list = []
while True:
    i += 1
    r = requests.get(API_URL + TAIL + '&page=' + str(i))
    if r.json()['ok'] == 0:
        break
    result = r.json()
    card_group = result['data']['cards'][0]['card_group']
    for card in card_group:
        text = card['mblog']['text']
        text = remove_links(text)
        if text:
            weibo_list.append(text)

if i == 1:
    print('地点已被删除')
else:
    with codecs.open('B2094655D76BA6FE409C.txt','w','utf-8') as f:
        for weibo in weibo_list:
            f.write(weibo + '\n')

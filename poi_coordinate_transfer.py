# 将高德坐标转换为gps坐标
import requests
point_list = []

API_KEY = '17bcc48a3f5266bc08a2bc6a13ca99ae'

def write_to_file(results):
    with open('nanjing_poi3.txt','a') as f:
        f.write(results + ';')
        
# transfer function
def transfer(locations):
    # print(locations)
    url = 'https://restapi.amap.com/v3/assistant/coordinate/convert'
    r = requests.get(url + '?key=' + API_KEY + '&locations=' + locations + '&coordsys=gps')
    return r.json()['locations']

with open('nanjing_poi2.txt') as f:
    locations = ''
    i = 0
    for line in f:
        point = line.rsplit(',')
        location = point[1] + ',' + point[2][:-1]
        i += 1
        if i % 19 == 0:
            locations += location
            results = transfer(locations)
            locations = ''
            write_to_file(results)
            continue
        locations += (location + '|')
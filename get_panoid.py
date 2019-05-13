import requests
import time

# 读取腾讯坐标并获取该坐标对应的全景panoid（5次/s，每次45个点）
# load coordinates
web_service = "https://apis.map.qq.com/ws/streetview/v1/getpano"
KEY = "4QVBZ-2YNLO-JZNWX-SALX6-BKVSH-VBFUX"
panoid_list = []
pointlist = []

def write_to_file(location):
    time.sleep(0.2)
    url = web_service + "?location=" + location + "&key=" + KEY
    r = requests.get(url)
   
    with open("nanjing_panoids.txt", "a") as f:
        if r.json()['status'] != 0:
            f.write('\n')
        else:
            detail = r.json()['detail']
            f.write(str(detail['location']['lat']))
            f.write(',')
            f.write(str(detail['location']['lng']))
            f.write(',')
            f.write(detail['id'] + '\n')

with open("nanjing_point_tencent.txt") as f:
    for line in f:
        point = {}
        point['x'] = line.rsplit(',')[0] 
        point['y'] = line.rsplit(',')[1]
        pointlist.append(point)

for index, point in enumerate(pointlist):
    location = point['x'] + ',' + point['y'][:-1]
    write_to_file(location)
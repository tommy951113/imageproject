import requests
import time

# load coordinates 
pointlist = []
web_service = "https://apis.map.qq.com/ws/streetview/v1/getpano"
radius = 50
key = "4QVBZ-2YNLO-JZNWX-SALX6-BKVSH-VBFUX"
panoid_list = []
point_list = []

with open("G:\\research_data\\ruijin_road\\sample_points_translated.txt") as f:
    for index,line in enumerate(f):
        point = {}
        point['x'] = line.rsplit(',')[0][:10]
        point['y'] = line.rsplit(',')[1][:9]
        pointlist.append(point)

for index, point in enumerate(pointlist):
    time.sleep(0.25)
    url = web_service + "?location=" + point['x'] + ',' + point['y'] + "&radius=" + str(radius) + "&key=" + key
    r = requests.get(url)
    detail = r.json()['detail']
    panoid_list.append(detail)

with open("panoid_ruijinlu.txt","w") as f:
    for panoid in panoid_list:
        f.write(str(panoid['location']['lat']) + ',' + str(panoid['location']['lng']) + ',' +panoid['id'] + '\n')

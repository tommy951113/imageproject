import requests
import time

# load coordinates
pointlist = []
# web_service = "https://apis.map.qq.com/ws/streetview/v1/getpano"
web_service = "https://apis.map.qq.com/ws/coord/v1/translate"
radius = 50
KEY = "4QVBZ-2YNLO-JZNWX-SALX6-BKVSH-VBFUX"
# panoid_list = []
point_list = []

def write_to_file(locations):
    time.sleep(0.2)
    url = web_service + "?locations=" + locations + "&type=3&key=" + KEY
    r = requests.get(url)
    locations_translated = r.json()['locations'] 
    with open("nanjing_point_tencent.txt", "a") as f:
        for point in locations_translated:
            f.write(
                str(point['lat']) + ',' +
                str(point['lng']) + '\n')

with open("nanjing_point2.txt") as f:
    for line in f:
        point = {}
        point['x'] = line.rsplit(',')[1] 
        point['y'] = line.rsplit(',')[0]
        pointlist.append(point)

locations = ''
for index, point in enumerate(pointlist):
    locations += point['x'][:-1] + ',' + point['y'] + ';'
    if (index + 1) % 42 == 0:
        write_to_file(locations[:-1])
        locations = ''
import requests
from PIL import Image
from io import BytesIO
import os
import time

# 读取坐标获得腾讯街景图像
COORDINATE_TRANSLATE_SERVICE = 'https://apis.map.qq.com/ws/coord/v1/translate'
PANOID_GET_SERVICE = 'https://apis.map.qq.com/ws/streetview/v1/getpano'
STREETVIEW_IMAGE_SERVICE = 'https://apis.map.qq.com/ws/streetview/v1/image'
KEY = "4QVBZ-2YNLO-JZNWX-SALX6-BKVSH-VBFUX"
RADIUS = 50
DIR = 'F:\\ImageProjects'

# def gps2tencent(gps):
#     # gps坐标转腾讯坐标
#     r = requests.get(COORDINATE_TRANSLATE_SERVICE + '?locations=' + gps +
#                      '&type=1&key=' + KEY)
#     location = r.json()['locations'][0]
#     return location

def download_streetview(panoid):
    time.sleep(0.2)
    for i in range(0, 360, 60):
        r = requests.get(STREETVIEW_IMAGE_SERVICE + "?size=960x640&pano=" +
                         panoid + "&heading=" + str(i) + "&pitch=0&key=" + KEY)
        try:
            image = Image.open(BytesIO(r.content))
            image.save(
                os.path.join(dir, panoid) + '\\' + panoid + "_" + str(i) +
                ".jpg")
            return 'done'
        except IOError:
            return panoid

def get_streetview_images():
    panoid_list = []
    # 读取Panoid文件
    with open('nanjing_panoids.txt') as f:
        for line in f:
            if line != '\n':
                panoid = line.rsplit(',')[2][:-1]
                panoid_list.append(panoid)
    # panoid_list为有效的panoid list
    result_list = []
    for panoid in panoid_list:
        result = download_streetview(panoid)
        result_list.append(result)
    
    # 输出取图结果，如果没取到图，则输出panoid
    with open('streetview_result.txt','a') as f:
        for result in result_list:
            f.write(result + '\n')
    # r = requests.get(PANOID_GET_SERVICE + "?location=" + str(point['lat']) +
    #                  ',' + str(point['lng']) + "&radius=" + str(RADIUS) +
    #                  "&key=" + KEY)
    # panoid = r.json()['detail']['id']
    

# get_streetview_images('31.934835,119.063863')
get_streetview_images()
import requests
from PIL import Image
from io import BytesIO
import os

# 输入gps坐标直接获得腾讯街景图像
COORDINATE_TRANSLATE_SERVICE = 'https://apis.map.qq.com/ws/coord/v1/translate'
PANOID_GET_SERVICE = 'https://apis.map.qq.com/ws/streetview/v1/getpano'
STREETVIEW_IMAGE_SERVICE = 'https://apis.map.qq.com/ws/streetview/v1/image'
KEY = "4QVBZ-2YNLO-JZNWX-SALX6-BKVSH-VBFUX"
RADIUS = 50
DIR = 'F:\\ImageProjects'

def gps2tencent(gps):
    # gps坐标转腾讯坐标
    r = requests.get(COORDINATE_TRANSLATE_SERVICE + '?locations=' + gps + '&type=1&key=' + KEY)
    location = r.json()['locations'][0]
    return location

def get_streetview_images(gps):
    point = gps2tencent(gps)
    # 获取panoid  （获取panoid出错）
    r = requests.get(PANOID_GET_SERVICE + "?location=" + str(point['lat']) + ',' + str(point['lng']) + "&radius=" + str(RADIUS) + "&key=" + KEY)
    panoid = r.json()['detail']['id']
    for i in range(0,360,60):
        r = requests.get(STREETVIEW_IMAGE_SERVICE + "?size=960x640&pano=" + panoid + "&heading=" + str(i) + "&pitch=0&key="+KEY)
        try:
            image = Image.open(BytesIO(r.content))
            image.save(os.path.join(dir, panoid) + '\\' + panoid + "_" + str(i) + ".jpg")
        except IOError:
            print('no available image')

get_streetview_images('31.934835,119.063863')
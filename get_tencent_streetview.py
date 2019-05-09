import requests
import time
import os
from PIL import Image
from io import BytesIO
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


# web_service = "https://apis.map.qq.com/ws/streetview/v1/getpano"
pano_image_service = "https://apis.map.qq.com/ws/streetview/v1/image"
# base_url = "https://map.qq.com/#pano="
# radius = 50
key = "4QVBZ-2YNLO-JZNWX-SALX6-BKVSH-VBFUX"

# get 10000 panoid
# i = 0
# for point in point_list[:10000]:
#     i += 1
#     print(str(i))
#     url = web_service + "?location=" + point['y'] + ',' + point['x'] + '&radius=' + str(radius) + '&key=' + key
#     r = requests.get(url)
#     if(r.json()['status'] == 0):
#         detail = r.json()['detail']
#         panoid_list.append(detail)


# panoid_list = []
# with open("panoid.txt") as f:
# 	for line in f:
# 		panoid_list.append(line.rsplit(',')[2])

# driver = webdriver.Chrome()
# driver.get(base_url + panoid_list[0])
# time.sleep(8)
# resultlist = []
# for (i,panoid) in enumerate(panoid_list):
#     streetview_url = base_url + panoid
#     time.sleep(2)
#     driver.get(streetview_url)

#     # click hist btn
#     elem = driver.find_element_by_class_name("PanoPhotoHisBtn")
#     elem.click()
#     photocells = driver.find_elements_by_class_name("PanoPhotoCell")


#     # get panoid
#     for photocell in photocells:
#         img = photocell.find_element_by_tag_name("img")
#         src = img.get_attribute("src")
#         title = photocell.find_element_by_class_name("PanoPhotoTitle")
#         streetview_date = title.get_attribute("title")
#         result = {}
#         result["point"] = pointlist[i]
#         result["panoid"] = src.rsplit("&")[6].rsplit('=')[1]
#         result["date"] = streetview_date
#         resultlist.append(result)

# with open('panoid_result.txt','w') as f:
#     for result in resultlist:
#         f.write(result["point"]['x'])
#         f.write(' ')
#         f.write(result['point']['y'])
#         f.write(' ')
#         f.write(result['panoid'])
#         f.write(' ')
#         f.write(result['date'])
#         f.write('\n')

# pano_service = "https://apis.map.qq.com/ws/streetview/v1/image"
# size = "600x300"
# pitch = -60
# heading = 180
# url_pano = pano_service + "?pano=" + id + "&size=" + size + "&pitch=" + str(pitch) + "&heading=" + str(heading) + "&key=" + key
# r = requests.get(url_pano)
# i = Image.open(BytesIO(r.content))
# i.save("streetview_nanjing3.jpg")

# load panoids
panoid_list = []
with open("panoid_ruijinlu.txt") as f:
    for line in f:
        panoid = line.rsplit(',')[2][:-1]
        panoid_list.append(panoid)

dir = "images\\ruijinlu"
# panoid_list = ['10101022120925124124900','10101022120925124127500']
for panoid in panoid_list:
    if not os.path.exists(os.path.join(dir, panoid)):
        os.makedirs(os.path.join(dir, panoid))
    for i in range(0,360,60):
        r = requests.get(pano_image_service + "?size=960x640&pano="+panoid+"&heading=" + str(i) + "&pitch=0&key="+key)
        try:
            image = Image.open(BytesIO(r.content))
            image.save(os.path.join(dir, panoid) + '\\' + panoid + "_" + str(i) + ".jpg")
        except IOError:
            print('no available image')
import requests
import time
from PIL import Image
from io import BytesIO
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

# load coordinates 
# pointlist = []
# with open("G:\\research_data\\ruijin_road\\sample_points_translated.txt") as f:
#      for index,line in enumerate(f):
#         point = {}
#         point['x'] = line.rsplit(',')[0][:10]
#         point['y'] = line.rsplit(',')[1][:9]
#         pointlist.append(point)

web_service = "https://apis.map.qq.com/ws/streetview/v1/getpano"
pano_image_service = "https://apis.map.qq.com/ws/streetview/v1/image"
base_url = "https://map.qq.com/#pano="
radius = 50
key = "4QVBZ-2YNLO-JZNWX-SALX6-BKVSH-VBFUX"

# panoid_list = []
# for index, point in enumerate(pointlist):
# 	# if (index + 1) % 5 == 1:
# 	time.sleep(0.25)
# 	url = web_service + "?location=" + point['x'] + ',' + point['y'] + "&radius=" + str(radius) + "&key=" + key
# 	r = requests.get(url)
# 	detail = r.json()['detail']
# 	panoid_list.append(detail)

# with open("panoid.txt","w") as f:
# 	for panoid in panoid_list:
# 		f.write(str(panoid['location']['lat']) + ',' + str(panoid['location']['lng']) + ',' +panoid['id'] + '\n')

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



# for panoid in panoid_list:
    
    # print(src)
# print(resultlist)
# html = requests.get(base_url + id)

# soup = BeautifulSoup(html.text, 'html.parser')
# print(soup.prettify())
# pano_photo_cell = soup.find_all("div",class_="PanoPhotoCell")
# print(pano_photo_cell)

# pano_service = "https://apis.map.qq.com/ws/streetview/v1/image"
# size = "600x300"
# pitch = -60
# heading = 180
# url_pano = pano_service + "?pano=" + id + "&size=" + size + "&pitch=" + str(pitch) + "&heading=" + str(heading) + "&key=" + key
# r = requests.get(url_pano)
# i = Image.open(BytesIO(r.content))
# i.save("streetview_nanjing3.jpg")

# load panoids
# with open("panoid_result.txt") as f:
#     panoid = f.readline().rsplit(' ')[2]
# url = pano_image_service + "?size=138x187&pano="+panoid+"&heading=0&pitch=-90&key="+ key
# r = requests.get(url)
# i = Image.open(BytesIO(r.content))
panoid = "10101003141207140925500"
# i.save(panoid + "1.jpg")
# r = requests.get(pano_image_service + "?size=960x640&pano="+panoid+"&heading=0&pitch=-90&key="+key)
# i = Image.open(BytesIO(r.content))
# i.save(panoid + "1.jpg")
for i in range(0,360,45):
    r = requests.get(pano_image_service + "?size=960x640&pano="+panoid+"&heading=" + str(i) + "&pitch=-45&key="+key)
    image = Image.open(BytesIO(r.content))
    image.save(panoid + "_" + str(i) + ".jpg")

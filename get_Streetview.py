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
pointlist = []
with open("G:\\research_data\\ruijin_road\\sample_points_translated.txt") as f:
     for index,line in enumerate(f):
        point = {}
        point['x'] = line.rsplit(',')[0][:10]
        point['y'] = line.rsplit(',')[1][:9]
        pointlist.append(point)

web_service = "https://apis.map.qq.com/ws/streetview/v1/getpano"
base_url = "https://map.qq.com/#pano="
radius = 50
key = "4QVBZ-2YNLO-JZNWX-SALX6-BKVSH-VBFUX"
panoid_list = []
for point in pointlist:
    url = web_service + "?location=" + point + "&radius=" + str(radius) + "&key=" + key
    r = requests.get(url)
    id = r.json()['detail']['id']
    panoid_list.append('panoid_list')

streetview_url = base_url + panoid_list[0]
driver = webdriver.Chrome()
driver.get(streetview_url)
link = driver.find_element_by_css_selector("a[href='https://get.adobe.com/cn/flashplayer/']")
link.click()

time.sleep(5)

# click hist btn
elem = driver.find_element_by_class_name("PanoPhotoHisBtn")
elem.click()
photocells = driver.find_elements_by_class_name("PanoPhotoCell")
resultlist = []

for photocell in photocells:
    img = photocell.find_element_by_tag_name("img")
    src = img.get_attribute("src")
    title = photocell.find_element_by_class_name("PanoPhotoTitle")
    streetview_date = title.get_attribute("title")
    result = {}
    result["panoid"] = src.rsplit("&")[6].rsplit('=')[1]
    result["date"] = streetview_date
    resultlist.append(result)

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
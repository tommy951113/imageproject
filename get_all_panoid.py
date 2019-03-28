# from bs4 import BeautifulSoup
# import requests
 
# url = "https://map.baidu.com/#panoid=09002500011603100854132478D&panotype=street&heading=293.5&pitch=7.84&l=21&tn=B_NORMAL_MAP&sc=0&newmap=1&shareurl=1&pid=09002500011603100854132478D"
# 1. get panoid from location
# 2. get all panoids from url
# 3. get streetview from panoid
# url = "http://api.map.baidu.com/place/v2/search?"
# get panoid from location
# r = requests.get('')
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
driver = webdriver.Chrome()

# driver.implicitly_wait(1)
url = "https://map.baidu.com/#panoid=09002500121710221336023316G&panotype=street&heading=92.52&pitch=0&l=21&tn=B_NORMAL_MAP&sc=0&newmap=1&shareurl=1&pid=09002500121710221336023316G"
driver.implicitly_wait(2)
driver.get(url)
# wait = WebDriverWait(driver, 5)
# try:
#     element = WebDriverWait(driver,10).until(
#         EC.presence_of_element_located((By.ID,"pano-funcarea"))
#     )
# finally:
#     driver.quit()
# elem = driver.find_element_by_name('word')
# elem.send_keys("厦门")
# elem.send_keys(Keys.RETURN)
# elem = driver.find_element_by_class_name('panorama')
# print(element)
elem = driver.find_element_by_class_name("photo-mask")
# elem = driver.find_elements_by_class_name("panoAlbum-item")
# elem = driver.find_element_by_id("pano-zoomout-btn")
# ActionChains(driver).move_to_element(elem)
elem.click()
options = driver.find_elements_by_class_name("item")
print(options[0].get_attribute("data-pid"))
# print(options)
time.sleep(1)
driver.quit()
# elem.send_keys(Keys.RETURN)
# f = open("new.html","w",encoding="utf-8")
# f.write(driver.page_source)
# f.close()
# print(driver.page_source)

# elem.click()

# assert "Python" in driver.title
# elem = driver.find_element_by_name('q')
# elem.send_keys("pycon")
# elem.send_keys(Keys.RETURN)
# print(driver.page_source)
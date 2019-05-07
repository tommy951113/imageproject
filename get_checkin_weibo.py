import requests
import time
import os
import codecs
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

# 119.14173,33.51234
SCROLL_PAUSE_TIME = 1.5
POI_ID = 'B2094650D46EABFE4493'
url = 'https://m.weibo.cn/p/100101' + POI_ID
driver = webdriver.Chrome()
driver.get(url)
try:
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME,"module-page-fragment"))
    )
    nav = driver.find_element_by_class_name('nav-item')
    elem = nav.find_element_by_xpath('//li[2]')
    elem.click()
    WebDriverWait(driver,10).until(
        EC.presence_of_element_located((By.CLASS_NAME,"weibo-text"))
    )
    # scroll to bottom of page
    last_height = driver.execute_script('return document.body.scrollHeight')
    while True:
        driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
        time.sleep(SCROLL_PAUSE_TIME)
        new_height = driver.execute_script('return document.body.scrollHeight')
        if new_height == last_height:
            break
        last_height = new_height

    elems = driver.find_elements_by_class_name('weibo-text')
    # print(len(elems))
    text_list = []
    for elem in elems:
        text = elem.find_element_by_xpath('.').text
        child_text = ''
        for elem in elem.find_elements_by_xpath('.//a'):
            text = text.replace(elem.text, '')
        text_list.append(text)
    with codecs.open(POI_ID + '.txt','w','utf-8') as f:
        for text in text_list:
            f.write(text + '\n')
finally:
    driver.quit()
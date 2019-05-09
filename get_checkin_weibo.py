import requests
import time
import os
import codecs
import re
import pandas
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

# 使用selenium方法爬取微博签到数据
# 119.14173,33.51234
SCROLL_PAUSE_TIME = 1.5
POI_ID = 'B2094650D46EABFF4999'
url = 'https://m.weibo.cn/p/100101' + POI_ID
driver = webdriver.Chrome()
driver.get(url)
try:
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "module-page-fragment"))
    )
    nav = driver.find_element_by_class_name('nav-item')
    elem = nav.find_element_by_xpath('//li[2]')
    elem.click()
    WebDriverWait(driver,10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "weibo-text"))
    )
    time.sleep(2)
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

        # 移除带链接的文字
        for item in elem.find_elements_by_xpath('.//a'):
            text = text.replace(item.text, '')
        if '分享图片' in text or '分享视频' in text:
            continue
        if text == '' or text.isspace():
            continue
        # 移除换行符和文字的表情符号
        text = text.replace('\n', ' ')
        text = re.sub(r'\[(.*?)\]', '', text)
        text_list.append(text)

    # print(text_list)
    with codecs.open(POI_ID + '.txt', 'w', 'utf-8') as f:
        for text in text_list:
            f.write(text + '\n')
finally:
    driver.quit()
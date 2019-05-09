import cv2
import numpy as np
from matplotlib import pyplot as plt
import os

def cal_tree_prop(img):
    img = cv2.imread(img)
    sump = 0
    for row in img:
        for col in row:
            if col[0] == 255 and col[2] == 11:
                sump += 1
    tree_prop = sump/(img.shape[0]*img.shape[1])            
    return tree_prop

dir =  'F:\\ImageProjects\\images\\ruijinlu'
folders = os.listdir(dir)

prop_list = []
for folder in folders:
    sump = 0
    prop_item = {}
    imgs = [f for f in os.listdir(dir + '\\' + folder) if f.endswith('seg.jpg')]
    for img in imgs:
        sump += cal_tree_prop(dir + '\\' + folder + '\\' + img)
    prop_item['id'] = folder
    prop_item['prop'] = sump
    prop_list.append(prop_item)

with open('prop_result','w') as f:
    for prop_item in prop_list:
        f.write(prop_item['id'])
        f.write(',')
        f.write(str(prop_item['prop']))
import cv2
import numpy as np

im = cv2.imread('streetview.jpg')
height,width,depth = im.shape
circle_img = np.zeros((height,width), np.uint8)
cv2.circle(circle_img,(int(width/2),int(height/2)),280,1,thickness=-1)
masked_data = cv2.bitwise_and(im,im,mask=circle_img)
# circle_img2 = np.zeros((int(height/2),int(width/2)), np.uint8)
# cv2.circle(circle_img2,(int(width/4),int(height/4)),140,1,thickness=-1)
# masked_data1 = cv2.bitwise_not(masked_data,masked_data,mask=circle_img2)
# cv2.imshow('masked',masked_data)
height2,width2,depth2 = masked_data.shape
circle_img2 = np.zeros((height2,width2), np.uint8)
cv2.circle(circle_img2,(int(width2 * 0.5),int(height2 * 0.5)),140,1,thickness=-1)
masked_data2 = cv2.bitwise_not(masked_data,masked_data,mask=circle_img2)
cv2.imshow('masked2',masked_data2)
cv2.waitKey(0)

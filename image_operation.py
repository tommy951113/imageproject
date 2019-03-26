import cv2
import numpy as np
from matplotlib import pyplot as plt
import pymeanshift as pms

def theta(xf, yf):
    if xf < cx:
        return np.pi/2 + np.arctan((yf-cy)/(xf-cx))
    else:
        return 3*np.pi/2 + np.arctan((yf-cy)/(xf-cx))

img1 = cv2.imread('streetview.jpg')
wc = img1.shape[1]
hc = img1.shape[0]
r0 = wc/(2*np.pi)
cx = cy = r0


img2 = np.empty([int(2*r0) + 1, int(2*r0) + 1, 3])
for xf in range(img2.shape[1]):
    for yf in range(img2.shape[0]):
        xc = theta(xf,yf)/(2*np.pi)*wc
        r = np.sqrt(np.power(xf - cx, 2) + np.power(yf - cy, 2))
        yc = r/r0 * hc
        if xc <= img1.shape[1] and yc <= img1.shape[0]:
            img2[yf][xf] = img1[int(yc)][int(xc)]
img2 = np.uint8(img2)
(segmented_image, labels_image, number_regions) = pms.segment(img2, spatial_radius=6, 
                                                              range_radius=4.5, min_density=50)
b,g,r = cv2.split(segmented_image)
brightness = (0.5*r+g+1.5*b)/3
brightness = np.uint8(brightness)
ret,th = cv2.threshold(brightness,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
h = brightness.shape[0]
w = brightness.shape[1]
for y in range(0, h):
        for x in range(0, w):
                brightness[y, x] = 255 if brightness[y, x] >= ret else 0

d0 = np.sqrt(np.power(cx,2) + np.power(cy,2))
n = 37
wr = r0/n

svf = 0
c = 1/(2*np.pi)*np.sin(np.pi/(2*n))      # constant in front of svf calculation equation
fn = 0

# image circle subset
circle_img = np.zeros((h,w),np.uint8)
cv2.circle(circle_img, (int(w/2),int(h/2)),int(r0 - 12*wr),1,thickness=-1)
masked_data = cv2.bitwise_and(brightness, brightness, mask=circle_img)
cv2.imshow('masked_data',masked_data)
# cv2.waitKey(0)
# def pt(i){
        
# }

# for i in range(n):

#         fn = fn + np.sin(np.pi*(2*i-1)/(2*n))*pt(i)

cv2.imshow('original iamge', img2)       
cv2.imshow('img2',segmented_image)
cv2.imshow('sky extraction: ', brightness)
# cv2.imshow('brightness',brightness)
cv2.waitKey(0)
cv2.destroyAllWindows()

import cv2
import numpy as np
from matplotlib import pyplot as plt
import pymeanshift as pms

def theta(xf, yf):
    if xf < cx:
        return np.pi/2 + np.arctan((yf-cy)/(xf-cx))
    else:
        return 3*np.pi/2 + np.arctan((yf-cy)/(xf-cx))

img1 = cv2.imread('streetview2.jpg')
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
        # if xc>yc:
        #     print(xc,yc,',')
cv2.imshow('original iamge', img2)       
cv2.imshow('img2',segmented_image)
# cv2.imshow('brightness',brightness)
cv2.waitKey(0)
cv2.destroyAllWindows()
# print(img2.dtype)
# plt.imshow('image2', img2)
# plt.show()
# print(img1)
# img2 = cv2.imread('streetview2.jpg')
# img2 = cv2.imread('opencv-logo-white.png')
# dst = cv2.addWeighted(img1,0.7,img2,0.3,0)
# rows,cols,channels = img2.shape
# roi = img1[0:rows,0:cols]

# img2gray = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
# ret, mask = cv2.threshold(img2gray,10,255,cv2.THRESH_BINARY)
# cv2.imshow('mask',mask)
# mask_inv = cv2.bitwise_not(mask)  # 反色
# cv2.imshow('mask_inv',mask_inv)
# img1_bg = cv2.bitwise_and(roi,roi,mask=mask_inv)
# cv2.imshow('img background', img1_bg)
# img2_fg = cv2.bitwise_and(img2,img2,mask=mask)
# cv2.imshow('img foreground', img2_fg)
# dst = cv2.add(img1_bg,img2_fg)
# cv2.imshow('dst dst',dst)
# img1[0:rows,0:cols] = dst
# cv2.imshow('res', img1)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
# dst = cv2.add(img1_bg,img2_fg)

# BLUE = [255,0,0]
# img = cv2.imread('roi.jpg')
# img = cv2.imread('messi5.jpg',0)
# ball = img[280:340,330:390]
# replicate = cv2.copyMakeBorder(img,40,10,10,70,cv2.BORDER_REPLICATE)
# reflect = cv2.copyMakeBorder(img,10,10,10,10,cv2.BORDER_REFLECT)
# constant= cv2.copyMakeBorder(img,10,10,10,10,cv2.BORDER_CONSTANT,value=BLUE)
# plt.subplot(231),plt.imshow(img,'gray'),plt.title('ORIGINAL')
# plt.subplot(232),plt.imshow(replicate,'gray'),plt.title('REPLICATE')
# plt.subplot(233),plt.imshow(reflect,'gray'),plt.title('REFLECT')
# plt.subplot(236),plt.imshow(constant,'gray'),plt.title('CONSTANT')
# plt.show()
# cv2.imshow('image',dst)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
# px = img[100,100]
# blue = img[100,100,0]
# print(blue)
# img[100,100] = [255,255,255]
# print(img[100,100])
# print(img.item(10,10,2))
# img.itemset((10,10,2),100)
# print(img.item(10,10,2))
# print(img.shape)
# print(img.size)
# print(img.dtype)
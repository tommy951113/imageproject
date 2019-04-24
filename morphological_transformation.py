import cv2
import numpy as np
from matplotlib import pyplot as plt

# Morphological Transformations
# Erosion, Dilation, Opening, Closing, Morphological Gradient
# Top Hat(image - opening), Black Hat(closing - image)
img = cv2.imread('images/brain.png')
kernel = np.ones((5,5), np.uint8)
# erosion = cv2.erode(img, kernel, iterations = 1)
# dilation = cv2.dilate(img,kernel,iterations = 1)
# opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
# closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)
# gradient = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)
# tophat = cv2.morphologyEx(img, cv2.MORPH_TOPHAT, kernel)
# blackhat = cv2.morphologyEx(img, cv2.MORPH_BLACKHAT, kernel)
print(cv2.getStructuringElement(cv2.MORPH_CROSS,(5,5)))

# plt.subplot(121),plt.imshow(img),plt.title('Original')
# plt.xticks([]), plt.yticks([])
# plt.subplot(122),plt.imshow(blackhat),plt.title('Blurred')
# plt.xticks([]), plt.yticks([])
# plt.show()
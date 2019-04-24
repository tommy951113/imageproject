import cv2
import numpy as np
from matplotlib import pyplot as plt

# IMAGE SMOOTHING INCLUDE 2D convolution, average filter,
# Gaussian Filtering, Median Filtering, Bilateral Filtering(双边滤波)
img = cv2.imread('images/streetview.jpg')

# 2D Convolution
# kernel = np.ones((5,5),np.float32)/25
# dst = cv2.filter2D(img,-1,kernel)

# Averaging
# blur = cv2.blur(img,(5,5))

# Gaussian Filtering
# blur = cv2.GaussianBlur(img,(5,5),0)

# Median Filtering
# median = cv2.medianBlur(img,5)

# Bilateral Filtering
# blur = cv2.bilateralFilter(img,9,75,75)

plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(blur),plt.title('Blurred')
plt.xticks([]), plt.yticks([])
plt.show()
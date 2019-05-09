import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('images\\10101130131020120928700\\10101130131020120928700_300.jpg')
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
h = hsv[:,:,0]
vegetation = np.full(h.shape, 255, dtype=np.uint8)
for (i,j), v in np.ndenumerate(h):
    if v > 75 and v < 170:
        vegetation[i][j] = 0

plt.subplot(121),plt.imshow(img[:,:,::-1]),plt.title('original'),plt.xticks([]),plt.yticks([])
plt.subplot(122),plt.imshow(vegetation),plt.title('vegetation'),plt.xticks([]),plt.yticks([])
plt.show()
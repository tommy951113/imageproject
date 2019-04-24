import cv2
import numpy as np
from matplotlib import pyplot as plt
import pymeanshift as pms

img1 = cv2.imread('images\\10101122121124141823300\\10101122121124141823300_240.jpg')[:,:,::-1]
wc = img1.shape[1]
hc = img1.shape[0]


img1 = np.uint8(img1)

# meanshift segment
(segmented_image, labels_image, number_regions) = pms.segment(
    img1, spatial_radius=6, range_radius=4.5, min_density=50)

b, g, r = cv2.split(segmented_image)
brightness = (0.5 * r + g + 1.5 * b) / 3
brightness = np.uint8(brightness)
ret, th = cv2.threshold(brightness, 0, 255,
                        cv2.THRESH_BINARY + cv2.THRESH_OTSU)
exg = 2 * g - b - r

for y in range(0, hc):
    for x in range(0, wc):
        if brightness[y, x] >= ret:
            brightness[y, x] = 255
        elif brightness[y, x] >= exg[y, x]:
            brightness[y, x] = 127
        else:
            brightness[y, x] = 0
plt.subplot(121),plt.imshow(img1)
plt.subplot(122),plt.imshow(brightness)
plt.show()

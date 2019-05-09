import cv2
import numpy as np
from matplotlib import pyplot as plt

# np.seterr(divide='ignore', invalid='ignore')

img = cv2.imread('images/streetview5.jpg')
b, g, r = cv2.split(img)

# img_new = np.empty(img.shape)
img_green = np.empty(b.shape)
r1 = g1 = b1 = np.empty(b.shape)
sum = r + g + b

for (i, j), value in np.ndenumerate(b):
    b1[i][j] = np.divide(b[i][j], sum[i][j])
    g1[i][j] = np.divide(g[i][j], sum[i][j])
    r1[i][j] = np.divide(r[i][j], sum[i][j])
print(b[0][0],g[0][0],r[0][0],sum[0][0])
print(b1[0][0],g1[0][0],r1[0][0])
img_new = cv2.merge((b1,g1,r1))

# for (i, j), value in np.ndenumerate(b):
#     s = img[i][j][0] + img[i][j][1] + img[i][j][2]
#     B, G, R = img[i][j][0]/s, img[i][j][1]/s, img[i][j][2]/s
#     img_new[i][j][0], img_new[i][j][1], img_new[i][j][2] = B, G, R

for (i, j), value in np.ndenumerate(b):
    green_index = 2.0 * img_new[i][j][1] - img_new[i][j][0] - img_new[i][j][2]
    print(green_index)
    if green_index > 0:
        img_green[i][j] = 255

plt.subplot(121), plt.imshow(img_new[:,:,::-1])
plt.subplot(122), plt.imshow(img_green)
plt.show()
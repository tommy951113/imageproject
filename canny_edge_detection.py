import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('01002500001405051327290575O.jpg',0)
edges = cv2.Canny(img,100,200)
plt.imshow(edges)
plt.show()

# wc = edges.shape[1]
# hc = edges.shape[0]

# for i in range(wc):
#     for j in range(hc):
#         if edges[j][i] > 0:
#             for x in range(j, hc-1):
#                 edges[x][i] = 255
#             break

# def theta(xf, yf):
#     if xf < cx:
#         return np.pi/2 + np.arctan((yf-cy)/(xf-cx))
#     else:
#         return 3*np.pi/2 + np.arctan((yf-cy)/(xf-cx))

# # img1 = cv2.imread('streetview.jpg')
# # wc = img1.shape[1]
# # hc = img1.shape[0]
# r0 = wc/(2*np.pi)
# cx = cy = r0

# img2 = np.empty([int(2*r0) + 1, int(2*r0) + 1])
# for xf in range(img2.shape[1]):
#     for yf in range(img2.shape[0]):
#         xc = theta(xf,yf)/(2*np.pi)*wc
#         r = np.sqrt(np.power(xf - cx, 2) + np.power(yf - cy, 2))
#         yc = r/r0 * hc
#         if xc <= edges.shape[1] and yc <= edges.shape[0]:
#             img2[yf][xf] = edges[int(yc)][int(xc)]

# img2 = np.uint8(img2)
# plt.subplot(121),plt.imshow(edges),plt.title('original')
# plt.subplot(122),plt.imshow(img2),plt.title('fisheye image')
# # plt.imshow(edges)
# plt.show()
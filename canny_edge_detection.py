import cv2
import numpy as np
from matplotlib import pyplot as plt

# img = cv2.imread('images/09000600121706201415155184A.jpg')[:,:,::-1]
# img2 = cv2.imread('images/09000600121706201415155184A.jpg', 0)
img3 = cv2.imread('images/09027900011607121435329675A.jpg')[:,:,::-1]
img4 = cv2.imread('images/09027900011607121435329675A.jpg',0)
# edges = cv2.Canny(img,100,200)
edges2 = cv2.Canny(img4,100,200)

# plt.subplot(2,3,1),plt.imshow(edges)
# plt.subplot(2,3,2),plt.imshow(img)
plt.subplot(2,3,4),plt.imshow(edges2)
plt.subplot(2,3,5),plt.imshow(img3)

# wc = edges.shape[1]
# hc = edges.shape[0]
wc2 = edges2.shape[1]
hc2 = edges2.shape[0]

# for i in range(wc):
#     for j in range(hc):
#         if edges[j][i] > 0:
#             for x in range(j, hc-1):
#                 edges[x][i] = 255
#             break
            
for i in range(wc2):
    for j in range(hc2):
        if edges2[j][i] > 0:
            for x in range(j, hc2-1):
                edges2[x][i] = 255
            break

# plt.subplot(2,3,3),plt.imshow(edges)
plt.subplot(2,3,6),plt.imshow(edges2)

plt.show()

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
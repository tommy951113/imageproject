import cv2
from matplotlib import pyplot as plt
import numpy as np


def fillEdges(width, height, edges):
    for i in range(width):
        for j in range(height):
            if edges[j][i] > 0:
                for x in range(j, height - 1):
                    edges[x][i] = 255
                break
    return edges

def theta(xf, yf):
    if xf < cx:
        return np.pi / 2 + np.arctan((yf - cy) / (xf - cx))
    else:
        return 3 * np.pi / 2 + np.arctan((yf - cy) / (xf - cx))

# def pt(i):
#     circle_img = np.zeros((h, w), np.uint8)
#     cv2.circle(circle_img, (int(h / 2), int(w / 2)), int(r0 - i * wr), 1, thickness=-1)
#     masked_data1 = cv2.bitwise_and(img3, img3, mask=circle_img)
#     circle_img2 = np.zeros((h, w), np.uint8)
#     cv2.circle(circle_img2, (int(h / 2), int(w / 2)), int(r0 - (i - 1) * wr), 1, thickness=-1)
#     masked_data2 = cv2.bitwise_and(img3, img3, mask=circle_img2)
#     masked_data = cv2.bitwise_not(masked_data1, masked_data1, mask=masked_data2)
#     unique, count = np.unique(masked_data, return_counts=True)
#     t = np.pi * np.power(int(r0 - (i - 1) * wr), 2) - np.pi * np.power(int(r0 - i * wr), 2)
#     return count[0] / int(t) if len(count) > 1 else 0

img_name = "images/09027900011607121435329675A.jpg"
img = cv2.imread(img_name)
wc = img.shape[1]
hc = img.shape[0]
r0 = wc / (2 * np.pi)
cx = cy = r0

img2 = img[:, :, 0]
edges = cv2.Canny(img, 100, 200)
pic = fillEdges(edges.shape[1], edges.shape[0], edges)
non_sky = np.argwhere(pic)

Z = img.reshape((-1, 3))
Z = np.float32(Z)
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
K = 12
ret, label, center = cv2.kmeans(Z, K, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)

center = np.uint8(center)
res = center[label.flatten()]
res2 = res.reshape((img.shape))

result_list = []
k = -1
for center_item in center:
    k = k + 1
    i = -1
    num1 = num2 = 0
    for row in res2:
        i = i + 1
        j = -1
        for col in row:
            j = j + 1
            if center_item[0] == col[0] and center_item[1] == col[1] and center_item[2] == col[2]:
                num2 = num2 + 1
                if pic[i][j] == 0:
                    num1 = num1 + 1
    result_list.append(num1 / num2)

effective_center_list = []
for i, item in enumerate(result_list):
    if item >= 0.3:
        effective_center_list.append(i)

for k in effective_center_list:
    i = -1
    for row in res2:
        i += 1
        j = -1
        for col in row:
            j += 1
            if pic[i][j] != 0 and col[0] == center[k][0] and col[1] == center[k][1] and col[2] == center[k][2]:
                pic[i][j] = 0
# filter noise
    kernel = np.ones((3,3),np.uint8)
    pic = cv2.morphologyEx(pic, cv2.MORPH_CLOSE, kernel)

# project to fisheyeimage
img3 = np.empty([int(2 * r0) + 1, int(2 * r0) + 1])
h = w = img3.shape[0]
for xf in range(img3.shape[1]):
    for yf in range(img3.shape[0]):
        xc = theta(xf, yf) / (2 * np.pi) * wc
        r = np.sqrt(np.power(xf - cx, 2) + np.power(yf - cy, 2))
        yc = r / r0 * hc
        if xc <= pic.shape[1] and yc <= pic.shape[0]:
            img3[yf][xf] = pic[int(yc)][int(xc)]

# cal sky view factor
# n = 37
# wr = r0 / n
# svf = 0
# c = 1 / (2 * np.pi) * np.sin(np.pi / (2 * n))  # constant in front of svf calculation equation
# fn = 0
# for i in range(1, n):
#     fn = fn + np.sin(np.pi * (2 * i - 1) / (2 * n)) * pt(i)
# svf = np.pi / (2 * n) * fn

# cal sky openess index
non_sky = np.count_nonzero(img3)
soi = (np.pi * np.power(h / 2, 2) - non_sky)/(np.pi * np.power(h / 2, 2))
soi = round(soi*100, 2)

img3 = np.uint8(img3)
plt.subplot(131), plt.imshow(img), plt.title('original image')
plt.subplot(132), plt.imshow(pic), plt.title('filled image')
plt.subplot(133), plt.imshow(img3), plt.title('fisheye image'), plt.title('soi=' + str(soi) + '%')
plt.show()
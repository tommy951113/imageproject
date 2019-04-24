import cv2
from matplotlib import pyplot as plt
import numpy as np
import os

def extract_sky(img_name):
    def fillEdges(width, height, edges):
        for i in range(width):
            for j in range(height):
                if edges[j][i] > 0:
                    for x in range(j, height - 1):
                        edges[x][i] = 255
                    break
        return edges

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

    kernel = np.ones((3,3),np.uint8)
    closing = cv2.morphologyEx(pic, cv2.MORPH_CLOSE, kernel)
    no_sky = np.count_nonzero(closing)
    soi = (wc * hc - no_sky) / (wc * hc)
    return img, closing, soi

os.chdir('images')
# dirs = next(os.walk('.'))[1]
dirs = ['10101030131222131353400']

for (i,directory) in enumerate(dirs):
    image_list = os.listdir(directory)
    soi = 0
    for (j,img) in enumerate(image_list):
        image, extract_img, soi = extract_sky(os.path.join(directory, img))
        soi += soi
        print("proccessing")
        plt.subplot(len(dirs) * 2, 6, 2 * i * 6 + j + 1), plt.imshow(extract_img)
        plt.subplot(len(dirs) * 2, 6, (2 * i + 1) * 6 + j + 1), plt.imshow(image[:,:,::-1])
    plt.title('soi=' + str(soi))
    # print("greeny = " + str(greeny))

# plt.subplot(131),plt.imshow(diff2)
# plt.subplot(132), plt.imshow()
# plt.subplot(133), plt.imshow()
plt.show()
# plt.subplot(131), plt.imshow(img[:,:,::-1]), plt.title('original image')
# plt.subplot(132), plt.imshow(pic), plt.title('filled image')
# plt.subplot(133), plt.imshow(closing), plt.title('closing image'),plt.title('SOI= '+ str(soi))
# plt.subplot(133), plt.imshow(img3), plt.title('fisheye image'), plt.title('svf=' + str(svf))
plt.show()
import cv2
import os
import numpy as np
import pymeanshift as pms
from matplotlib import pyplot as plt

# vegetation image
def extract_green(image):
    '''Return extracted image'''
    img = cv2.imread(image)
    (segmented_image, labels_image, number_regions) = pms.segment(
        img, spatial_radius=6, range_radius=4.5, min_density=50)
    b, g, r = cv2.split(segmented_image / 255)
    diff1 = g - r
    diff2 = g - b
    diff_image = diff1 * diff2
    vegetation = np.empty_like(diff_image)
    for (i, j), value in np.ndenumerate(diff_image):
        if diff_image[i][j] > 0 and diff1[i][j] > 0 and b[i][j] <= 0.7 and g[i][j] <= 0.7 and r[i][j] <= 0.7:
            vegetation[i][j] = 255
    # filtering noise
    kernel = np.ones((3,3),np.uint8)
    vegetation = cv2.morphologyEx(np.uint8(vegetation), cv2.MORPH_OPEN, kernel)
    return img, vegetation


os.chdir('images')
# dirs = next(os.walk('.'))[1]
dirs = ['10101030131222131353400']

for (i,dir) in enumerate(dirs):
    image_list = os.listdir(dir)
    greeny = 0
    for (j,img) in enumerate(image_list):
        image, veg = extract_green(os.path.join(dir, img))
        greeny += np.count_nonzero(veg) / (960 * 640)
        print("proccessing")
        plt.subplot(len(dirs) * 2, 6, 2 * i * 6 + j + 1), plt.imshow(veg)
        plt.subplot(len(dirs) * 2, 6, (2 * i + 1) * 6 + j + 1), plt.imshow(image[:,:,::-1])
    plt.title('greeny=' + str(greeny))
    # print("greeny = " + str(greeny))

# plt.subplot(131),plt.imshow(diff2)
# plt.subplot(132), plt.imshow()
# plt.subplot(133), plt.imshow()
plt.show()
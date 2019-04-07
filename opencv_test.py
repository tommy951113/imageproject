import cv2
from matplotlib import pyplot as plt
import numpy as np

def fillEdges(width, height, edges):
    for i in range(width):
        for j in range(height):
            if edges[j][i] > 0:
                for x in range(j, height-1):
                    edges[x][i] = 255
                break
    return edges

def showPic(img):
    plt.imshow(img)
    plt.show()

img_name = "images/streetview.jpg"
img = cv2.imread(img_name)

img2 = img[:,:,0]
edges = cv2.Canny(img,100,200)
pic = fillEdges(edges.shape[1], edges.shape[0], edges)
non_sky = np.argwhere(pic)
plt.subplot(1,3,1),plt.imshow(pic),plt.title('original image')

Z = img.reshape((-1,3))
Z = np.float32(Z)
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
K = 12
ret,label,center=cv2.kmeans(Z,K,None,criteria,10,cv2.KMEANS_RANDOM_CENTERS)

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
            if center_item[0]==col[0] and center_item[1]==col[1] and center_item[2]==col[2]:
                num2 = num2 + 1
                if pic[i][j] == 0:
                    num1 = num1 + 1
    result_list.append(num1 / num2)
# print(result_list)
effective_center_list = []
for i,item in enumerate(result_list):
    if item>=0.3:
        effective_center_list.append(i)
# print(effective_center_list)

for k in effective_center_list:
    i = -1
    for row in res2:
        i+=1
        j=-1
        for col in row:
            j+=1
            if pic[i][j] != 0 and col[0]==center[k][0] and col[1]==center[k][1] and col[2]==center[k][2]:
                pic[i][j] = 0

plt.subplot(1,3,2),plt.imshow(pic),plt.title('after clustering')
plt.subplot(1,3,3),plt.imshow(img),plt.title('original image')
plt.show()
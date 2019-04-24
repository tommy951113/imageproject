import numpy as np
import cv2
import matplotlib.pyplot as plt

# 
# geometric transformation include Scaling Translation 
# Affine Transformation(仿射变换) Perspective Transformation(透视变换)
# 

img = cv2.imread('images/streetview.jpg', 0)
rows,cols = img.shape

# scaling
# res = cv2.resize(img,None,fx=0.5, fy=3, interpolation = cv2.INTER_CUBIC)

# translation
# M = np.float32([[1,0,100],[0,1,50]])
# dst = cv2.warpAffine(img,M,(cols,rows))

# rotate
M = cv2.getRotationMatrix2D((cols/2,rows/2),60,1)
dst = cv2.warpAffine(img,M,(cols,rows))

cv2.imshow('image',dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
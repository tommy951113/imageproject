import cv2
from matplotlib import pyplot as plt
import numpy as np

arr = np.array([[1,2],[2,2],[3,6]])
arr2 = np.array([[0,0],[0,0],[1,1]])

for i,row in np.ndenumerate(arr2):
    for j,col in np.ndenumerate(row):
        if col == arr[i][j]:
            print(col) 
            
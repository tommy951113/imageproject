import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('images/streetview.jpg')
lower_reso = cv2.pyrDown(higher_reso)

import cv2  
import numpy as np  
import matplotlib.pyplot as plt

#读取原始图像
img = cv2.imread('lena-small.png')

#图像向上取样
r = cv2.pyrUp(img)
print(r)
print(r.shape)

#显示图像
cv2.imshow('original', img)
cv2.imshow('PyrUp', r)
cv2.waitKey()
cv2.destroyAllWindows()

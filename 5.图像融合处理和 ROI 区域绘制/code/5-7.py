import cv2
import numpy as np
import matplotlib.pyplot as plt

# 读取图片
src = cv2.imread('luo.png')
# 图像类型转换
result = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
grayImage = cv2.cvtColor(src, cv2.COLOR_BGR2HSV)
# 显示图像
cv2.imshow("src", src)
cv2.imshow("result", result)
cv2.imshow("grayImage", grayImage)
# 等待显示
cv2.waitKey(0)
cv2.destroyAllWindows()

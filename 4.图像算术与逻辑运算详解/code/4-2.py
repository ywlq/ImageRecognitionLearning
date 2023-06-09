import cv2
import numpy as np

# 读取图片
img = cv2.imread("luo.png")
# 图像各像素减 50
m = np.ones(img.shape, dtype="uint8") * 20
# OpenCV 减法运算
result = cv2.subtract(img, m)
# 显示图像
cv2.imshow("original", img)
cv2.imshow("result", result)
# 等待显示
cv2.waitKey(0)
cv2.destroyAllWindows()

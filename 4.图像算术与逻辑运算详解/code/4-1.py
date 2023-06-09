import cv2
import numpy as np

# 读取图片
img = cv2.imread("luo.png")

# 图像各像素加 100
m = np.ones(img.shape, dtype="uint8") * 200

# OpenCV 加法运算
result = cv2.add(img, m)

# 显示图像
cv2.imshow("original", img)
cv2.imshow("result", result)
# 等待显示
cv2.waitKey(0)
cv2.destroyAllWindows()

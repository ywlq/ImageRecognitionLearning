import cv2
import numpy

# 读取图片
img = cv2.imread("luo.png")
# 获取图像形状
print(img.shape)
print(img.size)
print(img.dtype)
# 显示图像
cv2.imshow("Demo", img)
# 等待显示
cv2.waitKey(0)
cv2.destroyAllWindows()

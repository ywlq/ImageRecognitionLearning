import cv2
import numpy

# 读取图片
img = cv2.imread("luo.png")
print(img.shape)
# 拆分通道
b, g, r = cv2.split(img)
#合并通道
m = cv2.merge([b, g, r])
cv2.imshow("Merge", m)
# 显示原始图像
cv2.imshow("B", b)
cv2.imshow("G", g)
cv2.imshow("R", r)
print(b.shape)
# 等待显示
cv2.waitKey(0)
cv2.destroyAllWindows()

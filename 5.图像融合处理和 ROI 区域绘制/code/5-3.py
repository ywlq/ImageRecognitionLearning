import cv2
import numpy as np

#读取图片
img = cv2.imread("Lena.png")
test = cv2.imread("luo.png",)
#定义 150×150 矩阵 3 对应 BGR
face = np.ones((150, 150, 3))
#显示原始图像
cv2.imshow("Demo", img)
#显示 ROI 区域
face = img[200:350, 200:350]
test[250:400, 250:400] = face
cv2.imshow("Result", test)
#等待显示
cv2.waitKey(0)
cv2.destroyAllWindows()
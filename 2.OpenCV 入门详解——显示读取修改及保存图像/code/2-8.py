import cv2
import numpy as np
#读取图片
img = cv2.imread("Lena.png")
#创建空图像
emptyImage = np.zeros(img.shape, np.uint8)

#变成白色
for row in range(img.shape[0]):
    for column in range(img.shape[1]):
        for BGR in range(img.shape[2]):
            emptyImage.itemset((row,column,BGR),255)

#显示图像
cv2.imshow("Demo", emptyImage)
#等待显示
cv2.waitKey(0)
cv2.destroyAllWindows()
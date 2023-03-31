import cv2
#读取图片
img = cv2.imread("Lena.png")
#读取像素
test = img[200,142]
print("读取的像素值:", test)
#修改像素
img[200,142] = [0, 0, 0]
print("修改后的像素值:", test)
#分别获取 BGR 通道像素
blue = img[200,142,0]
print("蓝色分量", blue)
green = img[200,142,1]
print("绿色分量", green)
red = img[200,142,2]
print("红色分量", red)
#显示图像
cv2.imshow("Demo", img)
#等待显示
cv2.waitKey(0)
cv2.destroyAllWindows()
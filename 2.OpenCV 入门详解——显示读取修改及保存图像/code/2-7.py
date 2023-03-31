import cv2

#读取图片
img = cv2.imread("Lena.png")
print(img.shape)
print(img[78][100])


#Numpy 读取像素
print(img.item(78, 100, 0))
print(img.item(78, 100, 1))
print(img.item(78, 100, 2))
#Numpy 修改像素
img.itemset((78, 100, 0), 100)
img.itemset((78, 100, 1), 100)
img.itemset((78, 100, 2), 100)
print(img.item(78, 100, 0))
print(img.item(78, 100, 1))
print(img.item(78, 100, 2))
cv2.imshow("demo",img)


for i in range(413):
    for j in range(300):
        for k in range(3):
            img.itemset((i,j,k),255)

cv2.imshow("demo",img)

cv2.waitKey(0)
cv2.destroyAllWindows()
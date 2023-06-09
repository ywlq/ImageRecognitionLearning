import cv2
import matplotlib.pyplot as plt

# 读取图像
img1 = cv2.imread('lena.png')
img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)

img2 = cv2.imread('xluo.png')
img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)

img3 = cv2.imread('flower.png')
img3 = cv2.cvtColor(img3, cv2.COLOR_BGR2RGB)

img4 = cv2.imread('huawei.png')
img4 = cv2.cvtColor(img4, cv2.COLOR_BGR2RGB)

# 显示四张图像
titles = ['lena', 'people', 'flower', 'huawei']
images = [img1, img2, img3, img4]
for i in range(4):
    plt.subplot(2, 2, i + 1), plt.imshow(images[i])
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])
plt.show()

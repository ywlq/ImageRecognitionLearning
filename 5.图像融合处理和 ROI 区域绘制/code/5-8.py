import cv2
import matplotlib.pyplot as plt

# 读取原始图像

img_BGR = cv2.imread('luo.png')
# BGR 转换为 RGB
img_RGB = cv2.cvtColor(img_BGR, cv2.COLOR_BGR2RGB)
# 灰度化处理
img_GRAY = cv2.cvtColor(img_BGR, cv2.COLOR_BGR2GRAY)
# BGR 转 HSV
img_HSV = cv2.cvtColor(img_BGR, cv2.COLOR_BGR2HSV)
# BGR 转 YCrCb
img_YCrCb = cv2.cvtColor(img_BGR, cv2.COLOR_BGR2YCrCb)
# BGR 转 HLS
img_HLS = cv2.cvtColor(img_BGR, cv2.COLOR_BGR2HLS)
# BGR 转 XYZ
img_XYZ = cv2.cvtColor(img_BGR, cv2.COLOR_BGR2XYZ)
# BGR 转 LAB
img_LAB = cv2.cvtColor(img_BGR, cv2.COLOR_BGR2LAB)
# BGR 转 YUV
img_YUV = cv2.cvtColor(img_BGR, cv2.COLOR_BGR2YUV)
# 调用 matplotlib 显示处理结果
titles = ['BGR', 'RGB', 'GRAY', 'HSV', 'YCrCb', 'HLS', 'XYZ', 'LAB', 'YUV']
images = [img_BGR, img_RGB, img_GRAY, img_HSV, img_YCrCb,
          img_HLS, img_XYZ, img_LAB, img_YUV]
for i in range(9):
    plt.subplot(3, 3, i + 1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])
plt.show()

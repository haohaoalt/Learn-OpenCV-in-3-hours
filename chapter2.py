import cv2
import numpy as np

img = cv2.imread("Resources/lena.png")
kernel = np.ones((5,5),np.uint8)
# 灰度图像
imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# 高斯模糊  参数：图像，模糊半径（高斯核），模糊类型
imgBlur = cv2.GaussianBlur(imgGray,(7,7),0)
# 边缘检测
imgCanny = cv2.Canny(img,150,200)
# 膨胀操作
imgDialation = cv2.dilate(imgCanny,kernel,iterations=1)
# 腐蚀操作
imgEroded = cv2.erode(imgDialation,kernel,iterations=1)

cv2.imshow("Gray Image",imgGray)
cv2.imshow("Blur Image",imgBlur)
cv2.imshow("Canny Image",imgCanny)
cv2.imshow("Dialation Image",imgDialation)
cv2.imshow("Eroded Image",imgEroded)
cv2.waitKey(0)
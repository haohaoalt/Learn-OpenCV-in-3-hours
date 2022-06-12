import cv2
import numpy as np

img = cv2.imread("Resources/lambo.PNG")
print(img.shape)

imgResize = cv2.resize(img,(1000,500))
print(imgResize.shape)
# 裁剪
imgCropped = img[0:200,200:495]

cv2.imshow("Image",img)
cv2.imshow("Image Resize",imgResize)
cv2.imshow("Image Cropped",imgCropped)

cv2.waitKey(0)
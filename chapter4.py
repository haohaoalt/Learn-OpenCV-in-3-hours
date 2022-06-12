import cv2
import numpy as np

img = np.zeros((512,512,3),np.uint8)
#print(img)
#img[:]= 255,0,0

cv2.line(img,(0,0),(img.shape[1],img.shape[0]),(0,255,0),3)
#最后一个参数是线宽，想要填充整个矩形，就用 cv2.FILLED
cv2.rectangle(img,(0,0),(250,350),(0,0,255),2)
# 参数：img，圆心，半径，颜色，线宽
cv2.circle(img,(400,50),30,(255,255,0),5)
# 参数： img，文本，左上角坐标，字体，字体大小，颜色，线宽
cv2.putText(img," OPENCV  ",(300,200),cv2.FONT_HERSHEY_COMPLEX,1,(0,150,0),3)


cv2.imshow("Image",img)

cv2.waitKey(0)
######################## READ IMAGE ############################
# import cv2
# # LOAD AN IMAGE USING 'IMREAD'
# img = cv2.imread("Resources/lena.png")
# # DISPLAY
# cv2.imshow("Lena Soderberg",img)
# cv2.waitKey(0)



######################### READ VIDEO #############################
# import cv2
# cap = cv2.VideoCapture('Resources/test_video.mp4')
# # 第3个参数是视频长度
# cap.set(3,640)
# # 第4个参数是视频宽度
# cap.set(4,480)
# while True:
#     success, img = cap.read()
#     cv2.imshow("Result", img)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break


######################### READ WEBCAM  ############################
import cv2
frameWidth = 640
frameHeight = 480
cap = cv2.VideoCapture(0)
cap.set(3, frameWidth)
cap.set(4, frameHeight)
cap.set(10,150)
while True:
    success, img = cap.read()
    cv2.imshow("Result", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

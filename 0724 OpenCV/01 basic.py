import cv2
import numpy as np

img= cv2.imread("lenna.bmp")
kernel= np.ones((10,10),np.uint8)     #np.ones 모든 배열에 '1'삽입 (n,n)했을때 선이 바뀐다는거

imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray,(7,7),(0))
imgCanny= cv2.Canny(img,150,200)     #edge추출
imgDialation = cv2.dilate(imgCanny,kernel,iterations=1)     #edge굵기변경:얇게
imgEroded= cv2.erode(imgDialation, kernel, iterations=1)     #edge굵기변경:굵게

cv2.imshow("Gray Image",imgGray)
cv2.imshow("Blur Image",imgBlur)
cv2.imshow("Canny Image",imgCanny)
cv2.imshow("Dialation Image",imgDialation)
cv2.imshow("Erode Image",imgEroded)
cv2.waitKey(0)
import cv2
import numpy as np
#fill the matrix with 0=black;gray scale
img=np.zeros((512,512,3),np.uint8) #unit8=+~255,8bit
#print(img)
#img[:]=255,0,0 #set colors for the whold image by blue
#img[200:300,100:300]=255,0,0 #set colors for a certain are by blue

cv2.line(img,(0,0),(img.shape[1],img.shape[0]),(0,255,0),3) #선,width, height: 이 순서가 바뀔때가있음
cv2.rectangle(img,(0,0),(250,350),(0,0,255),2)#사각형;2->FILLED
cv2.circle(img,(400,50),10,(255,255,0),5)#원
#텍스트
cv2.putText(img,"linelineline",(300,200),cv2.FONT_HERSHEY_COMPLEX,1,(0,150,0),3)

cv2.imshow("Image",img)
cv2.waitKey(0)
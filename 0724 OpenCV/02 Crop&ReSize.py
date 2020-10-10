import cv2
import numpy as np

img= cv2.imread("lenna.bmp")
print(img.shape)    #height, width, channel
imgResize = cv2.resize(img,(1000,500))
print(imgResize.shape)  #starting, ending point
imgCropped = img[0:200,200:500]

cv2.imshow("Image",img)
cv2.imshow("Image Resize",imgResize)
cv2.imshow("Image Cropped",imgCropped)

cv2.waitKey(0)

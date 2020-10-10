import cv2

faceCascade= cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
video_capture= cv2.VideoCapture(0)

while True:
    #capture frame-by-frame
    ret, frame= video_capture.read()
    imgGray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces= faceCascade.detectMultiScale(imgGray,1.1,4)

    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
    #DISPLAY the resulting frame
    cv2.imshow("Video",frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

#when everything is done, release the capture
video_capture.release()
cv2.destroyAllWindows()

import cv2
import numpy as np
cap = cv2.VideoCapture(0)
while True:
    r,frame=cap.read()
    frame = cv2.GaussianBlur(frame,(11,11),0)
    
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    hsv = cv2.morphologyEx(hsv, cv2.MORPH_CLOSE, (5,5))
    lower_blue=np.array([145,0,0])
    upper_blue=np.array([170,20,255])

    mask = cv2.inRange(hsv,lower_blue,upper_blue)
    
    res = cv2.bitwise_and(frame,frame,mask=mask)

    cv2.imshow('frame',frame)
    cv2.imshow('mask',mask)
    cv2.imshow('res',res)
    if cv2.waitKey(1) & 0xFF == ord('q') :
        break
cv2.destroyAllWindows()
cap.release()

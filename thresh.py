import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
 a , rw = cap.read()
 hsv = cv2.cvtColor(rw, cv2.COLOR_BGR2HSV)
 lower_white = np.array ( [10 ,150 ,150] )
 upper_white = np.array ( [180 ,255 ,250] )
                                  #120 255 250
 mask = cv2.inRange(hsv,lower_white,upper_white)
 res = cv2.bitwise_and( rw, rw, mask = mask)
 



 
 cv2.imshow('raw',rw)
 cv2.imshow('mask',mask)
 cv2.imshow('res',res)
 k = cv2.waitKey(5) & 0xFF
 if k == 27 : 
  break
cv2.destroyAllWindows()
cap.release()


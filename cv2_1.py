import cv2
import numpy as np
#cap = cv2.VideoCapture(0)
while True:
    #ret,frame = cap.read()
   # print ret
    frame= cv2.imread('images.jpg')
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    r,thresh = cv2.threshold(gray,127,255,cv2.THRESH_BINARY)
  #  thresh=gray
    image, contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    frame = cv2.drawContours(frame, contours, -1, (0,255,0), 3)
    cv2.imshow('thresh',thresh)
    print cv2.RETR_TREE
    #cv2.imshow('abcd',contours)
    cv2.imshow('frame',image)
    cv2.imshow('gray',gray)
    cv2.waitKey(0)
    #if cv2.waitKey(1) & 0xFF == ord('q') :
    break
    
#cap.release()
cv2.destroyAllWindows()

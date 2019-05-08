import cv2
import numpy as np
frame= cv2.imread("circles.jpg")
     

hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
kernel = np.ones((3,3),np.uint8)


# define range of skin color in HSV
lower_skin = np.array([0,0,0], dtype=np.uint8)
upper_skin = np.array([255,255,40], dtype=np.uint8)


mask = cv2.inRange(hsv, lower_skin, upper_skin)

mask = cv2.dilate(mask,kernel,iterations = 4)

mask = cv2.GaussianBlur(mask,(5,5),100) 

#find contours
_,contours,hierarchy= cv2.findContours(mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
im = cv2.drawContours(frame, contours, -1,(0,255,0), 2)
i=1

for cnt in contours:
        if(i!=1):
            perimeter= cv2.arcLength(cnt,True)
            print perimeter
        
            approx = cv2.approxPolyDP(cnt,0.15*cv2.arcLength(cnt,True),True)
            print len(approx)
            #send_command_x(len(approx))
        i+=1

cv2.imshow('Contour',im)
cv2.imshow('Mask',mask)
cv2.waitKey(0)
cv2.destroyAllWindows()

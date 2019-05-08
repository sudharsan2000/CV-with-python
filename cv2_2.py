import cv2
import numpy

img = cv2.imread('C:\Users\SUDHARSAN S\Downloads\light.jpg',cv2.IMREAD_COLOR)
tem= cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.line(img,(0,0),(200,200), (250,0,0), 4)
cv2.rectangle(img, (50,50), (100,100), (0,250,0),-1)
cv2.circle(img,(200,200),20,(0,0,250),5)
cv2.imshow('image',img)
cv2.imshow('temp',tem)
cv2.waitKey(0)
cv2.destroyAllWindows()

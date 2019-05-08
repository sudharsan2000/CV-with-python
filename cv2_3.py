import cv2
import numpy as np

img = cv2.imread('pic.jpg',cv2.IMREAD_COLOR)

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret,inv = cv2.threshold(img , 220 , 250 , cv2.THRESH_BINARY_INV)

cv2.imshow('inv',inv)
cv2.imshow('gray',gray)
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

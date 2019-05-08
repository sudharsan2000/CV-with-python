import cv2
import numpy as np
im=cv2.imread('images.jpg')

imgray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
ret,thresh = cv2.threshold(imgray,127,255,0)
image, contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
im = cv2.drawContours(im, contours, -1,(0,255,0), 3)
cv2.imshow('new',im)
cv2.waitKey(0)

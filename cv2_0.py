import cv2
cap = cv2.VideoCapture(0)
while(1):
    _,img = cap.read()
    cv2.imshow('i',img)
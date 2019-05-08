import cv2
import numpy as np 
cam = cv2.VideoCapture(0)
while True:
	ret, frame = cam.read()
	hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
	lower_blue = np.array([100,60,50])
	upper_blue = np.array([130,255,255])

	#Creating a mask where the values in the range are made 255 others are made 0
	mask = cv2.inRange(hsv , lower_blue, upper_blue)
	res = cv2.bitwise_and(frame, frame,mask = mask)
	cv2.imshow('Frame',frame)
	cv2.imshow('Smooth', mask)
	cv2.imshow('Filter', res)
	if cv2.waitKey(1) & 0xFF == 27:
		break
cam.release()
cv2.destroyAllWindows()

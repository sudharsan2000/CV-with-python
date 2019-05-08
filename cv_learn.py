import cv2
import numpy as np
cap = cv2.VideoCapture(0)
while(1):
    r,img = cap.read()
    #print img.itemset((10,10,2),100)
    cv2.imshow('img',img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cv2.destroyAllWindows()
cap.release()

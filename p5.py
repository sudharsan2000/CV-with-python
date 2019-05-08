import cv2
import numpy as np
import urllib3
def send_command_x(n):
    r=urllib3.urlopen("http://192.168.43.52/x_" + str(n) )
def send_command_y(n):
    r=urllib3.urlopen("http://192.168.43.52/y_" + str(n) )
cap=cv2.VideoCapture(0)
while True:
    while True:
        r,im = cap.read()
        blurred = cv2.GaussianBlur(im, (3, 3), 0)
        imgray = cv2.cvtColor(blurred,cv2.COLOR_BGR2GRAY)
        
        ret,thresh = cv2.threshold(imgray,50,255,1)
        kernel = np.ones((1,1),np.uint8)
        thresh = cv2.dilate(thresh,kernel,iterations = 1)
        cv2.imshow('t',thresh)
        
        contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
        im = cv2.drawContours(im, contours, -1,(0,125,100), 2)
        cv2.imshow('Contours',im)
        i=1
        flag=0
        if cv2.waitKey(1) & 0xFF == ord('q') :
            flag+=1
            break
        elif cv2.waitKey(1) & 0xFF == ord('s') :
            break
    if(flag!=0):
        break
    area = []
    approx=[]
    for cnt in contours:
        area.append(cv2.contourArea(cnt))
        approx.append(cv2.approxPolyDP(cnt,0.01*cv2.arcLength(cnt,True),True))
        
        
    y= (len(approx[area.index(min(area))]))/2 -3
    x = len( approx[area.index(max(area))] ) -3
    print (x,y)
    send_command_x(x)
    send_command_y(y)
cap.release()
cv2.destroyAllWindows()

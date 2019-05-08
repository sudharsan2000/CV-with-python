import cv2

cap = cv2.VideoCapture(0)

while (1):
    _,frame = cap.read()

    lap = cv2.Laplacian(frame,cv2.CV_64F)
    sobelx = cv2.Sobel( frame,cv2.CV_64F, 0, 1, ksize = 5)
    sobely = cv2.Sobel( frame,cv2.CV_64F, 1, 0, ksize = 5)
    edges = cv2.Canny(frame,80,80)

    cv2.imshow('frame',frame)
    cv2.imshow('Laplacian',lap)
    cv2.imshow('sobelx',sobelx)
    cv2.imshow('sobely',sobely)
    cv2.imshow('edges',edges)
    k= cv2.waitKey(5) & 0xFF
    if (k == 27):
        break
cv2.destroyAllWindows()
cap.release()

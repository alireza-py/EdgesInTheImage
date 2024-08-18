import cv2
import numpy

cam = cv2.VideoCapture(0)

while True:
    _,frame = cam.read()

    laplacian = cv2.Laplacian(frame, cv2.CV_8U)
    sobelx = cv2.Sobel(frame, cv2.CV_8U, 1, 0, ksize= 5)
    sobely = cv2.Sobel(frame, cv2.CV_8U, 0, 1, ksize= 5)
    canny = cv2.Canny(frame, 150, 300)

    cv2.imshow('laplacian', laplacian)
    cv2.imshow('frame', frame)
    cv2.imshow('sobelx', sobelx)
    cv2.imshow('sobely', sobely)
    cv2.imshow('canny', canny)

    if cv2.waitKey(1) == ord('a'): break

cv2.destroyAllWindows()
cam.release()
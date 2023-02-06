import cv2 as cv
img_og=cv.imread('rav.jpg')
img= cv.resize(img_og, (800,400))
cv.imshow('BRG img',img)

hsv= cv.cvtColor(img, cv.COLOR_BGR2HSV)  #convers color spaces
Lab= cv.cvtColor(img, cv.COLOR_BGR2LAB)
bgr= cv.cvtColor(hsv, cv.COLOR_HSV2BGR)
import cv2 as cv
import numpy as np

img_og= cv.imread('rav.jpg')
img= cv.resize(img_og,(800,400), interpolation=cv.INTER_AREA)
cv.imshow('cat',img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)    #converted to grey scale
cv.imshow('cat_grey',gray)

edge = cv.Canny(img, 125,175)                   #edge detection
cv.imshow('canny edges',edge)

blank = np.zeros(img.shape, dtype='uint8')   #making a blank image

contours, hierarchies = cv.findContours(edge, cv.RETR_LIST, cv.CHAIN_APPROX_NONE) 

cv.drawContours(blank, contours, -1, (255,255,255), 1)  #no.of.contours we want, color, thickness
cv.imshow('contours',blank)

cv.waitKey(0)
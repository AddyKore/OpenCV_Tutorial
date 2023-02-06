#here we will see various bluring n smoothing techniques

import cv2 as cv

img_og = cv.imread('rav.jpg')
img= cv.resize(img_og, (800,400))

#Averaging - in this bluring method, the system adjusts the pixel intensity depending on average of the surrounding pixel intensity
average = cv.blur(img, (7,7))
cv.imshow('Average Blur', average)

#gaussian blur
Gaussian = cv.GaussianBlur(img, (7,7), 0)
cv.imshow('Gaussian', Gaussian)

#median blur -- same as average but median -- better in removing noise 
median= cv.medianBlur(img, 3) #kernel size
cv.imshow('median',median)

#bilateral -- this blurs and retains the edges

bilateral = cv.bilateralFilter(img, 5, 15, 15) # diameter, sigma_color , sigma space (diameter of circle- jiske andar jo bhi pixwl hoga that will affter the blur of center pixel
cv.imshow('bilateral', bilateral)
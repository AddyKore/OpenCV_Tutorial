#this will let you split an image in its 3 color channels

import cv2 as cv
import numpy as np

img_og = cv.imread('rav.jpg')

img = cv.resize(img_og, (800,400))
cv.imshow('img', img)

b,g,r = cv.split(img)   # sp;iting the 3 channels seperately

cv.imshow('blue',b)      #this gives out a grey scale intensity based image for that color
cv.imshow('green',g)
cv.imshow('red',r)

print(img.shape)
print(b.shape)
print(g.shape)
print(r.shape)

merged_img = cv.merge([b,g,r])
cv.imshow('merged back',merged_img)


# these above images are black and white, what if we want to display actual color-- here is how

blank = np.zeros(img.shape[:2],dtype='uint8')

blue = cv.merge([b,blank,blank])
green = cv.merge([blank,g,blank])
red = cv.merge([blank,blank,r])

cv.imshow('bluish',blue)
cv.imshow('greeish',green)
cv.imshow('redish',red)
cv.waitKey(0)

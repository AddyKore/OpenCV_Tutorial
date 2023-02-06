import cv2 as cv
import numpy as np

img_og = cv.imread('/home/addy/Addy/python/OpenCV/Cat_Media/rav.jpg')
img = cv.resize(img_og,(800,400))

#translation
def translate(img, x, y):           #have to make a custom function for translation passing the image_name, and x,y legths that we wish to move the image by
    transMat = np.float32([[1,0,x],[0,1,y]])     #we need to make a translation Matrix of this sort which will then be multiplied with our image matrix to get results
    dimensions= (img.shape[1], img.shape[0])   #here we store the dimensions of image as these are needed too
    return cv.warpAffine(img, transMat, dimensions)

'''
here
-x means shift left
-y means shift up
+x means shift right
+y means shifr down
'''

translated = translate(img, 150,150)
cv.imshow('translated', translated)

#Rotation
def rotate(img, angle, rotPoint=None):     # so here to rotate we are sending img, angle to be rotated by and point to be rotated abt
    (height,width) = img.shape[:2]         #since for now we are rotating abt center we need dimensions to find the center

    if rotPoint is None:                    #to calculate the center
        rotPoint = (width//2,height//2)
    rotMat= cv.getRotationMatrix2D(rotPoint, angle, 1.0)      #here we do not define the rotation matrix as we did in translation not that simple
    #we use this function cv.getRotationMatrix2D and pass it the rotation point, angle and a scaling factor 
    dimensions=(width, height)

    #and now we again use the warpAffine to get our transformation

    return cv.warpAffine(img, rotMat, dimensions)

rotated = rotate(img,50)
cv.imshow('rotated',rotated)

#flipped

flip = cv.flip(img, 0)

#0 --> vertical flip
#1 --> horizontal flip

cv.imshow('flip', flip)

cv.waitKey(0)

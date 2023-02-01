import cv2 as cv

img=cv.imread('/home/addy/Addy/python/OpenCV/Cat_Media/rav.jpg')
cv.imshow('cat',img)
cv.waitKey(0)

#reading images is simple reading videos is a whole different game. we need to read videos frame by frame and for that we need a while loop
capture = cv.VideoCapture('/home/addy/Addy/python/OpenCV/Cat_Media/video.mp4')  # here we create a instance of the VideoCapture class by the name of capture
'''
cv.VideoCapture takes 2 types inputs in the brackates
if u put in an integer it would be one of the cameras attached to the system webcam being 0

if you have a video you want to reffer you would pass in the address to the video
'''

#now that the instance is created we have to read the video frame by frame

while True:
    isTrue, frame =capture.read()    
    '''
    here isTrue ka mereko nahi pata but frame is the variable in which our each frame is saved for each itterationof the while loop
    Obviously, it is overwriten every time
    '''                
    cv.imshow('Cat_Video',frame)     #displaying video frame by frame

    if cv.waitKey(20) & 0xFF==ord('d'):      # this is to break out of the while loop if not done, it would be an infinite loop
        break

capture.release()                           #deleting the capture instance
cv.destroyAllWindows()                      #destroying all the windows

#you must have observed for both these popup windows the video was zoomed in thats coz opencv, shows the video in base resolution and the media resolution 
# being bigger than screen resolution it stays that way

# 10/6/19 Sun
import imutils
import numpy as np
import cv2
# source: https://www.learnopencv.com/read-write-and-display-a-video-using-opencv-cpp-python/
# source: https://www.pyimagesearch.com/2017/02/06/faster-video-file-fps-with-cv2-videocapture-and-opencv/


# create a VideoCapture object and read from input a video file
cap = cv2.VideoCapture('/Users/erica/Desktop/f2c.mov')

# checks if video loads successfully
if (cap.isOpened() == False) :
    print ("Error opening video stream or file")

# display the video frame by frame
# read until video is completed
while(cap.isOpened()):
    ret, frame = cap.read()

    # display frame as we display images
    if ret == True:
        # Test code: make some changes to each frame
        # can replace for ML analysis done for each frame here
        frame = imutils.resize(frame, width=450)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        frame = np.dstack([frame, frame, frame])
        cv2.putText(frame, "Hello World", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
    # pause each frame in the video
    # time delay for each frame is 1ms
    # press Q on keyboard to exit
        cv2.imshow('frame',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break
# release video capture object
cap.release()

# close all frames
cv2.destroyAllWindows()

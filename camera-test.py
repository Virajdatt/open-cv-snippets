 #!~/miniforge3/bin/python

import cv2 as cv
import time
import tensorflow as tf
import tensorflow_hub as hub



cap = cv.VideoCapture(0)
if not cap.isOpened():
    print("Cannot open camera")
    exit()
while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    
    print(ret)
    # if frame is read correctly ret is True
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    # Our operations on the frame come here
   
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    #flipHorizontal = cv.flip(frame, 1)
    imagem = cv.bitwise_not(frame)

    # Display the resulting frame
    cv.namedWindow("Gray-Scale", cv.WINDOW_NORMAL)
    cv.resizeWindow("Gray-Scale", 300, 300)
    
    cv.imshow("Gray-Scale", gray,)

    cv.namedWindow("Negative")
    cv.moveWindow('Negative', 700, 800)
    #cv.resizeWindow("Negative", 300, 300)
    cv.imshow("Negative", imagem)
    #cv.imshow('frame', gray)
    #time.sleep(5) 
    #cv.imshow('frame', imagem)
    #cv.imshow('frame',flipHorizontal)
    if cv.waitKey(1) == ord('q'):
        break
# When everything done, release the capture
cap.release()
cv.destroyAllWindows()
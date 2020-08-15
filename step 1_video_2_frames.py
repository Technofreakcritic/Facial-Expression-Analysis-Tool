import os
import numpy as np
import cv2
from datetime import date
import sys

import time




#Get Frames Function And Save As Image
def getFrame(dirname,sec):
    vidcap.set(cv2.CAP_PROP_POS_MSEC,sec*1000)
    hasFrames,image = vidcap.read()
    if hasFrames:
        cv2.imwrite("Arsh"+"/image"+str(count)+".jpg", image)     # save frame as JPG file
    return hasFrames

dirname="Arsh"

vidcap = cv2.VideoCapture("Arsh.mp4")
#Set FrameRate and Sec
sec = 0

# If you want per min then change frameRate to 60.0 for longer video

frameRate = 10.0 #//it will capture image in each 0.5 second
count=1
success = getFrame(dirname,sec)
while success:
    count = count + 1
    sec = sec + frameRate
    sec = round(sec, 2)
    success = getFrame(dirname,sec)

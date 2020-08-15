import os
import numpy as np
import cv2
from datetime import date
import sys
import schedule
import time

#Things in this program

# Step 1 : Get current date
# Step 2 : Check if folder with current date exists
# Step 3 : Check if images are already present
#           If present terminate program
# Step 4 :  Else Check for Video
# Step 5 :  Cut  video into images



#Get Frames Function And Save As Image
def getFrame(dirname,sec):
    vidcap.set(cv2.CAP_PROP_POS_MSEC,sec*1000)
    hasFrames,image = vidcap.read()
    if hasFrames:
        cv2.imwrite(dirname+"/image"+str(count)+".jpg", image)     # save frame as JPG file
    return hasFrames


#Check current date
current_date = date.today()
current_date = current_date.strftime("%d-%b-%Y")

# Folder name Path
path = current_date

# Get the directory name from the specified path
dirname = os.path.basename(path)

if(dirname == current_date):
    print('Yes the same')
else:
    print('Nah amigo. The folder doesnt exist')


# Counter to check images
image_reader = 0

#Check for images
for file in os.listdir(path):
     if file.endswith(".jpg"):
         image_reader += 1

#Change logic operater later
if(image_reader > 0):
    print('Images exist')
    sys.exit()
else:
    for file in os.listdir(path):
        if file.endswith(".mp4"):
            print ('Video File name' ,file)

    vidcap = cv2.VideoCapture(file)
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

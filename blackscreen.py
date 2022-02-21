import cv2
import time
import numpy as np

fourcc=cv2.VideoWriter_fourcc(*'XVID')
outputfile=cv2.VideoWriter('output.avi',fourcc,20.0,(640,480))

cam=cv2.VideoCapture(0)
time.sleep(2)
bg=0

for in in range(60):
    ret,bg=cap.read()

bg=mp.flip(bg,axis=1)

while(cap.isOpened()):
    ret,img=cap.read()
    if not ret:
        break
    img=mp.flip(img,axis=1)

    hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

    lowerred=np.array([0,120,50])
    upperred=np.array([10,255,255])
    mask1=cv2.inRange(hsv,lowerred,upperred)

    lowerred=np.array([170,120,70])
    upperred=np.array([180,255,255])
    mask2=cv2.inRange(hsv,lowerred,upperred)

    mask1=mask1+mask2
    mask1=cv2.morphologyEX(mask1,cv2.MORPH_OPEN,np.ones((3,3),np.unit8))
    mask1=cv2.morphologyEX(mask1,cv2.MORPH_DILATE,np.ones((3,3),np.unit8))

    mask2=cv2.bitwise_not(mask1)
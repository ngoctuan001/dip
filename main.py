import cv2
import numpy as np
import math
from gesture import hand_gesture
from detect import detect_fist
import time
import threading
from grid import grid
import stack


flaglist =[0,0,0,0,0,0,0]
final_answer= [0,0,0,0,0,0,0]
def is_Fist(i,img,answer,confirm, flaglist ,final_answer,center,a):
    # isFist = detect_fist(confirm)

    isFist = a.main(confirm,img)
    cv2.putText(img, answer, (500, 250), cv2.FONT_HERSHEY_SIMPLEX, 2, 2)
    if isFist :
        flaglist[i] = True
        cv2.putText(img, "Activated", (50, 150), cv2.FONT_HERSHEY_SIMPLEX, 2, 2)
        cv2.putText(img, answer, center, cv2.FONT_HERSHEY_SIMPLEX, 2, 2)
        # cv2.rectangle(img, (0, 0), (100, 100), (255, 255, 0), 0)

        final_answer[i] = answer
    else:
        if flaglist[i] == True:
            cv2.putText(img, final_answer[i], center, cv2.FONT_HERSHEY_SIMPLEX, 2, (0,255,255), 5)




cap = cv2.VideoCapture(0)



a1 = stack.detect_()
a2 = stack.detect_()
a3 = stack.detect_()
a4 = stack.detect_()
a5 = stack.detect_()
a6 = stack.detect_()
a7 = stack.detect_()

while(cap.isOpened()):
    # # read image

    ret, img = cap.read()
    img = cv2.flip(img, 1)
    # get hand data from the rectangle sub window on the screen
    # cv2.rectangle(img, (300,300), (200,200), (0,255,0),0)
    # cv2.rectangle(img, (300, 200), (400, 300), (255, 255, 0), 0)
    # cv2.imshow('Gesture', img)
    grid(img)
    screen = img[150:300, 450:600]

    confirm_00 =img[50:150,50:150]
    confirm_01=img[50:150,150:250]
    confirm_11=img[150:250,150:250]
    confirm_12=img[150:250,250:350]
    confirm_20=img[250:350,50:150]
    confirm_21=img[250:350,150:250]
    confirm_22=img[250:350,250:350]
    # cv2.imshow('Gesture', img)

    #
    # if(n==1):
    #     isFist=detect_fist(screen)
    # if isFist:
    #     n=0
    #     isFist=1
    #     cv2.putText(img,"Activated",(50, 50), cv2.FONT_HERSHEY_SIMPLEX, 2, 2)
    #
    #     answer = hand_gesture(screen)
    #     temp = answer
    #     cv2.putText(img, answer, (150, 150), cv2.FONT_HERSHEY_SIMPLEX, 2, 2)

    answer = hand_gesture(screen)

    is_Fist(0,img,answer,confirm_00,flaglist ,final_answer,(85,125),a1)
    is_Fist(1, img, answer, confirm_01, flaglist, final_answer, (185, 125),a2)
    is_Fist(2, img, answer, confirm_11, flaglist, final_answer, (185, 225), a3)
    is_Fist(3, img, answer, confirm_12, flaglist, final_answer, (285, 225),a4)
    is_Fist(4, img, answer, confirm_20, flaglist, final_answer, (85, 325),a5)
    is_Fist(5, img, answer, confirm_21, flaglist, final_answer, (185, 325),a6)
    is_Fist(6,img, answer, confirm_22, flaglist, final_answer, (285, 325),a7)




    cv2.imshow('Gesture', img)

    k = cv2.waitKey(10)
    if k == 27:
        break




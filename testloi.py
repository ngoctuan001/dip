import cv2
import numpy as np
import time
from detect import detect_fist

def func():
    # global first_fist_detection
    global target_time
    first_fist_detection = False
    isFist = detect_fist(confirm)  # a function to detect fist inside that box

    current_time = int(time.time())
    # target_time = 0
    if isFist and not first_fist_detection:
        first_fist_detection = True
        target_time = current_time + 2
        print ("1")
    elif isFist and first_fist_detection:
        # print (first_fist_detection)
        print ("1")
        if current_time > target_time:
            print("current" , current_time, target_time)

            cv2.putText(img, "Fist", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 2, 2)

    else:
        # that is, no fist is detected
        first_fist_detection = False

cap = cv2.VideoCapture(0)
isFist = 0
# current_time = 0
target_time = 0
# first_fist_detection = False
while (cap.isOpened()):

    ret, img = cap.read()
    img = cv2.flip(img, 1)
    cv2.rectangle(img, (100, 100), (300, 300), (0, 255, 0), 0)
    confirm = img[100:300, 100:300]  # narrow the whole webcam to a box

    func()


    # print (first_fist_detection)
    cv2.imshow('Gesture', img)

    k = cv2.waitKey(10)
    if k == 27:
        break

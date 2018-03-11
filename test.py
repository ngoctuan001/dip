import cv2
import numpy as np
import time

def detect_fist(screen):
    hand_cascade = cv2.CascadeClassifier('fist.xml')

    img = screen
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    hands = hand_cascade.detectMultiScale(gray, minSize= (60,60) )

    # for (x, y, w, h) in hands:
    #     cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
    #     return True
    # return False

    for (x, y, w, h) in hands:
        print ("True")
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
        first_fist_detection = False
        current_time = int(time.time())
        if not first_fist_detection:
            first_fist_detection = True
            target_time = current_time + 2
        if first_fist_detection :
            if current_time > target_time:
                cv2.putText(img, "Fist", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 2, 2)
                print ("Correct")





cap = cv2.VideoCapture(0)
while (cap.isOpened()):
    ret, img = cap.read()
    img = cv2.flip(img, 1)



    cv2.rectangle(img, (450, 150), (600, 300), (255, 255, 0), 0)


    confirm = img[150:300, 450:600]  # narrow the whole webcam to a box

    detect_fist(confirm)  # a function to detect fist inside that box

    cv2.imshow('Gesture', img)

    k = cv2.waitKey(10)
    if k == 27:
        break


def is_Fist(i, img, answer, confirm, flaglist, final_answer, center):
    isFist = detect_fist(confirm)
    cv2.putText(img, answer, (500, 250), cv2.FONT_HERSHEY_SIMPLEX, 2, 2)
    if isFist:
        flaglist[i] = True
        cv2.putText(img, "Activated", (50, 150), cv2.FONT_HERSHEY_SIMPLEX, 2, 2)
        cv2.putText(img, answer, center, cv2.FONT_HERSHEY_SIMPLEX, 2, 2)
        # cv2.rectangle(img, (0, 0), (100, 100), (255, 255, 0), 0)

        final_answer[i] = answer
    else:
        if flaglist[i] == True:
            cv2.putText(img, final_answer[i], center, cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 255), 5)
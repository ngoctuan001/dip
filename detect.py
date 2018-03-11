import numpy as np
import cv2
import time
def detect_fist(screen):
    hand_cascade = cv2.CascadeClassifier('fist.xml')

    # cap = cv2.VideoCapture(0)


    # ret, img = cap.read()
    img = screen
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    hands = hand_cascade.detectMultiScale(gray, minSize= (60,60) )

    for (x, y, w, h) in hands:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
        # print(w,h)
        return "FIST"
    return None

    #     cv2.imshow('img', img)
    #     k = cv2.waitKey(30) & 0xff
    #     if k == 27:
    #         break
    #
    # cap.release()
    # cv2.destroyAllWindows()

if __name__ == "__main__":
    cap = cv2.VideoCapture(0)
    while (cap.isOpened()):
        ret, img = cap.read()
        img = cv2.flip(img, 1)
        cv2.rectangle(img, (450, 150), (600, 300), (255, 255, 0), 0)
        screen = img[150:300, 450:600]
        answer = detect_fist(screen)
        cv2.putText(img, answer , (450, 100), cv2.FONT_HERSHEY_SIMPLEX,2, (0,255,255), 5)
        cv2.imshow('Gesture', img)

        k = cv2.waitKey(10)
        if k == 27:
            break


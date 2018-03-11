import cv2
import numpy as np
from detect import detect_fist

import time


class detect_:
    def __init__(self):
        self.first_fist_detection = False
        self.isFist = 0
        self.current_time = 0
        self.target_time = 0

    def main(self,confirm, img):
        self.isFist = detect_fist(confirm)  # a function to detect fist inside that box

        self.current_time = int(time.time())


        if self.isFist and not self.first_fist_detection:
            self.first_fist_detection = True
            self.target_time = self.current_time + 0.2
        elif self.isFist and self.first_fist_detection:
            if self.current_time > self.target_time:
                cv2.putText(img, "Fist", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 2, 2)
                return True
        else:
            # that is, no fist is detected
            self.first_fist_detection = False
            return False



# cap = cv2.VideoCapture(0)
# isFist = 0
# current_time = 0
# target_time = 0
# first_fist_detection = False
# while (cap.isOpened()):
#
#     ret, img = cap.read()
#     img = cv2.flip(img, 1)
#     cv2.rectangle(img, (100, 100), (300, 300), (0, 255, 0), 0)
#     confirm = img[100:300, 100:300]  # narrow the whole webcam to a box
#
#     func()
#
#     # print (first_fist_detection)
#     cv2.imshow('Gesture', img)
#
#     k = cv2.waitKey(10)
#     if k == 27:
#         break


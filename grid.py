import cv2
import numpy as np


def grid(img):
    cv2.rectangle(img, (50, 50), (150, 150), (0, 255, 0), 0)
    cv2.rectangle(img, (150, 50), (250, 150), (0, 255, 0), 0)
    cv2.rectangle(img, (250, 50), (350, 150), (0, 255, 0), -5)
    cv2.rectangle(img, (50, 150), (150, 250), (0, 255, 0), -5)
    cv2.rectangle(img, (150, 150), (250, 250), (0, 255, 0), 0)
    cv2.rectangle(img, (250, 150), (350, 250), (0, 255, 0), 0)
    cv2.rectangle(img, (50, 250), (150, 350), (0, 255, 0), 0)
    cv2.rectangle(img, (150, 250), (250, 350), (0, 255, 0), 0)
    cv2.rectangle(img, (250, 250), (350, 350), (0, 255, 0), 0)

    cv2.rectangle(img, (450, 150), (600, 300), (255, 255, 0), 0)

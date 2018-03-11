import stack
import cv2




cap = cv2.VideoCapture(0)
a = stack.detect_()

while (cap.isOpened()):
    ret, img = cap.read()
    img = cv2.flip(img, 1)
    cv2.rectangle(img, (100, 100), (300, 300), (0, 255, 0), 0)
    confirm = img[100:300, 100:300]  # narrow the whole webcam to a box


    print(a.main(confirm,img))



    cv2.imshow('Gesture', img)

    k = cv2.waitKey(10)
    if k == 27:
        break
import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lower_blue = np.array([50, 80, 80])
    upper_blue = np.array([180, 255, 255])

    mask = cv2.inRange(hsv, lower_blue, upper_blue)
    res = cv2.bitwise_and(frame, frame, mask=mask)

    kernel = np.ones((5, 5), np.uint8)
    # erosion = cv2.erode(mask, kernel, iterations=1)     # erode pixel
    # dilation = cv2.dilate(mask, kernel, iterations=1)   # dilate pixel

    opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)    # remove false positives, such background noise
    closing = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)   # remove false negatives, such some black pixels within object

    cv2.imshow('frame', frame)
    cv2.imshow('res', res)
    # cv2.imshow('erosion', erosion)
    # cv2.imshow('dilation', dilation)
    cv2.imshow('opening', opening)
    cv2.imshow('closing', closing)

    if cv2.waitKey(5) & 0xff == 27:
        break

cap.release()
cv2.destroyAllWindows()


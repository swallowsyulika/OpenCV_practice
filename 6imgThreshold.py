import cv2
import numpy as np

img = cv2.imread("bookpage.jpg")
# ret, threshold = cv2.threshold(img, 12, 255, cv2.THRESH_BINARY)
# !! without grayscale threshold will be very colorful, cause not all BGR are out of thresh
img_grayscaled = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, threshold = cv2.threshold(img_grayscaled, 12, 255, cv2.THRESH_BINARY)
# threshold(img, thresh, max, threshold-type)
# THRESH_BINARY: exceed thresh set max, other set 0
# THRESH_BINARY_INV: exceed thresh set 0, other set max
gaus = cv2.adaptiveThreshold(img_grayscaled, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 155, 1)
# adaptiveThreshold(img, max, adapat-method, threshold-type, block-size, c)

cv2.imshow('original', img)
cv2.imshow('threshold', threshold)
cv2.imshow('gaus', gaus)
cv2.waitKey(0)
cv2.destroyAllWindows()


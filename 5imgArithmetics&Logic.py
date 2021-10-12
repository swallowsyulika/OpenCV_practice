import cv2
import numpy as np

''' matplotlib.png size == mainsvmimage.png > mainlogo.png '''
img1 = cv2.imread('matplotlib.png')
img2 = cv2.imread('mainsvmimage.png')
img3 = cv2.imread('mainlogo.png')

# add = img1 + img2
# this will be sort of messy addition

# add = cv2.add(img1, img2)
# (155,211,79) + (50, 170, 200) = 205, 381, 279...translated to (205, 255,255)
# cv2.imshow('add', add)

# weighted = cv2.addWeighted(img1, 0.6, img2, 0.4, 0)
# addWeighted(img, weight, img, weight, gamma)  can keep affected
# cv2.imshow('weighted', weighted)

rows, cols, channels = img3.shape   # keep mind, img3 is small.
roi = img1[0:rows, 0:cols]

img3gray = cv2.cvtColor(img3, cv2.COLOR_BGR2GRAY)

ret, mask = cv2.threshold(img3gray, 220, 255, cv2.THRESH_BINARY_INV)
# mask will for img3 (the white side is logo) with and

mask_inv = cv2.bitwise_not(mask)
# mask_inv will for img1 (the white side is around the logo) with and

img1_bg = cv2.bitwise_and(roi, roi, mask=mask_inv)
# except logo are 0, else are original
img3_fg = cv2.bitwise_and(img3, img3, mask=mask)
# except logo are original, else are 0

dst = cv2.add(img1_bg, img3_fg)     # let img1_bg(roi) + img3_fg(size equal roi)
img1[0:rows, 0:cols] = dst

cv2.imshow('mask', img3_fg)
cv2.imshow('res', img1)
cv2.waitKey(0)
cv2.destroyAllWindows()


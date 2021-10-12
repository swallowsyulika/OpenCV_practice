import numpy as np
import cv2

img = cv2.imread('nwatch.jpg', cv2.IMREAD_COLOR)

px = img[300, 200]  # the color of px at x y
# and also u can change color   img[300, 200] = [255, 255, 255]
# roi = img[100:150, 100:150]
# print(roi)

img[100:150, 100:150] = [255, 255, 255]     # u can see a white squre
watch_face = img[37:111, 107:194]
img[0:74, 0:87] = watch_face
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()


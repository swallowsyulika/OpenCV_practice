import cv2
import numpy
import matplotlib.pyplot as plt

img = cv2.imread("watch.jpg", cv2.IMREAD_GRAYSCALE)
# cv2.IMREAD_GRAYSCALE   0  default
# cv2.IMREAD_COLOR       1
# cv2.IMREAD_UNCHANGED   -1

## how cv2 show img
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

## how matplotlib show img
# plt.imshow(img, cmap='gray', interpolation='bicubic')
# plt.plot([50, 100], [80, 100], 'c', linewidth=5)       # draw line
# plt.show()

# cv2.imwrite('watch.png', img)   # write file

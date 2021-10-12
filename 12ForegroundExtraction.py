import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("foregroundextraction.jpg")
mask = np.zeros(img.shape[:2], np.uint8)

bgdmodel = np.zeros((1, 65), np.float64)
fgdmodel = np.zeros((1, 65), np.float64)

rect = (125, 125, 240, 240)  # (startx, starty, w, h)
# cv2.rectangle(img, (125, 125), (125+240, 125+240), (255, 0, 0), 1)  check

cv2.grabCut(img, mask, rect, bgdmodel, fgdmodel, 5, cv2.GC_INIT_WITH_RECT)
mask2 = np.where((mask == 2) | (mask == 0), 0, 1).astype('uint8')
img = img * mask2[:, :, np.newaxis]

plt.imshow(img)
plt.colorbar()
plt.show()

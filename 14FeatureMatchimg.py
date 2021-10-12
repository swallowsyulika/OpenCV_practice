import cv2
import numpy as np
import matplotlib.pyplot as plt

temp = cv2.imread("templateforFeature.jpg", 0)
img = cv2.imread("featurematchimg.jpg", 0)

orb = cv2.ORB_create()
kp1, des1 = orb.detectAndCompute(temp, None)
kp2, des2 = orb.detectAndCompute(img, None)

bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

matches = bf.match(des1, des2)
matches = sorted(matches, key=lambda x: x.distance)

imgf = cv2.drawMatches(temp, kp1, img, kp2, matches[:10], None, flags=2)
plt.imshow(imgf)
plt.show()

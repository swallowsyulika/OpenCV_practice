import numpy as np
import cv2

img = cv2.imread("watch.jpg", cv2.IMREAD_COLOR)
# (fp, point1, point2, BGR(in opencv), linewidth)
cv2.line(img, (0, 0), (500, 500), (212, 255, 127), 10)  # aq
cv2.rectangle(img, (100, 100), (400, 400), (255, 0, 0), 5)  # b
cv2.circle(img, (300, 300), 25, (0, 0, 255), -1)    # r

pts = np.array([[180, 180], [240, 200], [350, 350], [200, 420]], np.int32)
cv2.polylines(img, [pts], True, (0, 255, 0), 10)    # g

font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img, 'opencv watch', (200, 100), font, 1, (200, 255, 255), 2, cv2.LINE_AA)

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

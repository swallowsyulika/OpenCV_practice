import cv2
import numpy as np

cap = cv2.VideoCapture(0)       # set camera 0>>>first 1>>>secend
# fourcc = cv2.VideoWriter_fourcc(*'XVID')    # set editor
# out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))
# (file name, fp, fps, resolution)

while True:
    ret, frame = cap.read()     # read() will return two objs, first is bool, secend is frame
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)      # turn to gray
    # out.write(frame)
    cv2.imshow('frame', frame)
    cv2.imshow('gray', gray)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
# out.release()
cv2.destroyAllWindows()


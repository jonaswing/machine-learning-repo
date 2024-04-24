import cv2
import numpy as np

img = np.zeros((500, 500, 3), np.uint8)
img[:, :] = 255

cv2.putText(img, 'Text', (20, 40),
            cv2.FONT_HERSHEY_SIMPLEX, 1,
            (0,0,0), 2, cv2.LINE_AA)

cv2.putText(img, 'Text', (300, 80),
            cv2.FONT_HERSHEY_SIMPLEX, 2,
            (0,0,0), 2, cv2.LINE_AA)

cv2.putText(img, 'Text', (20, 300),
            cv2.FONT_HERSHEY_SIMPLEX, 3,
            (0,0,0), 2, cv2.LINE_AA)

cv2.putText(img, 'Text', (250, 450),
            cv2.FONT_HERSHEY_SIMPLEX, 4,
            (0,0,0), 2, cv2.LINE_AA)

cv2.imshow('Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

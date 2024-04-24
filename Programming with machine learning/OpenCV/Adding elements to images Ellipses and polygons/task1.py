import cv2
import numpy as np


img = np.zeros((500, 500, 3), np.uint8)
img[:, :] = 255


pts = np.array([[250, 25],[350, 150],
                [486,150], [400, 250],
                [420, 370], [250, 300],
                [130, 370], [25, 150]], np.int32)

coordinates = pts.reshape((-1,1,2))
# Draw the polygon on the image, using the coordinates. A line will be drawn
# from the last coordinate to connect it to the first (True) using the colour
# white and a line thickness of 3.
cv2.polylines(img, [coordinates], True,(0, 0, 255), 3)

cv2.imshow('Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
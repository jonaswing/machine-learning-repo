import cv2
import numpy as np


# Create black image
img = np.ones((500, 500, 3), np.uint8)
img[:, :] = 0

# Draw filled circle
cv2.circle(img, (250, 250), 240, (255, 255, 255), -1)
# Draw outline circle
cv2.circle(img, (250, 250), 240, (0, 255, 0), 5)

# Draw smaller filled circle
cv2.circle(img, (250, 250), 200, (240, 240, 240), -1)
# Draw smaller outline circle
cv2.circle(img, (250, 250), 200, (100, 255, 100), 5)

# Draw smaller filled circle
cv2.circle(img, (250, 250), 160, (220, 220, 220), -1)
# Draw smaller outline circle
cv2.circle(img, (250,50), 160, (200, 255, 200), 5)

# Draw smaller filled circle
cv2.circle(img, (250, 250), 120, (200, 200, 200), -1)
# Draw smaller outline circle
cv2.circle(img, (250, 250), 120, (230, 255, 230), 5)

# Draw smaller filled circle
cv2.circle(img, (250, 250), 80, (180, 180, 180), -1)
# Draw smaller outline circle
cv2.circle(img, (250, 250), 80, (240, 255, 240), 5)


cv2.imshow('Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
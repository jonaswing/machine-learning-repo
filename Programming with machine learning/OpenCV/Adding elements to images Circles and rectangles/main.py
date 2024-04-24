# import OpenCV
import cv2
# import numpy
import numpy as np
# Create a white image with 3 channels 512 x 512 pixels in size.
img = np.zeros((512,512,3), np.uint8)
img[:, :] = 255
# Draw a blue circle with a center at (450, 100) and
# radius at 50. The rectangle is drawn with a line thickness of 3.
cv2.circle(img, (450, 100), 50, (255, 0, 0), 5)
# Draw a pink circle with a center at (200, 400) and
# radius at 90. The rectangle is drawn as filled (-1)..
cv2.circle(img, (200, 400), 90, (147, 20, 255), -1)
# Draw a green rectangle with a top left corner at (100, 100) and
# bottom right at (200, 200). The rectangle is drawn with a line thickness of 5.
cv2.rectangle(img, (100, 100), (200, 200), (0, 255, 0), 5)
# Draw an orange rectangle with a top left corner at (300, 300) and
# bottom right at (450, 4500). The rectangle is drawn as filled (-1).
cv2.rectangle(img, (300, 300), (450, 450), (0, 165, 255), -1)

# Display the image
cv2.imshow("The image", img)
# Waits for user to press any key
cv2.waitKey(0)
# Close all open windows
cv2.destroyAllWindows()
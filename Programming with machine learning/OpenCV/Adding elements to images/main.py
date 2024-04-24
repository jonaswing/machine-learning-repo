# import OpenCV
import cv2
# import numpy
import numpy as np
# Create a black image with 3 channels, 512 x 512 pixels in size.
img = np.zeros((512,512,3), np.uint8)
# Draw a vertical red line with thickness of 3px
cv2.line(img, (255,0), (255,511), (0,0,255), 3)
# Draw a horizontal blue line with thickness of 5px
cv2.line(img, (0,255), (511,255), (255,0,0), 5)
# Draw a diagonal green line from the top-left to bottom right corner
# with a thickness of 7 px.
cv2.line(img, (0,0), (511,511), (0, 255, 0), 7)
# Draw a diagonal purple line from the bottom-left to top right corner
# with a thickness of 9 px.
cv2.line(img, (0,511), (511,0), (128,0,128), 9)

# Display the image
cv2.imshow("The image", img)
# Waits for user to press any key
cv2.waitKey(0)
# Close all open windows
cv2.destroyAllWindows()
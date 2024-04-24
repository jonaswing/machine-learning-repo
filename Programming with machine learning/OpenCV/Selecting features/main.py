# import OpenCV
import cv2
# import numpy
import numpy as np


# Using cv2.imread() method to read the file specified.
# Image provided by @macrovector_official on Freepik.com
img = cv2.imread('bird4.jpg')
# Convert the image to grayscale
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# Shi-Tomasi corner detection
# Creates a new goodFeaturesToTrack object, it receives:
# - The grayscale image in which to look for corners.
# - The number of corners to find (100).
# - The quality of the corners to find. This value is in the range 0 to 1. Corners
#   below this threshold are dropped (0.1).
# - The minimum Euclidean distance between detected corners (10).
kp = cv2.goodFeaturesToTrack(gray,100,0.1,10)
# Convert the floating point corner values to integers
kp = np.int0(kp)
print("Top 5 corners detected:\n", kp[:5])
# Convert the gray scale image back to a 3-channel image.
# This is only necessary if you want to be able to see the
# keypoints drawn in colour on the grayscale image. Otherwise,
# the keypoints may be drawn on the colour image or in grayscale on
# the original grayscale image.
img = cv2.cvtColor(gray,cv2.COLOR_GRAY2BGR)
# Iterate through all the keypoints
for i in range(0,len(kp)):
    # Retrieve x and y values of each keypoint
    x = kp[i][0, 0]
    y = kp[i][0, 1]
    # Draw a red circle on the image for each keypoint, with a radius and thickness of 10.
    cv2.circle(img,(x,y), 5, (0, 0, 255), 1)

# Display the output image
cv2.imshow("Face with keypoints (Shi-Tomasi)", img)
# Waits for user to press any key
cv2.waitKey(0)
# Close all open windows
cv2.destroyAllWindows()
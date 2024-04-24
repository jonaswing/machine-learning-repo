# import OpenCV
import cv2
# import numpy
import numpy as np


# Using cv2.imread() method to read the file specified.
# Image provided by @macrovector_official on Freepik.com
img = cv2.imread('bird9.jpg')
# Convert the image to grayscale
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# Create an ORB_create() object
orb = cv2.ORB_create()
# Find the keypoints in the image, using ORB.
kp = orb.detect(img, None)
# Display the number of corners detected.
print("Number of corners detected:\n", len(kp))
# Compute the descriptors with ORB
kp, des = orb.compute(img, kp)
# Output the first descriptor
print("First descriptor:\n",des[0])
# Draw the keypoints on the grayscale image.
img = cv2.drawKeypoints(gray, kp, None, color=(0,0,255),
                        flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

# Display the output image
cv2.imshow("Face with keypoints (ORB)", img)
# Waits for user to press any key
cv2.waitKey(0)
# Close all open windows
cv2.destroyAllWindows()
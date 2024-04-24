# import OpenCV
import cv2
# import numpy
import numpy as np


# Using cv2.imread() method to read the file specified.
# Image provided by @macrovector_official on Freepik.com
img = cv2.imread('bird4.jpg')
# Convert the image to grayscale
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# Key point detection using SIFT
siftfeatures = cv2.SIFT_create()
# Use the SIFT_create object to detect keypoints in the grayscale image.
kp = siftfeatures.detect(gray, None)
# Display the number of corners detected.
print("Number of corners detected:\n", len(kp))
# #drawing the key points on the input image using drawKeypoints() function
# - The first parameter is the image to draw on, in this case, it's the grayscale, but it could have been the original.
# - The list of keypoints. The keypoints contain more than just coordinates.
# - An output image. In this case, an image is returned, so output image is set to None.
# - The colour with which to draw the keypoints (red). If not specified, each keypoint will have its own colour.
# - There are multiple flags with which the keypoints may be drawn,
#   such as simply drawing small dots:  v2.DRAW_MATCHES_FLAGS_DEFAULT. This flag draws
#   the keypoints with information regarding the corner size and orientation.
img = cv2.drawKeypoints(gray, kp, None, (0,0,255),
                        flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

# Display the output image
cv2.imshow("Face with keypoints (SIFT)", img)
# Waits for user to press any key
cv2.waitKey(0)
# Close all open windows
cv2.destroyAllWindows()
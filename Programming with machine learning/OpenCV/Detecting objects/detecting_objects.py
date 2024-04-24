# import OpenCV
import cv2
# import numpy
import numpy as np

# Using cv2.imread() method to read the file specified as grayscale.
# Image provided by @aedka on Freepik.com
img = cv2.imread("coins.jpg", 0)
img = cv2.resize(img,(1024, 768))


# Setup SimpleBlobDetector parameters.
params = cv2.SimpleBlobDetector_Params()

# Change thresholds
params.minThreshold = 0
params.maxThreshold = 255

# Filter by Area.
params.filterByArea = True
params.minArea = 500
params.maxArea = 100000

# Filter by Circularity
params.filterByCircularity = True
params.minCircularity = 0.4

# Filter by Convexity
params.filterByConvexity = True
params.minConvexity = 0.01

# Filter by Inertia
params.filterByInertia = True
params.minInertiaRatio = 0.01

# Set up the detector with the custom parameters.
detector = cv2.SimpleBlobDetector_create(params)

# Detect blobs.
kp = detector.detect(img)

# Output the number of blobs detected, as indicated by the number of key points.
print("Number of blobs detected: ", len(kp))

# Draw detected blobs as red circles.
img_with_blobs = cv2.drawKeypoints(img, kp, None, (0, 0, 255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

# Display the image
cv2.imshow("Blobs", img_with_blobs)
# Waits for user to press any key
cv2.waitKey(0)
# Close all open windows
cv2.destroyAllWindows()
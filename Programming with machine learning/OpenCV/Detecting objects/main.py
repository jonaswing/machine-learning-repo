# import OpenCV
import cv2
# import numpy
import numpy as np

# Using cv2.imread() method to read the file specified as grayscale.
# Image provided by @aedka on Freepik.com
img = cv2.imread("coins.jpg", 0)
img = cv2.resize(img,(1024, 768))

# Set up the detector with the default parameters.
detector = cv2.SimpleBlobDetector_create()

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
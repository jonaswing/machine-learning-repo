# import OpenCV
import cv2
# import numpy
import numpy as np

# Using cv2.imread() method to read the file specified as grayscale.
# Image provided by @starline on Freepik.com
img = cv2.imread("shapes.jpg")

# Converts the image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# Use thresholding to create a binary image
ret, thresh = cv2.threshold(gray, 240, 255, cv2.THRESH_BINARY)
# Use findContours to find the contour lines of the image.
# The first parameter is the image on which to find the contours, the second
# parameter refers to the retrieval mode and the last to whether all the boundary points are returned
# or only the start and end points of lines.
# contours contains the list (or tree-structure) of contour points and hierarchy
# contains a structure describing how the shapes are related to each other.
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
#  Create empty images (the same size as the original) on which to draw the contours.
img_contours_a = np.zeros(img.shape)
img_contours_b = np.zeros(img.shape)
# Use drawContours to draw the contours on the specific image. The first -1 value
# indicates that all contours should be drawn; alternatively specific contours may
# be drawn by providing an index.
# The contours are first drawn on copies of the original image and then on 2 all
# black images. In both cases, the first drawContours statement draws the contour
# outlines in green at a line width of 5. The second drawContours statement fills the
# contours (-1) with red.
# Draw on copies of the original image
img_1 = img.copy()
img_2 = img.copy()
cv2.drawContours(img_1, contours, -1, (0, 255, 0), 5)
cv2.drawContours(img_2, contours, -1, (0, 0, 255), -1)
# Draw on a black background
cv2.drawContours(img_contours_a, contours, -1, (0, 255, 0), 5)
cv2.drawContours(img_contours_b, contours, -1, (0, 0, 255), -1)
# Horizontally and vertically stack the original and contour images.
combined_a = np.hstack([img_1, img_2])
combined_b = np.hstack([img_contours_a, img_contours_b])
# Display the contours on the original images
cv2.imshow("Drawn on the original image", combined_a)
# Waits for user to press any key
cv2.waitKey(0)
# Display the contours on the black images
cv2.imshow("Drawn on the black background", combined_b)
# Waits for user to press any key
cv2.waitKey(0)
# Destroy all windows created by the script
cv2.destroyAllWindows()
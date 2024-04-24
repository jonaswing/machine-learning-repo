import cv2
import numpy as np

image = cv2.imread('bird4.jpg')

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

ret, thresh = cv2.threshold(gray, 135, 200, cv2.THRESH_BINARY)

contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

img_contours_a = np.zeros(image.shape)
img_contours_b = np.zeros(image.shape)


img_1 = image.copy()
img_2 = image.copy()
cv2.drawContours(img_1, contours, -1, (0, 255, 0), 1)
cv2.drawContours(img_2, contours, -1, (0, 0, 255), -1)
# Draw on a black background
cv2.drawContours(img_contours_a, contours, -1, (0, 255, 0), 1)
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

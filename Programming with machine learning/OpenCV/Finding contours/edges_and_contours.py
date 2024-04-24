import cv2
import numpy as np


img = cv2.imread('bird4.jpg')
cv2.imshow('Original', img)
cv2.waitKey(0)

# Grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('Gray', gray)
cv2.waitKey(0)

# Blurred
blurred = cv2.GaussianBlur(gray, (3,3), 0)
cv2.imshow('Blurred', blurred)
cv2.waitKey(0)

# Binary
retval1, binary = cv2.threshold(gray, 130, 255, cv2.THRESH_BINARY)
cv2.imshow('Binary', binary)
cv2.waitKey(0)

# Canny edge detection
canny_image = cv2.Canny(blurred, 100, 200)
cv2.imshow('Canny', canny_image)
cv2.waitKey(0)

# Sobel edge detection
sobel_x = cv2.Sobel(binary,cv2.CV_64F,1,0)
cv2.imshow('Sobel', sobel_x)
cv2.waitKey(0)



# Contour
contours, hierarchy = cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
img_contours_a = np.zeros(img.shape)
img_1 = img.copy()
cv2.drawContours(img_1, contours, -1, (0, 255, 0), 1)
cv2.imshow('Contour', img_1)
cv2.waitKey(0)


cv2.destroyAllWindows()




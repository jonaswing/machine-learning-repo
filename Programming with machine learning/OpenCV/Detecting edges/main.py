# import OpenCV
import cv2
# import numpy
import numpy as np

# Using cv2.imread() method to read the file specified.
# Image provided by @rawpixel.com on Freepik.com
img = cv2.imread("GroupPhoto.jpg")

# Converting the image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# Remove noise from the image using Gaussian blur.
# This step may be omitted or replaced with another type of
# noise removal.
# GaussianBlur requires an image to be applied to, a mask size (3 x 3) and
# the standard deviation in the x and y directions (set to 0 in this case).
blurred = cv2.GaussianBlur(gray,(3,3),0)

# Create the edge images by calling each of the edge detection functions
# Applies laplacian edge detection
laplacian = cv2.Laplacian(blurred,cv2.CV_64F)
# Applies Sobel edge detection to the x-axis
sobel_x = cv2.Sobel(blurred,cv2.CV_64F,1,0)
# Applies Sobel edge detection to the y-axis
sobel_y = cv2.Sobel(blurred,cv2.CV_64F,0,1)
# Applies Canny edge detection
canny = cv2.Canny(gray, 100, 200)

# Saves each image to disk
cv2.imwrite("laplacian.jpg", laplacian)
cv2.imwrite("sobel_x.jpg", sobel_x)
cv2.imwrite("sobel_y.jpg", sobel_y)
cv2.imwrite("canny.jpg", canny)
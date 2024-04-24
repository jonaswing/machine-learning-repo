#Import OpenCV
import cv2

# Using cv2.imread() method to read the file specified.
# Image provided by @pink1unicorn on Freepik.com
img = cv2.imread("bird4.jpg")
# Convert the colour image to grayscale first
img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# Convert the image to black and white using a threshold of 127.
ret, bw = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
# Display the original image
cv2.imshow("Black and white dog", bw)
# Waits for user to press any key
cv2.waitKey(0)

# Convert the image to inverted black and white using a threshold of 127
ret, bw_inv = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY_INV)
# Display the original image
cv2.imshow("Inverted black and white dog", bw_inv)
# Waits for user to press any key
cv2.waitKey(0)

# Convert the image to black and white using a threshold of 50
ret, bw_low_thresh = cv2.threshold(img, 50, 255, cv2.THRESH_BINARY)
# Display the original image
cv2.imshow("Black and white dog, with low threshold", bw_low_thresh)
# Waits for user to press any key
cv2.waitKey(0)

# Convert the image to black and white using a threshold of 200
ret, bw_high_thresh = cv2.threshold(img, 200, 255, cv2.THRESH_BINARY)
# Display the original image
cv2.imshow("Black and white dog, with high threshold", bw_high_thresh)
# Waits for user to press any key
cv2.waitKey(0)
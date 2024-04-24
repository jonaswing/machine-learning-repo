#Import OpenCV
import cv2

# Using cv2.imread() method to read the file specified.
# Image provided by @user16172657 on Freepik.com
img = cv2.imread("bird4.jpg")

# Display the image
cv2.imshow('Original snowy town', img)

# Waits for user to press any key
cv2.waitKey(0)

# Rotate the image 90 degrees clockwise
img = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)

# Display the image
cv2.imshow('Snowy town 90', img)

# Waits for user to press any key
cv2.waitKey(0)

# Rotate the image 180 degrees
img = cv2.rotate(img, cv2.ROTATE_180)

# Display the image
cv2.imshow('Snowy town 270 (90 + 180)', img)

# Waits for user to press any key
cv2.waitKey(0)

# Closing all open windows
cv2.destroyAllWindows()
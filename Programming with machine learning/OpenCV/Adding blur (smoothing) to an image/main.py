#Import OpenCV
import cv2

# Using cv2.imread() method to read the file specified.
# Image provided by @pink1unicorn on Freepik.com
img = cv2.imread("bird4.jpg")

# Display the original image
cv2.imshow("Original cat", img)
# Waits for user to press any key
cv2.waitKey(0)

# Smooth the image using a 3x3 mask
smoothed_3x3 = cv2.blur(img, (3,3))
# Display the original image
cv2.imshow("3x3 Smoothed cat", smoothed_3x3)
# Waits for user to press any key
cv2.waitKey(0)

# Smooth the image using a 50x50 mask
smoothed_50x50 = cv2.blur(img, (50,50))
# Display the original image
cv2.imshow("50x50 Smoothed cat", smoothed_50x50)
# Waits for user to press any key
cv2.waitKey(0)

# Smooth the image using a 100x100 mask
smoothed_100x100 = cv2.blur(img, (100,100))
# Display the original image
cv2.imshow("100x100 Smoothed cat", smoothed_100x100)
# Waits for user to press any key
cv2.waitKey(0)

# closing all open windows
cv2.destroyAllWindows()
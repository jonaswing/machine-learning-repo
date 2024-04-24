#Import OpenCV
import cv2

# Using cv2.imread() method to read the file specified.
# Image provided by @pink1unicorn on Freepik.com
img = cv2.imread("bird4.jpg")

# Display the original image
cv2.imshow("Original dog", img)
# Waits for user to press any key
cv2.waitKey(0)

# Convert the image to grayscale using the blue,green,red to gray conversion
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# Display the original image
cv2.imshow("Grayscale dog", gray)
# Waits for user to press any key
cv2.waitKey(0)

# Convert the image to grayscale using the blue,green,red to HLS conversion
hls = cv2.cvtColor(img,cv2.COLOR_BGR2HLS)
# Display the original image
cv2.imshow("HLS dog", hls)
# Waits for user to press any key
cv2.waitKey(0)

# Convert the image to grayscale using the blue,green,red to HSV conversion
hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
# Display the original image
cv2.imshow("HSV dog", hsv)
# Waits for user to press any key
cv2.waitKey(0)

# closing all open windows
cv2.destroyAllWindows()
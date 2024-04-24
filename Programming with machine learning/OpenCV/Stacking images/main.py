#Import OpenCV and Numpy
import cv2
import numpy as np

# Using cv2.imread() method to read the file specified.
# Image provided by @pink1unicorn on Freepik.com
img = cv2.imread("bird4.jpg")

# Create 3 colour space converted images
yuv = cv2.cvtColor(img,cv2.COLOR_BGR2YUV)
hls = cv2.cvtColor(img,cv2.COLOR_BGR2HLS)
hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

# Horizontally stack the original and yuv images
# next to each other to create a new image.
horizontal_1 = np.hstack((img, yuv))
# Horizontally stack the hls and hsv images
# next to each other to create a new image.
horizontal_2 = np.hstack((hls, hsv))
# Vertically stack the two horizontal images.
vertical_1 = np.vstack((horizontal_1, horizontal_2))
# Resize the new stacked image to the size of the original image.
stacked = cv2.resize(vertical_1,(img.shape[1], img.shape[0]))

# Display the combined (stacked) image.
cv2.imshow("Stacked image", stacked)
# Waits for user to press any key
cv2.waitKey(0)

# closing all open windows
cv2.destroyAllWindows()
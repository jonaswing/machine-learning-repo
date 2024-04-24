#Import OpenCV
import cv2

# Using cv2.imread() method to read the file specified.
img = cv2.imread("bird4.jpg")

print(img.shape)

# Create a copy of the image to highlight the area of interest from which
# the cropped copy is to be created.
area_of_interest = img.copy()
# Draw a red rectangle around the top bird by
# setting pixel values to red.
# This is not necessary, but is done in this example to highlight
# the area to be retrieved by cropping.
area_of_interest[10:60,100:180] = [0,0,255]





# Display the area_of_interest image
cv2.imshow('Area of interest', area_of_interest)
# Waits for user to press any key
cv2.waitKey(0)

# Creates a cropped version of the original version
# that only contains the area of interest.
# The slice includes all pixels in rows 800 to 1050 and columns 2850:3630.
cropped = img[10:60,100:180]

# Display the cropped image
cv2.imshow('Cropped image', cropped)
#
# Waits for user to press any key
cv2.waitKey(0)

# closing all open windows
cv2.destroyAllWindows()
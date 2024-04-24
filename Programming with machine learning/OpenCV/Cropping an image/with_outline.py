# Import OpenCV
import cv2

# Using cv2.imread() method to read the file specified.
img = cv2.imread("bird4.jpg")

# Create a copy of the image to highlight the area of interest
area_of_interest = img.copy()

# Draw a red rectangle outline around the specified area
x1, y1, x2, y2 = 100, 10, 180, 60
cv2.rectangle(area_of_interest, (x1, y1), (x2, y2), (0, 0, 255), thickness=1)

# Display the area_of_interest image
cv2.imshow('Area of interest', area_of_interest)
cv2.waitKey(0)

# Creates a cropped version of the original version
# that only contains the area of interest.
cropped = img[y1:y2, x1:x2]

# Display the cropped image
cv2.imshow('Cropped image', cropped)
cv2.waitKey(0)

# Closing all open windows
cv2.destroyAllWindows()

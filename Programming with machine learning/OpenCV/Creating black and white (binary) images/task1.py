import cv2

# The image
image = cv2.imread('bird4.jpg')

# Convert image to greyscale
grey = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow('Grey', grey)
cv2.waitKey(0)

# Convert image to black and white
retval1, thresh1 = cv2.threshold(grey, 64, 255, cv2.THRESH_BINARY)
cv2.imshow('threshold 1', thresh1)
cv2.waitKey(0)

# Convert image with thresh 127
retval2, thresh2 = cv2.threshold(grey, 127, 255, cv2.THRESH_BINARY)
cv2.imshow('threshold 2', thresh2)
cv2.waitKey(0)

# Convert image with thresh 135
retval3, thresh3 = cv2.threshold(grey, 135, 255, cv2.THRESH_BINARY)
cv2.imshow('threshold 3', thresh3)
cv2.waitKey(0)


# Inverting the image with best threshold
inverted_binary = cv2.bitwise_not(thresh3)
cv2.imshow('Inverted', inverted_binary)
cv2.waitKey(0)

# Saving the inverted image to disk
cv2.imwrite('inverted.jpg', inverted_binary)

cv2.destroyAllWindows()
#Import OpenCV
import cv2

# Using cv2.imread() method to read the file specified.
# Image provided by @user16172657 on Freepik.com
img = cv2.imread("birds2.jpg")

# Rescale image by providing a new size. This scaling does
# not take aspect ratio into account and simply rescales the image
# to the provided size.
by_size = cv2.resize(img, dsize=(1024, 768))
# Rescale image by providing scaling factors. 0.5 scales the image
# to half its original size. If the fx and fy values do not match,
# the image's aspect ratio will not be maintained.
# dsize is set to None as it is a required parameter.
by_factor = cv2.resize(img, dsize=None, fx=0.2, fy=0.2)

# Output the original and new image shapes
print("Original shape: ", img.shape)
print("Scaled by size shape: ", by_size.shape)
print("Scaled by factor shape: ", by_factor.shape)

cv2.imshow("Resized bird", by_factor)

cv2.waitKey(0)
cv2.destroyAllWindows()
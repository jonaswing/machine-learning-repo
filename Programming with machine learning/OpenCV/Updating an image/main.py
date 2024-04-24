#Import OpenCV
import cv2

# Using cv2.imread() method to read the file specified.
img = cv2.imread("birds2.jpg")
# Draw a red rectangle around the top bird by
# setting pixel values to blue.
# Draw the left line at 10 pixels wide
img[800:1050,2850:2860] = [255,0,0]
# Draw the right line at 10 pixels wide
img[800:1050,3620:3630] = [255,0,0]
# Draw the top line at 10 pixels wide
img[800:810,2850:3630] = [255,0,0]
# Draw the bottom line at 10 pixels wide
img[1050:1060,2850:3630] = [255,0,0]
# Draw a green rectangle around the middle bird by
# setting pixel values to red.
img[1350:1650,3150:3160] = [0,255,0]
img[1350:1650,3780:3790] = [0,255,0]
img[1350:1360,3150:3790] = [0,255,0]
img[1650:1660,3150:3790] = [0,255,0]
# Draw a red rectangle around the bottom bird by
# setting pixel values to red.
img[2000:2450,3150:3160] = [0,0,255]
img[2000:2450,3880:3890] = [0,0,255]
img[2000:2010,3150:3890] = [0,0,255]
img[2450:2460,3150:3890] = [0,0,255]

# Saves the image as the file name specified.
# If no path is included it is saved in the current working directory.
# Otherwise, if a full path is provided, it is saved at the
# specified location.
cv2.imwrite("BirdsUpdated2.jpg", img)
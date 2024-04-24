# import OpenCV
import cv2
# import numpy
import numpy as np

# Create a black image with 3 channels 512 x 512 pixels in size.
img = np.zeros((512,512,3), np.uint8)
# Draw an ellipse with its center at (256, 256) within a rectangle of size (200, 50).
# The ellipse is to be drawn at an angle of 0 degrees, with all pixels in the ellipse
# from 0 to 360 degrees to be drawn using red (0, 0, 255). The ellipse is to be drawn
# using a line width of 5.
cv2.ellipse(img,(256, 256), (200, 50), 0, 0, 360, (0, 0, 255), 5)
# Draw an ellipse with its center at (256, 256) within a rectangle of size (200, 50).
# The ellipse is to be drawn at an angle of 90 degrees, with all pixels in the ellipse
# from 0 to 360 degrees to be drawn using blue (0, 0, 255). The ellipse is to be drawn
# using a line width of 7.
cv2.ellipse(img,(256, 256), (200, 50), 90, 0, 360, (255, 0, 0), 7)
# Draw an ellipse with its center at (256, 256) within a rectangle of size (200, 50).
# The ellipse is to be drawn at an angle of 45 degrees, with all pixels in the ellipse
# from 0 to 180 degrees to be drawn using green (0, 255, 0). The ellipse is to be drawn
# using a line width of 9.
cv2.ellipse(img,(256, 256), (200, 50), 45, 0, 180, (0, 255, 0), 9)
# Draw an ellipse with its center at (256, 256) within a rectangle of size (200, 50).
# The ellipse is to be drawn at an angle of 135 degrees, with all pixels in the ellipse
# from 180 to 360 degrees to be drawn using yellow (128, 128, 0). The ellipse is to be drawn
# as filled.
cv2.ellipse(img,(256, 256), (200, 50), 135, 180, 360, (0, 255, 255), -1)
# Define a series of vertices (coordinates) to be used to draw the polygon
pts = np.array([[150, 25],[350, 25],
                [486,150], [486, 350],
                [350, 486], [150, 486],
                [25, 350], [25, 150]], np.int32)
# Reshape it to use the number of elements in the array as
# (NUMBER OF ROWS (COORDINATES), 1, 2) -> -1 forces Python to use the number of elements
# in the input data as the number of rows.
coordinates = pts.reshape((-1,1,2))
# Draw the polygon on the image, using the coordinates. A line will be drawn
# from the last coordinate to connect it to the first (True) using the colour
# white and a line thickness of 3.
cv2.polylines(img, [coordinates], True,(255, 255, 255), 3)

# Display the image
cv2.imshow("The image", img)
# Waits for user to press any key
cv2.waitKey(0)
# Close all open windows
cv2.destroyAllWindows()
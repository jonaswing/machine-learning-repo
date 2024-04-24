# import OpenCV
import cv2
# import numpy
import numpy as np

# Using cv2.imread() method to read the file specified.
# Image provided by @wirestock on Freepik.com
img = cv2.imread("bird4.jpg")
# Create a grayscale copy of the image
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# Convert back to GBR to have a grayscale 3-channel image
gray = cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)
# Place the text "Original" on the original image
# at position (1100, 2200), using the font FONT_HERSHEY_SIMPLEX,
# at font size 10 in white, with a line width of 3. Anti-aliasing
# (a form of smoothing) is applied to the lines of the text (LINE_AA).
cv2.putText(img, "Original",(50, 150),
            cv2.FONT_HERSHEY_SIMPLEX, 1,
            (255, 255, 255), 2, cv2.LINE_AA)
# Place the text "Grayscale" on the grayscale image
# at position (1000, 2200), using the font FONT_HERSHEY_SIMPLEX,
# at font size 10 in red, with a line width of 3. Anti-aliasing
# (a form of smoothing) is applied to the lines of the text (LINE_AA).
cv2.putText(gray, "Grayscale",(50, 150),
            cv2.FONT_HERSHEY_SIMPLEX, 1,
            (0, 0, 255), 2, cv2.LINE_AA)
# Draw a red rectangle around the sloth
cv2.rectangle(gray, (830, 200), (1650, 1400), (0, 0, 255), 3)
# Place the text "(830, 200)" above the top-left corner of the rectangle.
# In this case the text is displayed at a smaller font size of 2.
cv2.putText(gray, "(830, 200)",(830, 160),
            cv2.FONT_HERSHEY_SIMPLEX, 2,
            (0, 0, 255), 3, cv2.LINE_AA)
# Stack the 2 images horizontally as a single image.
combined = np.hstack([img, gray])
# Resize the image to half it's current width and height.
combined = cv2.resize(combined, None, None, fx=0.5, fy=0.5)

# Display the image
cv2.imshow("The image", combined)
# Waits for user to press any key
cv2.waitKey(0)
# Close all open windows
cv2.destroyAllWindows()
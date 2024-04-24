import cv2
import numpy as np

# Read image
original_image = cv2.imread('Shadows.jpg')
original_image = cv2.resize(original_image,(600, 310))

# Set up the detector with default parameters.
detector = cv2.SimpleBlobDetector_create()

# Detect blobs.
kp = detector.detect(original_image)

# Draw detected blobs as red circles.
img_with_blobs = cv2.drawKeypoints(original_image, kp, None, (0, 0, 255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

# Stack the images vertically
stacked_images = np.vstack((original_image, img_with_blobs))

# Draw red line between the stacked images
cv2.line(stacked_images, (0, 305), (600, 305), (0,0,255), 2)

# Write "Original image" text on original image
cv2.putText(stacked_images, 'Original image', (150, 150),
            cv2.FONT_HERSHEY_SIMPLEX, 1.2,
            (0,0,255), 1, cv2.LINE_AA)

# Write "15 blobs detected" text on drawn image
cv2.putText(stacked_images, '15 blobs detected', (20, 340),
            cv2.FONT_HERSHEY_SIMPLEX, 0.6,
            (0,0,255), 1, cv2.LINE_AA)

# Display the image
cv2.imshow("Blobs", stacked_images)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Save the updated image
cv2.imwrite('Updated_shadows.jpg', stacked_images)
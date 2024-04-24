import cv2
import os
import numpy as np

image1 = cv2.imread('10images/bird1.jpg')
image2 = cv2.imread('10images/bird2.jpg')
image3 = cv2.imread('10images/bird3.jpg')
image4 = cv2.imread('10images/bird4.jpg')
image5 = cv2.imread('10images/bird5.jpg')
image6 = cv2.imread('10images/bird6.jpg')

new_size = (300, 200)

resized_image1 = cv2.resize(image1, dsize=new_size)
resized_image2 = cv2.resize(image2, dsize=new_size)
resized_image3 = cv2.resize(image3, dsize=new_size)
resized_image4 = cv2.resize(image4, dsize=new_size)
resized_image5 = cv2.resize(image5, dsize=new_size)
resized_image6 = cv2.resize(image6, dsize=new_size)

vertical_stacked1 = np.vstack((resized_image1, resized_image2, resized_image3))
vertical_stacked2 = np.vstack((resized_image4, resized_image5, resized_image6))

horizontal_stacked = np.hstack((vertical_stacked1, vertical_stacked2))

combined = cv2.resize(horizontal_stacked, dsize=new_size)

# Save image to disk
cv2.imwrite('combined_image.jpg', combined)

cv2.imshow('image', combined)
cv2.waitKey(0)
cv2.destroyAllWindows()







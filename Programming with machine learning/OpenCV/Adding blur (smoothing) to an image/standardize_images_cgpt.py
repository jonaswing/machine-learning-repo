import os
import cv2
import imutils


image_folder = '10images'
image_list = []

# Get images from image_folder and add to the image_list
for image_name in os.listdir(image_folder):
    image_path = os.path.join(image_folder, image_name)
    image_list.append(image_path)

print(image_list)

# Standardize images
resized_images = []
for image_path in image_list:
    # Read the image
    image = cv2.imread(image_path)

    # Resize the image
    resized_image = imutils.resize(image, width=200)

    # Store the resized image in a list
    resized_images.append(resized_image)

# Display all resized images
for resized_image in resized_images:
    cv2.imshow('Resized Image', resized_image)
    cv2.waitKey(0)

cv2.destroyAllWindows()

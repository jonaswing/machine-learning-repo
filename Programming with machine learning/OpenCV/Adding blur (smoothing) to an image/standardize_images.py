import os
import cv2


image_folder = '10images'
image_list = []

# Get images from image_folder and add to the image_list
for image_name in os.listdir(image_folder):
    image_path = os.path.join(image_folder, image_name)
    image_list.append(image_path)

print(image_list)

# Standardize images
for image in image_list:
    image = cv2.imread(image)
    cv2.resize(image, dsize=(1024, 768))

    cv2.imshow('Image', image)
    cv2.waitKey(0)

cv2.destroyAllWindows()



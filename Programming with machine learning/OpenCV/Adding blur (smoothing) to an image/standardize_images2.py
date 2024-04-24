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
for image_path in image_list:
    image = cv2.imread(image_path)

    if image.shape[0] > image.shape[1]:
        rotated_image = cv2.rotate(image, rotateCode=cv2.ROTATE_90_CLOCKWISE)
        cv2.imshow('Rotated', rotated_image)

    else:
        cv2.imshow('Image', image)

    cv2.waitKey(0)

cv2.destroyAllWindows()
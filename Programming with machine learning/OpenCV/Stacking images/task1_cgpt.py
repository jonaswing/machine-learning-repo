import cv2
import numpy as np
import os

# Function to resize an image to a specific size
def resize_image(image, new_size):
    return cv2.resize(image, new_size)

# Function to create vertical stacks of images
def create_vertical_stack(images):
    return np.vstack(images)

# Function to create horizontal stack of two images
def create_horizontal_stack(image1, image2):
    return np.hstack((image1, image2))

# Function to read all images from a folder
def read_images_from_folder(folder_path):
    images = []
    for filename in os.listdir(folder_path):
        if filename.endswith(('.jpg', '.jpeg', '.png')):  # Add more file extensions if needed
            image_path = os.path.join(folder_path, filename)
            img = cv2.imread(image_path)
            if img is not None:
                images.append(img)
    return images


# Folder path containing your 100 images (replace 'folder_path' with your actual folder path)
folder_path = '10images'
images = read_images_from_folder(folder_path)

# Resize all images to the same size
new_size = (300, 200)
resized_images = [resize_image(img, new_size) for img in images]

# Create vertical stacks (e.g., three images in each stack)
vertical_stacks = [create_vertical_stack(resized_images[i:i+3]) for i in range(0, len(resized_images), 3)]

# Create a single horizontal stack from the vertical stacks
combined_image = create_horizontal_stack(*vertical_stacks)

# Resize the combined image to the same size as one of the original images
final_size = (images[0].shape[1], images[0].shape[0])
final_image = resize_image(combined_image, final_size)

# Save the final image to disk (replace 'output_path' with your desired output file path)
cv2.imwrite('output_path.jpg', final_image)

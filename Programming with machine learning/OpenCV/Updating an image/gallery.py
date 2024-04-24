import cv2
import os
import pandas as pd
from get_file_info import get_file_names, get_file_shapes, get_file_sizes
import random


# Specify folder
folder = '10images'

# Get file names in folder
files = get_file_names(folder)
# Get file shapes in folder
file_shapes = get_file_shapes(folder)
# Get file sizes in folder
file_sizes = get_file_sizes(folder)


# Create DataFrame with file info
file_info = {
    'Name': files,
    'Shape': file_shapes,
    'Size': file_sizes
}
file_info = pd.DataFrame(file_info)
print(file_info)


# Randomly choose an image to display
random_image_name = random.choice(files)

# Construct the full path to the randomly chosen image
random_image_path = os.path.join(folder, random_image_name)

# Read the image
img = cv2.imread(random_image_path)

# Randomly decide whether to display in grayscale or color
if random.choice([True, False]):
    # Convert the image to grayscale
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Display the image
cv2.imshow(random_image_name, img)

# Wait for a key event and close the window
cv2.waitKey(1000)
cv2.destroyAllWindows()








import cv2, os, pandas as pd, random
from get_file_info import get_file_names, get_file_shapes, get_file_sizes

folder = '10images'
files, file_shapes, file_sizes = get_file_names(folder), get_file_shapes(folder), get_file_sizes(folder)

file_info = pd.DataFrame({'Name': files, 'Shape': file_shapes, 'Size': file_sizes})
print(file_info)

random_image_name = random.choice(files)
random_image_path = os.path.join(folder, random_image_name)
img = cv2.imread(random_image_path)

if random.choice([True, False]): img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow(random_image_name, img), cv2.waitKey(1000), cv2.destroyAllWindows()

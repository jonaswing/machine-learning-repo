import os
import cv2


def get_file_names(folder):
    return [f for f in os.listdir(folder) if os.path.isfile(os.path.join(folder, f))]


def get_file_shapes(folder):
    file_names = get_file_names(folder)
    shapes = []
    for file_name in file_names:
        file_path = os.path.join(folder, file_name)
        img = cv2.imread(file_path)
        if img is not None:
            shapes.append(img.shape)
    return shapes


def get_file_sizes(folder):
    file_names = get_file_names(folder)
    sizes = []
    for file_name in file_names:
        file_path = os.path.join(folder, file_name)
        size = os.path.getsize(file_path)
        sizes.append(size)
    return sizes


def get_file(folder):
    file_names = get_file_names(folder)
    sizes = []
    for file_name in file_names:
        file_path = os.path.join(folder, file_name)
        size = os.path.getsize(file_path)
        sizes.append(size)
    return sizes


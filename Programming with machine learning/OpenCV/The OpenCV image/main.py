#Import OpenCV
import cv2

# Using cv2.imread() method to read the file specified.
# When only a file name is specified, it is assumed that the file is in the same folder as the script.
# Alternatively a full path my be provided, e.g. "c:\\Some_Folder\\target.png".
# Adding a zero loads the image as grayscale.
# Credit for this photo:  Photo by Becca Tapert on Unsplash:
# https://unsplash.com/@beccatapert?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText
normal_img = cv2.imread("chatgpticon.png")
grayscale_img = cv2.imread("chatgpticon.png", 0)

# Display the shapes of the two images
print("Normal shape:  ", normal_img.shape)
print("Grayscale shape:  ", grayscale_img.shape)

# Display the number of values in each image
print("Normal values:  ", normal_img.size)
print("Grayscale values:  ", grayscale_img.size)

# Display the type of values stored in each image
print("Normal dtype:  ", normal_img.dtype)
print("Grayscale dtype:  ", grayscale_img.dtype)

print()

# Display the details of the first pixel of each image
print("Normal image first pixel details: ", normal_img[0,0])
print("Grayscale image first pixel details: ", grayscale_img[0,0])
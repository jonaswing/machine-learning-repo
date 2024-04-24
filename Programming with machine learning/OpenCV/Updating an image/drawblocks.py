import cv2

# Specify file path
image_path = '10images/bird1.jpg'
image = cv2.imread(image_path)

print("Image shape:", image.shape)
print("Image size:", image.size)


while input != 'q' or y_value != '':
    block_size_x = input("Specify block size x: ")
    block_size_y = input("Specify block size y: ")
    x_value = input("Specify x value: ")
    y_value = input("Specify y value: ")

    # image[block_size_x:block_size_y,x_value:y_value] = [0,255,0]
    image[1350:1650, 3780:3790] = [0, 255, 0]
    image[1350:1650, 3780:3790] = [0, 255, 0]
    image[1350:1360, 3150:3790] = [0, 255, 0]
    image[1650:1660, 3150:3790] = [0, 255, 0]
    cv2.imwrite("bird1_updated.jpg", image)

    if input == 'q':
        break


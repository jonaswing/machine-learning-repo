from PIL import Image


def display_image_info(image):
    width, height = image.size
    print(f"Image size: {width} x {height}")


def draw_block(image, x, y, block_size, color):
    for i in range(y, y + block_size):
        for j in range(x, x + block_size):
            image.putpixel((j, i), color)


def main():
    # Ask the user for the image file path
    image_path = input("Enter the path of the image file: ")

    # Load the image
    try:
        image = Image.open(image_path)
    except IOError:
        print(f"Error: Unable to open the image file '{image_path}'. Make sure the path is correct.")
        return

    # Display image information
    display_image_info(image)

    while True:
        # Ask the user for block size
        block_size = int(input("Enter the block size in pixels: "))

        # Ask the user for x and y coordinates
        x = int(input("Enter the x (column) value: "))
        y = int(input("Enter the y (row) value: "))

        # Ask the user for color values
        red = int(input("Enter the red channel value (0-255): "))
        green = int(input("Enter the green channel value (0-255): "))
        blue = int(input("Enter the blue channel value (0-255): "))

        # Check if coordinates are within the image boundaries
        if x < 0 or y < 0 or x + block_size > image.width or y + block_size > image.height:
            print("Error: Block goes beyond the image boundaries. Try again.")
            continue

        # Draw the block on the image
        color = (red, green, blue)
        draw_block(image, x, y, block_size, color)

        # Display the updated image
        image.show()

        # Ask the user if they want to continue
        user_input = input("Enter 'q' to quit or any other key to continue: ")
        if user_input.lower() == 'q':
            break

    # Save the final image
    final_path = input("Enter the path to save the final image: ")
    image.save(final_path)
    print(f"Image saved at {final_path}")


if __name__ == "__main__":
    main()

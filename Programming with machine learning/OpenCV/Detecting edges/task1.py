import cv2


image = cv2.imread('bird4.jpg')

# Convert image to greyscale
grey_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply noise reduction
blurred_image = cv2.GaussianBlur(grey_image, (3,3), 0)

# Apply the Canny edge detector to this image at six different thresholds
canny1 = cv2.Canny(grey_image, 100, 200)
cv2.imshow('canny1', canny1)
cv2.waitKey(0)

canny_with_noise_reduction = cv2.Canny(blurred_image, 50, 200)
cv2.imshow('canny_with_noise_reduction', canny_with_noise_reduction)
cv2.waitKey(0)

canny2 = cv2.Canny(grey_image, 50, 200)
cv2.imshow('canny2', canny2)
cv2.waitKey(0)

canny3 = cv2.Canny(grey_image, 200, 300)
cv2.imshow('canny3', canny3)
cv2.waitKey(0)

canny4 = cv2.Canny(grey_image, 300, 400)
cv2.imshow('canny4', canny4)
cv2.waitKey(0)

canny5 = cv2.Canny(grey_image, 100, 300)
cv2.imshow('canny5', canny5)
cv2.waitKey(0)

canny6 = cv2.Canny(grey_image, 300, 100)
cv2.imshow('canny6', canny6)
cv2.waitKey(0)


# Save best image to disk
cv2.imwrite('best_looking_edge_image.jpg', canny_with_noise_reduction)


cv2.destroyAllWindows()

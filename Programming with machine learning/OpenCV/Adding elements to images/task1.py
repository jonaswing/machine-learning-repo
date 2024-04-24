import cv2

img = cv2.imread('bird4.jpg')

print(img.shape)

img_drawn = cv2.line(img, (120, 10), (120, 60), (255,0,0), 2)
img_drawn = cv2.line(img_drawn, (180, 10), (180, 60), (0,255,0), 2)
img_drawn = cv2.line(img_drawn, (120, 10), (180, 10), (0,0,255), 2)
img_drawn = cv2.line(img_drawn, (120, 60), (180, 60), (0,255,255), 2)

cv2.imshow('Drawn', img_drawn)
cv2.waitKey(0)
cv2.destroyAllWindows()

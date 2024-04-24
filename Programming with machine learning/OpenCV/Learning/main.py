import cv2

img = cv2.imread("bird9.jpg")

print(img.shape)

cv2.circle(img, (300, 300), 200, (200, 10, 192), 0)

cv2.imshow("Best cat in the world.", img)



cv2.waitKey(0)
cv2.destroyAllWindows()
#Import OpenCV
import cv2

# Using cv2.imread() method to read the file specified.
# When only a file name is specified, it is assumed that the file is in the same folder as the script.
# Alternatively a full path may be provided, e.g. "c:\\Some_Folder\\target.png".
# Credit for this photo:  Photo by Becca Tapert on Unsplash:
# https://unsplash.com/@beccatapert?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText
img = cv2.imread("chatgpticon.png")

# Display the image
cv2.imshow('The ChatGPT logo', img)

# Waits for user to press any key
cv2.waitKey(0)

# Closing all open windows
cv2.destroyAllWindows()

# Alternative, will destroy specified window
# cv2.destroyWindow('The ChatGPT logo')


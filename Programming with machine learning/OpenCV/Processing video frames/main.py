import cv2

# Create a video capture object to load the video specified.
# Video by BeThe Observer from Pexels
vid_capture = cv2.VideoCapture('skies.mp4')

# isOpened() will return True while there are still frames.
while (vid_capture.isOpened()):
    # vid_capture.read() methods returns a tuple
    # The first element is a bool indicating if there are any frames left
    # and the second is a frame (an image), if there are frames left to retrieve.
    ret, frame = vid_capture.read()
    # If there are still frames, display it in a window
    if ret == True:
        cv2.imshow('Cloudy sky', frame)
        # Display the frame for a pre-set number of milliseconds and return
        # any keys pressed by the user
        key = cv2.waitKey(20)

        # If the user presses the 'q' key, stop the loop.
        if key == ord('q'):
            break
    else:
        # If there are no frames returned, stop the loop.
        break



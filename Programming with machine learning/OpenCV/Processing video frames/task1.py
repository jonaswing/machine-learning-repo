import cv2


# Access an online web source, such as a CCTV camera feed
vid_capture_web = cv2.VideoCapture("rtsp://wowzaec2demo.streamlock.net/vod/mp4:BigBuckBunny_115k.mp4")

# IsOpened() contains True if the video was successfully loaded.
if vid_capture_web.isOpened() == False:
    print("Error opening the video file")
else:
    # Retrieve and display frame rate information
    fps = vid_capture_web.get(cv2.CAP_PROP_FPS)
    print("Frames per second : ", fps, "FPS")

    # Retrieve and display the number of frames in the video
    frame_count = vid_capture_web.get(cv2.CAP_PROP_FRAME_COUNT)
    print("Frame count: ", frame_count)


# isOpened() will return True while there are still frames.
while (vid_capture_web.isOpened()):
    # vid_capture.read() methods returns a tuple
    # The first element is a bool indicating if there are any frames left
    # and the second is a frame (an image), if there are frames left to retrieve.
    ret, frame = vid_capture_web.read()
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


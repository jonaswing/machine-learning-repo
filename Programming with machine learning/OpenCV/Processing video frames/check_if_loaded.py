import cv2


# Create a video capture object to load the video specified.
# Video by BeThe Observer from Pexels
vid_capture = cv2.VideoCapture('skies.mp4')


# IsOpened() contains True if the video was successfully loaded.
if vid_capture.isOpened() == False:
    print("Error opening the video file")
else:
    # Retrieve and display frame rate information
    fps = vid_capture.get(cv2.CAP_PROP_FPS)
    print("Frames per second : ", fps, "FPS")

    # Retrieve and display the number of frames in the video
    frame_count = vid_capture.get(cv2.CAP_PROP_FRAME_COUNT)
    print("Frame count: ", frame_count)
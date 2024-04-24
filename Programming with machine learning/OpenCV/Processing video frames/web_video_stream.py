import cv2

# Access the default webcam on the system.
vid_capture_cam = cv2.VideoCapture(0)
# Access an online web source, such as a CCTV camera feed
vid_capture_web = cv2.VideoCapture("URL_of_video_stream")
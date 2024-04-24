import cv2

def main():
    video_url = "rtsp://rtspstream:c23e9914844ba0036bcec3dfb6a54cf2@zephyr.rtsp.stream/movie"
    cap = cv2.VideoCapture(video_url)

    if not cap.isOpened():
        print("Error: Could not open video.")
        return

    while True:
        ret, frame = cap.read()

        if not ret:
            print("Error: Failed to grab frame.")
            break

        cv2.imshow("Video", frame)

        key = cv2.waitKey(1)  # Wait for a key event (1 millisecond)

        if key == ord('a'):  # Press 'a' to capture and save a frame
            save_frame(frame, "captured_frame.jpg")

        elif key == ord('x'):  # Press 'x' to exit
            break

    cap.release()
    cv2.destroyAllWindows()

def save_frame(frame, filename):
    cv2.imwrite(filename, frame)
    print(f"Frame saved as {filename}")

if __name__ == "__main__":
    main()

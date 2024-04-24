import cv2
import subprocess

def main():
    video_url = "rtsp://rtspstream:c23e9914844ba0036bcec3dfb6a54cf2@zephyr.rtsp.stream/movie"
    cap = cv2.VideoCapture(video_url)

    if not cap.isOpened():
        print("Error: Could not open video.")
        return

    # Set up FFmpeg to capture audio
    audio_output = "captured_audio.wav"
    audio_command = [
        r"C:\Users\jwing\OneDrive\Dokumenter\ffmpeg-N-113412-g0b8e51b584-win64-gpl",  # Specify the full path to ffmpeg
        "-i", video_url,
        "-vn",  # Disable video recording
        "-acodec", "pcm_s16le",
        "-ar", "44100",
        "-ac", "2",
        audio_output
    ]

    audio_process = subprocess.Popen(audio_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

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

    # Wait for the audio process to finish
    audio_process.wait()
    print(f"Audio saved as {audio_output}")

def save_frame(frame, filename):
    cv2.imwrite(filename, frame)
    print(f"Frame saved as {filename}")

if __name__ == "__main__":
    main()

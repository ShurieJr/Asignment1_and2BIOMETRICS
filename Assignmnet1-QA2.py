import cv2
def capture_and_save_video(output_filename='shuuriye.avi', fps=30.0, camera_index=0):
    # Create a VideoCapture object
    cap = cv2.VideoCapture(camera_index)
    # Check if camera opened successfully
    if not cap.isOpened():
        print("Error: Could not open camera.")
        return

    # Get frame dimensions from camera
    frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter(output_filename, fourcc, fps, (frame_width, frame_height))

    print("Recording started. Press 'q' to stop...")

    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()
        if not ret:
            print("Error: Can't receive frame. Exiting...")
            break

        # Display the resulting frame
        cv2.imshow('Camera Feed', frame)

        # Write the frame to the output file
        out.write(frame)
        # Break the loop on 'q' key press
        if cv2.waitKey(1) == ord('q'):
            break
    # Release everything when done
    cap.release()
    out.release()
    cv2.destroyAllWindows()
    print(f"Video saved as {output_filename}")

if __name__ == "__main__":
    capture_and_save_video(output_filename='shuuriye.avi', fps=20.0)
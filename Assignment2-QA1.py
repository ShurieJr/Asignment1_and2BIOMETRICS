import cv2
def crop_and_save_object(input_path, output_path):
    # Read
    image = cv2.imread(input_path)
    if image is None:
        print(f"Error: Could not read image from {input_path}")
        return
    # Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    # Detect faces
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    if len(faces) == 0:
        print("No faces detected. Please try with a different image or method.")
        return
    #  first detected face
    (x, y, w, h) = faces[0]

    # Crop the face region
    cropped_object = image[y:y + h, x:x + w]
    # Display the cropped object
    cv2.imshow("Cropped Object", cropped_object)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # Save the cropped object to a new file
    cv2.imwrite(output_path, cropped_object)
    print(f"Cropped object saved to {output_path}")


# Example usage
input_image = "img.png"  # Replace with your image path
output_image = "cropped_face.png"
crop_and_save_object(input_image, output_image)
import cv2

def process_image(input_path, output_path):
    # Read the image
    img = cv2.imread(input_path)
    # Checking
    if img is None:
        print(f"Error: Could not read image from {input_path}")
        return False

    # show the image
    cv2.imshow('Image Preview', img)

    print("Press any key to continue...")
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # Save the image
    success = cv2.imwrite(output_path, img)

    if success:
        print(f"Image successfully saved to {output_path}")
        return True
    else:
        print(f"Error: Failed to save image to {output_path}")
        return False

if __name__ == "__main__":
    input_file = "OIP.jpg"
    output_file = "D://copy.jpg"
    process_image(input_file, output_file)
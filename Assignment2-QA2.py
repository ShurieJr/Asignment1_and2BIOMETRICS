import cv2
import numpy as np

def process_image(input_path):
    # Read the input image
    img = cv2.imread(input_path)
    if img is None:
        print(f"Error: Could not read image from {input_path}")
        return

    # Display original image
    cv2.imshow('Original Image', img)
    cv2.waitKey(0)

    # 1. Resize the image (scale to half size)
    resized_img = cv2.resize(img, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_LINEAR)
    cv2.imshow('Resized Image (50%)', resized_img)
    cv2.waitKey(0)
    cv2.imwrite('resized_image.jpg', resized_img)

    # 2. Flip the image horizontally
    flipped_img = cv2.flip(img, 1)  # 1 for horizontal, 0 for vertical, -1 for both
    cv2.imshow('Flipped Image (Horizontal)', flipped_img)
    cv2.waitKey(0)
    cv2.imwrite('flipped_image.jpg', flipped_img)

    # 3. Rotate the image by 45 degrees
    (h, w) = img.shape[:2]
    center = (w // 2, h // 2)
    rotation_matrix = cv2.getRotationMatrix2D(center, 45, 1.0)  # 45 degree rotation
    rotated_img = cv2.warpAffine(img, rotation_matrix, (w, h))
    cv2.imshow('Rotated Image (45 degrees)', rotated_img)
    cv2.waitKey(0)
    cv2.imwrite('rotated_image.jpg', rotated_img)

    # 4. Shift/translate the image (move 100px right and 50px down)
    translation_matrix = np.float32([[1, 0, 100], [0, 1, 50]])
    shifted_img = cv2.warpAffine(img, translation_matrix, (w, h))
    cv2.imshow('Shifted Image', shifted_img)
    cv2.waitKey(0)
    cv2.imwrite('shifted_image.jpg', shifted_img)

    # 5. Affine transformation (skew the image)
    # Define 3 points on original image and their new locations
    pts1 = np.float32([[50, 50], [200, 50], [50, 200]])
    pts2 = np.float32([[10, 100], [200, 50], [100, 250]])
    affine_matrix = cv2.getAffineTransform(pts1, pts2)
    affine_img = cv2.warpAffine(img, affine_matrix, (w, h))
    cv2.imshow('Affine Transformed Image', affine_img)
    cv2.waitKey(0)
    cv2.imwrite('affine_image.jpg', affine_img)

    cv2.destroyAllWindows()
    print("All processed images saved successfully!")

if __name__ == "__main__":
    input_image = "shuuriye.jpg"
    process_image(input_image)
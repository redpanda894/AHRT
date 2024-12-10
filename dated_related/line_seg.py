from pdf2image import convert_from_path
import cv2
import pytesseract
import os
import numpy as np

# Paths
input_image_path = os.path.expanduser("~/workspaces/staff/pbrotela/uni/semester5/ece528/Project/AHRT/image.png")
output_folder = os.path.expanduser("~/workspaces/staff/pbrotela/uni/semester5/ece528/Project/AHRT/line_images_2")
os.makedirs(output_folder, exist_ok=True)


# Function to preprocess the image
def preprocess_image(image_path):
    # Load the image
    img = cv2.imread(image_path)
    if img is None:
        raise FileNotFoundError(f"Image at {image_path} could not be loaded. Check the file path.")

    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Apply binary thresholding
    _, binary = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY_INV)

    # Save binary image for debugging
    debug_binary_path = os.path.join(output_folder, "debug_binary.png")
    cv2.imwrite(debug_binary_path, binary)
    print(f"Binary threshold image saved for debugging: {debug_binary_path}")

    return img, binary

# Function to segment rows using contours
def segment_rows(binary, original_image, padding=5):
    # Find contours in the binary image
    contours, _ = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Filter and sort contours by their vertical position (top-to-bottom)
    row_contours = []
    for contour in contours:
        x, y, w, h = cv2.boundingRect(contour)
        if 10 < h < 300:  # Ignore very small or very large "rows" (likely noise or full sheet)
            row_contours.append((x, y, w, h))
    row_contours = sorted(row_contours, key=lambda c: c[1])  # Sort by vertical position (y-coordinate)

    # Crop rows based on contours
    row_images = []
    last_y_end = -1  # Track the last processed row to avoid overlaps
    for idx, (x, y, w, h) in enumerate(row_contours):
        if y < last_y_end:
            continue  # Skip overlapping rows to avoid duplicates

        # Add small padding above and below each row
        y_start = max(0, y - padding)
        y_end = min(original_image.shape[0], y + h + padding)
        row_image = original_image[y_start:y_end, :]  # Crop the full width of the image
        row_images.append((row_image, (x, y, w, h)))  # Store row image and bounding box

        # Save each row as an image
        row_path = os.path.join(output_folder, f"row_{idx + 1}.png")
        cv2.imwrite(row_path, row_image)
        print(f"Saved row image: {row_path}")

        last_y_end = y_end  # Update the end of the last row processed

    if not row_images:
        print("No rows detected. Ensure the input image is clear and properly preprocessed.")
    
    return row_images, row_contours

# Debug function to draw bounding boxes on the original image
def debug_draw_row_boundaries(image, row_contours, padding=5):
    debug_img = image.copy()
    for (x, y, w, h) in row_contours:
        y_start = max(0, y - padding)
        y_end = min(image.shape[0], y + h + padding)
        cv2.rectangle(debug_img, (0, y_start), (image.shape[1], y_end), (0, 255, 0), 2)
    debug_img_path = os.path.join(output_folder, "debug_rows.png")
    cv2.imwrite(debug_img_path, debug_img)
    print(f"Debug image with row boundaries saved: {debug_img_path}")

# Main function
def main():
    print("Loading and preprocessing the image...")
    try:
        original_image, binary_image = preprocess_image(input_image_path)
    except FileNotFoundError as e:
        print(e)
        return

    print("Detecting and segmenting rows...")
    row_images_and_contours, row_contours = segment_rows(binary_image, original_image, padding=5)

    if not row_images_and_contours:
        print("No rows detected. Check debug outputs.")
        return

    print("Creating debug visualization...")
    debug_draw_row_boundaries(original_image, row_contours)

    print(f"Row segments saved in: {output_folder}")

if __name__ == "__main__":
    main()
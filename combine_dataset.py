import os
form PIL import Image
import argparse
import json

def conversion_jpg(directory):
    pass

def convert_images_to_jpg(directory):
    if not os.path.exists(directory):
        print(f"Directory {directory} does not exist.")
        return
    for root,_ , files in os.walk(directory):
        for file in files:
            if file.endswith(".png") || file.endswith(".tif"):
                file_path = os.path.join(root, file)
                try:
                    with Image.open(file_path) as img:
                        # Convert image to RGB (required for saving as JPG)
                        img = img.convert('RGB')
                        
                        # Prepare output file path with .jpg extension, maintaining directory structure
                        relative_path = os.path.relpath(root, directory)
                        base_name = os.path.splitext(filename)[0]
                        # Add top-level directory name (e.g., Generic, Belleville) as prefix to base name
                        top_level_dir = relative_path.split(os.sep)[0] if os.sep in relative_path else relative_path
                        output_filename = f"{top_level_dir}_{base_name}.jpg"

                        output_subdir = os.path.join(output_directory, relative_path)
                        if not os.path.exists(output_subdir):
                            os.makedirs(output_subdir)
                        output_file_path = os.path.join(output_subdir, output_filename)
                        
                        # Save the image as JPG
                        img.save(output_file_path, "JPEG")
                        print(f"Converted: {filename} to {output_file_path}")
                except Exception as e:
                    print(f"Failed to convert {filename}: {e}")

def convert_references_to_jpg(directory):
    if not os.path.exists(directory):
        print(f"Directory {directory} does not exist.")
        return
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".json"):
                file_path = os.path.join(root, file)
                try:
                    with open(file_path, "r") as f:
                        data = json.load(f)
                        ground_truth = data.get("ground_truth")
                        if ground_truth:
                            for dataset_type in ["training", "test", "valid"]:
                                if dataset_type in ground_truth:
                                    images = ground_truth[dataset_type].get("images", {})
                                    updated_images = {}
                                    for image_name, text in images.items():
                                        # Add top-level directory name as prefix to image names
                                        relative_path = os.path.relpath(root, directory)
                                        top_level_dir = relative_path.split(os.sep)[0] if os.sep in relative_path else relative_path
                                        new_image_name = f"{top_level_dir}_{image_name.replace('.png', '.jpg').replace('.tif', '.jpg')}"
                                        updated_images[new_image_name] = text
                                    ground_truth[dataset_type]["images"] = updated_images
                    
                    # Write the updated JSON back to the file
                    with open(file_path, "w") as f:
                        json.dump(data, f, indent=4)
                        print(f"Updated JSON file: {file_path}")
                except Exception as e:
                    print(f"Failed to process {file_path}: {e}")    if not os.path.exists(directory):


def main():
    parser = argparse.ArgumentParser(description="Script to convert images to jpg format.")
    parser.add_argument('-d', '--directory', type=str, required=True, help='Directory containing the data sets')
    parser.add_argument('-o', '--output', type=str, required=True, help='Output directory for the converted images')
    
    args = parser.parse_args()

if __name__ == "__main__":
    main()

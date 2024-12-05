import os
from PIL import Image
import argparse
import json
import shutil

def convert_images_to_jpg(directory, output_directory):
    if not os.path.exists(directory):
        print(f"Directory {directory} does not exist.")
        return
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".png") or file.endswith(".tif"):
                file_path = os.path.join(root, file)
                try:
                    with Image.open(file_path) as img:
                        # Convert image to RGB (required for saving as JPG)
                        img = img.convert('RGB')
                        
                        # Prepare output file path with .jpg extension, maintaining directory structure
                        relative_path = os.path.relpath(root, directory)
                        base_name = os.path.splitext(file)[0]
                        # Add top-level directory name (e.g., Generic, Belleville) as prefix to base name
                        top_level_dir = relative_path.split(os.sep)[0] if os.sep in relative_path else relative_path
                        output_filename = f"{top_level_dir}_{base_name}.jpg"

                        output_subdir = os.path.join(output_directory, relative_path)
                        if not os.path.exists(output_subdir):
                            os.makedirs(output_subdir)
                        output_file_path = os.path.join(output_subdir, output_filename)
                        
                        # Save the image as JPG
                        img.save(output_file_path, "JPEG")
                        print(f"Converted: {file} to {output_file_path}")
                except Exception as e:
                    print(f"Failed to convert {file}: {e}")


import os
import json
import shutil

def convert_references_to_jpg(directory, output_directory):
    if not os.path.exists(directory):
        print(f"Directory {directory} does not exist.")
        return

    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".json"):
                file_path = os.path.join(root, file)
                try:
                    # Determine the top-level directory name
                    relative_path = os.path.relpath(root, directory)
                    top_level_dir = relative_path.split(os.sep)[0] if os.sep in relative_path else relative_path
                    
                    with open(file_path, "r", encoding="utf-8") as f:
                        data = json.load(f)
                        ground_truth = data.get("ground_truth", {})
                        
                        # Process each dataset type in "ground_truth"
                        for dataset_type in ["train", "valid", "test"]:
                            if dataset_type in ground_truth:
                                images = ground_truth[dataset_type]
                                updated_images = {}
                                
                                # Change file extensions to .jpg and prepend the top-level directory
                                for image_name, text_data in images.items():
                                    new_image_name = f"{top_level_dir}_{image_name.replace('.png', '.jpg').replace('.tif', '.jpg')}"
                                    updated_images[new_image_name] = text_data
                                
                                # Update the ground_truth dataset
                                ground_truth[dataset_type] = updated_images
                    
                    # Write the updated JSON back to a new file called altered_labels.json in the same directory
                    altered_file_path = os.path.join(root, "altered_labels.json")
                    with open(altered_file_path, "w", encoding="utf-8") as f:
                        json.dump(data, f, indent=4, ensure_ascii=False)
                        print(f"Created altered JSON file: {altered_file_path}")
                    
                    # Copy the altered JSON file to the output directory with the same relative path
                    output_subdir = os.path.join(output_directory, os.path.relpath(root, directory))
                    if not os.path.exists(output_subdir):
                        os.makedirs(output_subdir)
                    shutil.copy(altered_file_path, os.path.join(output_subdir, "altered_labels.json"))
                    print(f"Copied altered JSON file to: {os.path.join(output_subdir, 'altered_labels.json')}")
                
                except Exception as e:
                    print(f"Failed to process {file_path}: {e}")

def convert_references_to_jpg(directory, output_directory):
    if not os.path.exists(directory):
        print(f"Directory {directory} does not exist.")
        return

    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".json"):
                file_path = os.path.join(root, file)
                print(f"Processing file: {file_path}")  # Debug statement
                try:
                    # Determine the top-level directory name
                    relative_path = os.path.relpath(root, directory)
                    top_level_dir = relative_path.split(os.sep)[0] if os.sep in relative_path else relative_path
                    print(f"Top-level directory: {top_level_dir}")  # Debug statement
                    
                    # Load JSON data
                    with open(file_path, "r", encoding="utf-8") as f:
                        data = json.load(f)
                        ground_truth = data.get("ground_truth", {})
                        
                        # Process each dataset type in "ground_truth"
                        for dataset_type in ["train", "valid", "test"]:
                            if dataset_type in ground_truth:
                                images = ground_truth[dataset_type]
                                updated_images = {}
                                
                                # Change file extensions to .jpg and prepend the top-level directory
                                for image_name, text_data in images.items():
                                    new_image_name = f"{top_level_dir}_{image_name.replace('.png', '.jpg').replace('.tif', '.jpg')}"
                                    updated_images[new_image_name] = text_data
                                    print(f"Renaming: {image_name} -> {new_image_name}")  # Debug statement
                                
                                # Update the ground_truth dataset
                                ground_truth[dataset_type] = updated_images
                    
                    # Save the altered JSON directly to the output directory
                    output_subdir = os.path.join(output_directory, os.path.relpath(root, directory))
                    if not os.path.exists(output_subdir):
                        os.makedirs(output_subdir)
                    altered_file_path = os.path.join(output_subdir, "altered_labels.json")
                    
                    with open(altered_file_path, "w", encoding="utf-8") as f:
                        json.dump(data, f, indent=4, ensure_ascii=False)
                        print(f"Created altered JSON file: {altered_file_path}")
                
                except Exception as e:
                    print(f"Failed to process {file_path}: {e}")


def common_json_union(directory, output_file):
    combined_data = {}
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".json"):
                file_path = os.path.join(root, file)
                try:
                    with open(file_path, "r") as f:
                        data = json.load(f)
                        for key, value in data.items():
                            if key not in combined_data:
                                combined_data[key] = value
                            else:
                                # Merge dictionaries
                                if isinstance(value, dict):
                                    for sub_key, sub_value in value.items():
                                        if sub_key not in combined_data[key]:
                                            combined_data[key][sub_key] = sub_value
                                        else:
                                            combined_data[key][sub_key].update(sub_value)
                                elif isinstance(value, list):
                                    if key not in combined_data:
                                        combined_data[key] = value
                                    else:
                                        combined_data[key] = list(set(combined_data[key] + value))
                except Exception as e:
                    print(f"Failed to process {file_path}: {e}")
    
    # Write the combined JSON to the output file
    try:
        with open(output_file, "w") as f:
            json.dump(combined_data, f, indent=4)
            print(f"Created combined JSON file: {output_file}")
    except Exception as e:
        print(f"Failed to write combined JSON file: {e}")

def main():
    parser = argparse.ArgumentParser(description="Script to convert images to jpg format.")
    parser.add_argument('-d', '--directory', type=str, required=True, help='Directory containing the data sets')
    parser.add_argument('-o', '--output', type=str, required=True, help='Output directory for the converted images')
    parser.add_argument('-u', '--union', action='store_true', help='Create a union of all JSON files in the directory')
    parser.add_argument('-of', '--output_file', type=str, help='Output file for the combined JSON')
    
    args = parser.parse_args()

    if args.union:
        if not args.output_file:
            print("Output file must be specified when using --union option.")
            return
        common_json_union(args.directory, args.output_file)
    else:
        convert_images_to_jpg(args.directory, args.output)
        convert_references_to_jpg(args.directory, args.output)

if __name__ == "__main__":
    main()

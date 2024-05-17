from PIL import Image
import os

def convert_webp_to_png(source_folder, destination_folder):
    # Ensure destination folder exists
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    # Loop through all files in the source folder
    for filename in os.listdir(source_folder):
        if filename.endswith(".webp"):
            # Open the WebP image file
            with Image.open(os.path.join(source_folder, filename)) as img:
                # Define the new filename, replacing the file extension
                new_filename = os.path.splitext(filename)[0] + ".png"
                
                # Convert and save the image as PNG
                img.convert('RGB').save(os.path.join(destination_folder, new_filename), "PNG")
                
                print(f"Converted {filename} to {new_filename}")

# Usage example
source_folder = './source'
destination_folder = './dest'
convert_webp_to_png(source_folder, destination_folder)

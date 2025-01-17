from rembg import remove
from PIL import Image
import sys
import os


def removebg(inputPath):
    # Get the file extension
    file_extension = os.path.splitext(inputPath)[1][1:].lower()

    # Check if the file extension is in the list of accepted file types
    if file_extension not in ['jpg', 'jpeg', 'png']:
        print(f"Warning: Unsupported file type '{file_extension}'. Supported file types are: jpg, jpeg, png.")
        sys.exit(1)

    try:
        originalImage = Image.open(inputPath)
        imageWithoutBg = remove(originalImage)

        # Create the output path by replacing the file extension with ".png"
        outputPath = os.path.splitext(inputPath)[0] + '.png'
        imageWithoutBg.save(outputPath)

        print("Background removed successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    if(len(sys.argv) < 2):
        print("Usage: python removebg.py <input_path>")
        sys.exit(1)

    removebg(sys.argv[1])
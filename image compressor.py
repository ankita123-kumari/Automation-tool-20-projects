from PIL import Image
import os

# Compression settings
INPUT_IMAGE = "camera.jpeg"  # Change this to your image file
OUTPUT_IMAGE = "compressed.jpg"
QUALITY = 100  # Compression level (1-100)

# Function to compress image
def compress_image(input_path, output_path, quality):
    try:
        # Open the image
        img = Image.open(input_path)
        
        # Convert to RGB mode (avoids transparency issues)
        if img.mode in ("RGBA", "P"):
            img = img.convert("RGB")
        
        # Save with compression
        img.save(output_path, "JPEG", quality=quality)
        print(f"Compression successful! Saved as {output_path}")
    
    except Exception as e:
        print(f"Error: {str(e)}")

# Run the function
compress_image(INPUT_IMAGE, OUTPUT_IMAGE, QUALITY)
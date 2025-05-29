import os
import shutil

# Define source folder (where files are stored)
SOURCE_FOLDER = r"C:\Automation tools projects (20)"  # Change to your target folder

# Define file type categories
FILE_CATEGORIES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
    "Documents": [".pdf", ".docx", ".txt", ".pptx", ".xlsx"],
    "Videos": [".mp4", ".avi", ".mov", ".mkv"],
    "Music": [".mp3", ".wav", ".aac", ".flac"],
    "Executables": [".exe", ".bat", ".msi"],
    "Archives": [".zip", ".rar", ".tar", ".gz"],
    "Others": []
}

# Function to organize files
def organize_files(source_folder):
    # Ensure the source folder exists
    if not os.path.exists(source_folder):
        print("Error: Source folder not found!")
        return

    # Iterate through files in the source folder
    for file in os.listdir(source_folder):
        file_path = os.path.join(source_folder, file)

        # Skip folders
        if os.path.isdir(file_path):
            continue
        
        # Determine category
        file_extension = os.path.splitext(file)[1].lower()
        category = "Others"  # Default category

        for folder, extensions in FILE_CATEGORIES.items():
            if file_extension in extensions:
                category = folder
                break

        # Create destination folder if it doesn't exist
        destination_folder = os.path.join(source_folder, category)
        if not os.path.exists(destination_folder):
            os.makedirs(destination_folder)

        # Move the file
        shutil.move(file_path, os.path.join(destination_folder, file))
        print(f"Moved: {file} → {category}")

    print("✅ File organization completed!")

# Run the file organizer
organize_files(SOURCE_FOLDER)
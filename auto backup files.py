import shutil
import os
import datetime

def backup_files(source_dir, backup_dir):
    """Automatically backs up files from source to backup directory."""
    if not os.path.exists(source_dir):
        print("Source directory does not exist!")
        return
    
    # Create a timestamped backup folder
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    backup_path = os.path.join(backup_dir, f"backup_{timestamp}")
    os.makedirs(backup_path, exist_ok=True)

    # Copy files from source to backup
    for file_name in os.listdir(source_dir):
        full_file_name = os.path.join(source_dir, file_name)
        if os.path.isfile(full_file_name):
            shutil.copy(full_file_name, backup_path)
    
    print(f"Backup completed successfully! Files saved in {backup_path}")

# Example Usage
source_directory = "C:/Users/Ankita/Documents/Projects"
backup_directory = "C:/Users/Ankita/Backups"
backup_files(source_directory, backup_directory)
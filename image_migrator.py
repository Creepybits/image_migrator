import os
import shutil

# --- CONFIGURATION - EDIT THESE VALUES ---
# The drive you want to move files FROM
source_drive = 'C:\\'
# The drive you want to move files TO
dest_drive = 'D:\\'

# --- IMPORTANT! REVIEW AND ADD TO THIS EXCLUSION LIST ---
# We have pre-filled this with standard system folders.
# You MUST add your own specific user folders to prevent moving important app data.
# Ensure you replace 'your_username' with your actual Windows username.
exclude_dirs = {
    # Standard System Folders (DO NOT REMOVE)
    os.path.join(source_drive, 'Windows'),
    os.path.join(source_drive, 'Program Files'),
    os.path.join(source_drive, 'Program Files (x86)'),
    os.path.join(source_drive, 'ProgramData'),
    os.path.join(source_drive, 'Users', 'Public'),
    
    # Common User Application Data Folders (REVIEW AND ADD YOURS)
    os.path.join(source_drive, 'Users', 'your_username', 'AppData'),
    os.path.join(source_drive, 'Users', 'your_username', '.vscode'),
    os.path.join(source_drive, 'Users', 'your_username', '.triton'),
    os.path.join(source_drive, 'Users', 'your_username', '.cache'),
    # Add any other folders you want to skip here!
}
# --- END OF CONFIGURATION ---

def is_excluded(path, exclusions):
    """Check if a path or any of its parent directories are in the exclusion list."""
    for ex_dir in exclusions:
        if path.startswith(ex_dir):
            return True
    return False

def migrate_images(source, dest, exclusions):
    """Recursively find image files and move them while preserving directory structure."""
    print(f"Scanning {source}...")
    for root, dirs, files in os.walk(source, topdown=True):
        # Prune excluded directories to avoid walking through them
        dirs[:] = [d for d in dirs if not is_excluded(os.path.join(root, d), exclusions)]
        
        if is_excluded(root, exclusions):
            continue

        for file in files:
            if file.lower().endswith(('.png', '.jpg', '.jpeg', '.webp', '.gif')):
                source_path = os.path.join(root, file)
                
                # Create the destination directory structure
                relative_path = os.path.relpath(root, source)
                dest_dir = os.path.join(dest, relative_path)
                os.makedirs(dest_dir, exist_ok=True)
                
                dest_path = os.path.join(dest_dir, file)
                
                try:
                    print(f"Moving {source_path} to {dest_path}")
                    shutil.move(source_path, dest_path)
                except Exception as e:
                    print(f"Error moving {source_path}: {e}")

if __name__ == "__main__":
    print("--- Image Migration Script ---")
    print("WARNING: This script will move image files from the source to the destination.")
    print(f"Source: {source_drive}")
    print(f"Destination: {dest_drive}")
    
    # Final confirmation from the user
    confirm = input("Have you edited the script configuration and backed up your data? (yes/no): ")
    if confirm.lower() == 'yes':
        migrate_images(source_drive, dest_drive, exclude_dirs)
        print("Migration complete.")
    else:
        print("Migration cancelled. Please configure the script before running.")

from pathlib import Path

# Define file categories with their extensions
CATEGORIES = {
    "Programs": [".exe"],
    "Pictures": [".png", ".jpg", ".jpeg"],
    "Video": [".mp4", ".mkv", ".avi"],
    "Compressed": [".zip", ".rar", ".7z"],
    "Documents": [".pdf", ".doc", ".docx", ".ppt", ".pptx", ".xls", ".xlsx", ".txt"],
    "Music": [".mp3", ".wav"],
    "Programming": [".html", ".css", ".js", ".py", ".java", ".cpp", ".c"],
}

def organize_downloads():
    downloads_path = Path.home() / "Downloads"

    # Ensure all category folders exist
    for category in CATEGORIES.keys():
        (downloads_path / category).mkdir(exist_ok=True)

    # Create 'Others' folder for uncategorized files
    others_path = downloads_path / "Others"
    others_path.mkdir(exist_ok=True)

    # Iterate over files in Downloads
    for file in downloads_path.iterdir():
        if file.is_file():
            # Find the matching category for the file
            destination = next((cat for cat, exts in CATEGORIES.items() if file.suffix.lower() in exts), "Others")
            file.rename(downloads_path / destination / file.name)

    print("Files have been organized successfully!")

if __name__ == "__main__":
    print("Organizing files...")
    organize_downloads()
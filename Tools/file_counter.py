import os

folder = "Audio/audio5_chunks"

# Count only files (ignore subfolders)
counter = sum(
    1 for file in os.listdir(folder)
    if os.path.isfile(os.path.join(folder, file))
)

print(f"Number of files in '{folder}':", counter)

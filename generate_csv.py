import os
import csv

chunk_dir = "Audio/audio5_chunks"             # Folder with .wav chunks
output_csv = "audio5_chunks.csv"                       # CSV will be saved in current directory

# Open the CSV file for writing
with open(output_csv, "w", newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(["chunk_id", "audio_path", "transcription"])  # Header

    # Iterate through all .wav files in the chunk directory
    for file in sorted(os.listdir(chunk_dir)):
        if file.endswith(".wav"):
            chunk_id = file.replace(".wav", "")                             # Strip extension
            audio_path = os.path.join(chunk_dir, file)                      # Full path to audio
            writer.writerow([chunk_id, audio_path, ""])                     # Write row

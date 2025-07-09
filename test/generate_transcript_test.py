import os
import csv

chunk_dir = "test/test_chunks"       # folder where your .wav chunks live
output_dir = "test"                  # output folder 
output_csv = os.path.join(output_dir, "test.csv")  # ✅ save inside test/

with open(output_csv, "w", newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(["chunk_id", "audio_path", "transcription"])

    for file in sorted(os.listdir(chunk_dir)):
        if file.endswith(".wav"):
            chunk_id = file.replace(".wav", "")
            writer.writerow([chunk_id, os.path.join(chunk_dir, file), ""])

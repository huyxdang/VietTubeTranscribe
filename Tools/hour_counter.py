from pydub import AudioSegment
import os

AUDIO_DIR = "Audio/audio5_chunks"
total_duration_ms = 0
file_count = 0

for filename in os.listdir(AUDIO_DIR):
    if filename.lower().endswith(".wav"):
        file_path = os.path.join(AUDIO_DIR, filename)
        try:
            audio = AudioSegment.from_wav(file_path)
            total_duration_ms += len(audio)
            file_count += 1
        except Exception as e:
            print(f"⚠️ Error with {filename}: {e}")

# Convert milliseconds to hours, minutes, seconds
total_seconds = total_duration_ms / 1000
hours = int(total_seconds // 3600)
minutes = int((total_seconds % 3600) // 60)
seconds = int(total_seconds % 60)

print(f"✅ Processed {file_count} audio files.")
print(f"🕒 Total duration: {hours}h {minutes}m {seconds}s ({round(total_seconds/3600, 2)} hours)")

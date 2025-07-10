from pydub import AudioSegment
import os

# Settings
AUDIO_DIR = "Audio/audio5_chunks"
MIN_DURATION_MS = 5000  # 5 seconds

# Sort files in order (important for finding previous chunk)
files = sorted([f for f in os.listdir(AUDIO_DIR) if f.endswith(".wav")])

stitched_count = 0

for i in range(1, len(files)):  # start from 1 because we may modify previous
    current_path = os.path.join(AUDIO_DIR, files[i])
    prev_path = os.path.join(AUDIO_DIR, files[i - 1])

    # Load both current and previous chunks
    try:
        current_audio = AudioSegment.from_wav(current_path)
        if len(current_audio) < MIN_DURATION_MS:
            prev_audio = AudioSegment.from_wav(prev_path)

            # Stitch current to previous
            stitched_audio = prev_audio + current_audio

            # Save over previous file
            prev_name = files[i - 1]
            prev_save_path = os.path.join(AUDIO_DIR, prev_name)
            stitched_audio.export(prev_save_path, format="wav", parameters=["-ar", "16000"])

            # Delete short chunk
            os.remove(current_path)
            stitched_count += 1

    except Exception as e:
        print(f"⚠️ Error processing {files[i]}: {e}")

print(f"✅ Stitched and removed {stitched_count} short chunk(s) (<5s)")

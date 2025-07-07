from pydub import AudioSegment, silence
import os

# Define input & output paths
input_path = "downloads_16kHz/choi game.wav"
output_dir = "segments_trial_16kHz"
os.makedirs(output_dir, exist_ok=True)

# Load audio
audio = AudioSegment.from_wav(input_path)

# Silence detection parameters
min_silence_len = 900          # ms (you can try 500 or 1000)
silence_thresh = audio.dBFS - 14  # adaptive threshold
keep_silence = 250              # pad segments with 250ms of silence

# Segment
chunks = silence.split_on_silence(
    audio,
    min_silence_len=min_silence_len,
    silence_thresh=silence_thresh,
    keep_silence=keep_silence
)

print(f"→ Found {len(chunks)} segments.")

# Save each chunk
for i, chunk in enumerate(chunks):
    out_path = os.path.join(output_dir, f"sorno_{i:03}.wav")
    chunk.export(out_path, format="wav")
    print(f"    Saved: {out_path}")

print("✅ Trial complete.")

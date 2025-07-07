from pydub import AudioSegment, silence
import os
from glob import glob
import statistics

# Input & output folders
INPUT_DIR = "downloads_16kHz"
OUTPUT_DIR = "segments"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Silence detection parameters
MIN_SILENCE_LEN = 900           # ms
SILENCE_THRESH_PAD = 14         # dB
KEEP_SILENCE = 250              # ms

# Track durations
durations_ms = []

# Get all .wav files in the input directory
audio_files = glob(os.path.join(INPUT_DIR, "*.wav"))

for file_index, filepath in enumerate(audio_files):
    filename = os.path.splitext(os.path.basename(filepath))[0]
    print(f"📂 Processing {filename}...")

    try:
        # Load audio
        audio = AudioSegment.from_wav(filepath)
        silence_thresh = audio.dBFS - SILENCE_THRESH_PAD

        # Segment
        chunks = silence.split_on_silence(
            audio,
            min_silence_len=MIN_SILENCE_LEN,
            silence_thresh=silence_thresh,
            keep_silence=KEEP_SILENCE
        )

        print(f"  → Found {len(chunks)} segments.")

        # Save each chunk and record duration
        for i, chunk in enumerate(chunks):
            out_path = os.path.join(OUTPUT_DIR, f"{filename}_clip_{i:03}.wav")
            chunk.export(out_path, format="wav")
            durations_ms.append(len(chunk))  # duration in ms

    except Exception as e:
        print(f"❌ Failed to process {filename}: {e}")

# Summary stats
if durations_ms:
    durations_sec = [d / 1000 for d in durations_ms]
    print("\n📊 Segment Duration Stats (seconds):")
    print(f"  Min:    {min(durations_sec):.2f}")
    print(f"  Max:    {max(durations_sec):.2f}")
    print(f"  Median: {statistics.median(durations_sec):.2f}")
    print(f"  Total segments: {len(durations_sec)}")
else:
    print("⚠️ No segments were created.")

print("\n✅ Done segmenting all files!")

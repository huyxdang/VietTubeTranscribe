from pydub import AudioSegment, silence
import os
from glob import glob

# Input & output folders
INPUT_DIR = "downloads"
OUTPUT_DIR = "segments"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Parameters for silence detection
MIN_SILENCE_LEN = 500         # 500ms of silence
KEEP_SILENCE = 200            # keep 200ms padding at start/end
SILENCE_THRESH_PAD = 16       # dB below average volume

# Get all .wav files in the input directory
audio_files = glob(os.path.join(INPUT_DIR, "*.wav"))

for file_index, filepath in enumerate(audio_files):
    filename = os.path.splitext(os.path.basename(filepath))[0]
    print(f"Processing {filename}...")

    # Load audio
    audio = AudioSegment.from_wav(filepath)

    # Calculate silence threshold relative to average volume
    silence_thresh = audio.dBFS - SILENCE_THRESH_PAD # Subtracting 16 because standard for speech segmentation 

    # Split on silence
    chunks = silence.split_on_silence(
        audio,
        min_silence_len=MIN_SILENCE_LEN,
        silence_thresh=silence_thresh,
        keep_silence=KEEP_SILENCE
    )

    print(f"  → Found {len(chunks)} segments.")

    # Save each chunk
    for i, chunk in enumerate(chunks):
        out_path = os.path.join(
            OUTPUT_DIR,
            f"{filename}_clip_{i:03}.wav"
        )
        chunk.export(out_path, format="wav")

print("✅ Done segmenting all files!")
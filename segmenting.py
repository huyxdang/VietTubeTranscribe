from pydub import AudioSegment  
import os                      

# Define the input/output folders and chunk size
INPUT_DIR = "Audio/audio5_trimmed"     
OUTPUT_DIR = "Audio/audio5_chunks"   
os.makedirs(OUTPUT_DIR, exist_ok = True)
CHUNK_LENGTH_MS = 7000             

def segment_audio(input_wav, chunk_length_ms=CHUNK_LENGTH_MS, output_dir=OUTPUT_DIR):
    """
    Segment a single audio file into fixed-length chunks (default: 7s) and save them.

    Args:
        input_wav (str): Path to the input .wav file
        chunk_length_ms (int): Length of each chunk in milliseconds
        output_dir (str): Directory to save the output chunks
    """
    os.makedirs(output_dir, exist_ok=True)  # Ensure output directory exists

    # Load audio and standardize sample rate to 16kHz
    audio = AudioSegment.from_wav(input_wav)
    audio = audio.set_frame_rate(16000)

    base_name = os.path.splitext(os.path.basename(input_wav))[0]  # Get file name without extension
    total_length = len(audio)

    # Break the audio into chunks
    for i in range(0, total_length, chunk_length_ms):
        chunk = audio[i:i+chunk_length_ms]
        chunk_filename = f"{base_name}_chunk_{i//chunk_length_ms:04d}.wav"
        chunk_path = os.path.join(output_dir, chunk_filename)

        # Export the chunk as a .wav file with 16kHz sampling rate
        chunk.export(chunk_path, format="wav", parameters=["-ar", "16000"])

def segment_all_in_folder(input_dir=INPUT_DIR):
    """
    Segment all .wav files in the given folder.

    Args:
        input_dir (str): Path to the folder containing .wav files
    """
    for filename in os.listdir(input_dir):
        if filename.lower().endswith(".wav"):
            input_path = os.path.join(input_dir, filename)
            segment_audio(input_path)

if __name__ == "__main__":
    segment_all_in_folder()

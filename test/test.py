from pydub import AudioSegment
import os

output_folder = "test/test_clip"
os.makedirs(output_folder, exist_ok = True)

# Load the full .wav file
audio = AudioSegment.from_wav("downloads_16kHz/cam 100 trieu.wav")

# Define 5 minutes in milliseconds
five_minutes = 5 * 60 * 1000  # = 300,000 ms

# Define 90 seconds in milliseconds
start = 115 * 1000 # = 

# Extract the first 5 minutes
first_five = audio[:five_minutes]

# Trim the first 90 seconds
trimmed_five = first_five[start:]

output_path = os.path.join(output_folder, "trimmed_sample.wav")
# Export to a new file
trimmed_five.export(output_path, format="wav", parameters=["-ar", "16000"])

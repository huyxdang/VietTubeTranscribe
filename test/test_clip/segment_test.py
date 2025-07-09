from pydub import AudioSegment
import os

def segment_audio(input_wav, chunk_length_ms=7000, output_dir="test/test_chunks"):
    os.makedirs(output_dir, exist_ok=True)
    audio = AudioSegment.from_wav(input_wav)
    audio = audio.set_frame_rate(16000)  # ✅ Ensure 16kHz

    total_length = len(audio)
    for i in range(0, total_length, chunk_length_ms):
        base_name = os.path.splitext(os.path.basename(input_wav))[0]
        chunk = audio[i:i+chunk_length_ms]
        chunk.export(
        f"{output_dir}/{base_name}_chunk_{i//chunk_length_ms:04d}.wav",
            format="wav",
            parameters=["-ar", "16000"]
        )

if __name__ == "__main__":
    segment_audio("test/test_clip/trimmed_sample.wav")  

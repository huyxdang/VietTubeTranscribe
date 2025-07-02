# 🇻🇳 Vietnamese Speech-to-Text Dataset (Conversational Podcasts)

This is a personal project to build a high-quality Vietnamese speech dataset (~20 hours) by downloading conversational podcast audio from YouTube, segmenting it, and manually transcribing each clip. Inspired by projects like [LJ Speech](https://keithito.com/LJ-Speech-Dataset/), this dataset is intended to support future research in ASR (automatic speech recognition) for low-resource languages.

---

## 📁 Project Structure

viet-speech-dataset/
├── downloads/ # Original downloaded audio (longform .wav)
├── segments/ # Segmented audio clips (short clips for transcription)
├── transcriptions/ # Transcribed clips (JSON/CSV format)
├── app/ # Manual transcription tool (React/Streamlit)
├── youtube_links.txt # List of 24 YouTube podcast URLs
├── batch_download.sh # Script to download and extract audio
└── README.md

---

## 🔧 How It Works

### 1. 🧲 Download Audio
Put your YouTube podcast links (1 per line) in `youtube_links.txt`, then run:

```bash
bash batch_download.sh
This downloads audio-only .wav files into downloads/.

2. ✂️ Segment by Silence
Use a script (e.g., with pydub or ffmpeg) to split long audio files into smaller clips based on silence. Save to segments/.

3. ✍️ Manual Transcription
Use a simple web app to:

Play audio clips

Manually type in transcriptions

Save (audio_path, transcription) pairs to JSON/CSV

4. 📦 Export Dataset
After labeling, export the data in a format like:

json
Copy
Edit
{
  "audio_filepath": "segments/clip_001.wav",
  "transcription": "Em chào các bạn, hôm nay chúng ta sẽ nói về..."
}
🛠 Tools & Stack
yt-dlp — audio download

ffmpeg — audio segmentation

React or Streamlit — transcription tool

Python — data preprocessing scripts

✨ Status
✅ ~20 hours of YouTube podcast downloaded

⏳ Transcription tool in development

📜 License
Currently for research/personal use only. Please contact xhuydng@gmail.com before using for commercial purposes.

🙋‍♂️ Author
Created by Huy Dang – feel free to reach out for collaborations or ideas on low-resource language AI!
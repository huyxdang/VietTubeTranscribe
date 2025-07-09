import os
import pandas as pd
import streamlit as st
import soundfile as sf

# SETTINGS
CSV_PATH = "test/test.csv"
AUDIO_DIR = "test/test_chunks"
SAMPLING_RATE = 16000

# Load CSV
df = pd.read_csv(CSV_PATH)

# Track progress with Streamlit session state
if "index" not in st.session_state:
    st.session_state.index = 0

# Display controls
st.title("📝 Manual Transcription Interface")

# Navigation
col1, col2 = st.columns(2)
with col1:
    if st.button("⬅️ Back") and st.session_state.index > 0:
        st.session_state.index -= 1
with col2:
    if st.button("➡️ Next") and st.session_state.index < len(df) - 1:
        st.session_state.index += 1

row = df.iloc[st.session_state.index]

st.markdown(f"### Chunk {st.session_state.index + 1} / {len(df)}")
st.audio(row["audio_path"], format="audio/wav", start_time=0)

# Input transcription
new_text = st.text_area("✍️ Your transcription:", value=row["transcription"] or "", height=150)

# Save button
if st.button("💾 Save transcription"):
    df.at[st.session_state.index, "transcription"] = new_text
    df.to_csv(CSV_PATH, index=False)
    st.success("Saved!")

# Optional: show filename
st.caption(f"📄 File: {row['audio_path']}")

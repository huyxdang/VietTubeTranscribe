import os
import pandas as pd
import streamlit as st

# SETTINGS
CSV_PATH = "audio5_chunks.csv"
SAMPLING_RATE = 16000

# Load CSV
@st.cache_data
def load_data():
    return pd.read_csv(CSV_PATH)

df = load_data()

# Track progress using session state
if "index" not in st.session_state:
    st.session_state.index = 0

# Handle empty DataFrame case
if len(df) == 0:
    st.warning("✅ All audio clips have been reviewed or deleted.")
    st.stop()

# Ensure index is valid
st.session_state.index = min(st.session_state.index, len(df) - 1)
row = df.iloc[st.session_state.index]

# --- UI Header ---
st.title("📝 Manual Transcription Interface")
st.markdown(f"### Clip {st.session_state.index + 1} of {len(df)}")

# --- Audio playback ---
st.audio(row["audio_path"], format="audio/wav", start_time=0)

# --- Navigation ---
col1, col2, col3 = st.columns([1, 1, 1])
with col1:
    if st.button("⬅️ Back") and st.session_state.index > 0:
        st.session_state.index -= 1
        st.experimental_rerun()

with col2:
    if st.button("➡️ Next") and st.session_state.index < len(df) - 1:
        st.session_state.index += 1
        st.experimental_rerun()

with col3:
    if st.button("🗑️ Delete"):
        try:
            os.remove(row["audio_path"])  # delete audio file
        except Exception as e:
            st.error(f"Error deleting file: {e}")

        df = df.drop(index=row.name).reset_index(drop=True)  # remove from df
        df.to_csv(CSV_PATH, index=False)
        st.session_state.index = min(st.session_state.index, len(df) - 1)
        st.success("Deleted.")
        st.experimental_rerun()

# --- Transcription input ---
new_text = st.text_area("✍️ Your transcription:", value=row["transcription"] or "", height=150)

if st.button("💾 Save transcription"):
    df.at[st.session_state.index, "transcription"] = new_text
    df.to_csv(CSV_PATH, index=False)
    st.success("Saved!")

# --- Optional file display ---
st.caption(f"📄 File: {row['audio_path']}")

import streamlit as st
import speech_recognition as sr
import tempfile
import os
from utils import LANGUAGES, convert_to_wav
from translate import show_translation_ui, LANGUAGES as TRANSLATE_LANGUAGES  # Import from translate.py

def speech_to_text(audio_source, audio_file, stt_lang):
    """
    Handles the speech-to-text functionality.

    Args:
        audio_source (str): The source of the audio ("Microphone" or "Upload Audio File").
        audio_file (streamlit.UploadedFile): The uploaded audio file (if applicable).
        stt_lang (str): The selected language for speech recognition.

    Returns:
        str: The recognized text, or None on error.
    """
    recognizer = sr.Recognizer()
    text = ""

    if audio_source == "Upload Audio File":
        if audio_file is not None:
            try:
                with tempfile.NamedTemporaryFile(delete=False, suffix=os.path.splitext(audio_file.name)[1]) as input_tmp:
                    input_tmp.write(audio_file.getbuffer())
                    input_path = input_tmp.name

                wav_path = tempfile.mktemp(suffix=".wav")

                if not input_path.lower().endswith('.wav'):
                    if convert_to_wav(input_path, wav_path):
                        st.success("✅ Audio file converted to WAV format")
                    else:
                        st.error("❌ Failed to convert audio to WAV")
                        os.unlink(input_path)
                        return None
                else:
                    wav_path = input_path

                with sr.AudioFile(wav_path) as source:
                    audio = recognizer.record(source)
                st.success("✅ Audio file loaded. Processing...")

            except Exception as e:
                st.error(f"❌ Error processing audio file: {e}")
                if 'input_path' in locals() and os.path.exists(input_path):
                    os.unlink(input_path)
                if 'wav_path' in locals() and os.path.exists(wav_path) and wav_path != input_path:
                    os.unlink(wav_path)
                return None
        else:
            st.warning("⚠️ Please upload an audio file first")
            return None

    else:  # Microphone input
        with sr.Microphone() as source:
            st.info("🎧 Listening... Speak now")
            try:
                audio = recognizer.listen(source, timeout=10)
                st.success("✅ Audio captured. Processing...")
            except sr.WaitTimeoutError:
                st.warning("⚠️ No speech detected within the timeout.")
                return None

    # Recognize speech
    try:
        text = recognizer.recognize_google(audio, language=LANGUAGES[stt_lang])
        return text
    except sr.UnknownValueError:
        st.error("🔇 Could not understand the audio")
        return None
    except sr.RequestError as e:
        st.error(f"⚠️ Could not request results; {e}")
        return None
    except Exception as e:
        st.error(f"❌ An error occurred during recognition: {e}")
        return None
    finally:
        # Clean up temporary files
        if audio_source == "Upload Audio File":
            if 'input_path' in locals() and os.path.exists(input_path):
                os.unlink(input_path)
            if 'wav_path' in locals() and os.path.exists(wav_path) and wav_path != input_path:
                os.unlink(wav_path)
    return None

# ... (keep all your existing imports and functions until speech_to_text_tab)

def speech_to_text_tab():
    """Handles speech-to-text tab with persistent state"""
    st.markdown("""
    <div class="tab-content" id="speech-to-text-content">
        <h2 class="section-title">Speech Recognition</h2>
    </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns([1, 1], gap="large")

    with col1:
        stt_lang = st.selectbox(
            "Select spoken language:",
            options=list(LANGUAGES.keys()),
            index=list(LANGUAGES.keys()).index("English"),
            key="stt_lang"
        )

        audio_source = st.radio(
            "Audio source:",
            ("Microphone", "Upload Audio File"),
            horizontal=True,
            key="audio_source"
        )

        audio_file = None
        if audio_source == "Upload Audio File":
            audio_file = st.file_uploader(
                "Upload an audio file",
                type=["wav", "mp3", "ogg", "flac", "aac", "m4a"],
                key="audio_uploader"
            )

    with col2:
        # Store recognized text in session state
        if 'recognized_text' not in st.session_state:
            st.session_state.recognized_text = None
        
        if st.button("🎤 Start Speech to Text", key="stt_button"):
            text = speech_to_text(audio_source, audio_file, stt_lang)
            if text:
                st.session_state.recognized_text = text
        
        # Display results if text exists in session state
        if st.session_state.recognized_text:
            st.markdown(f"""
            <div class="result-box">
                <p>{st.session_state.recognized_text}</p>
            </div>
            """, unsafe_allow_html=True)

            # Download option
            st.download_button(
                label="📥 Download as Text",
                data=st.session_state.recognized_text,
                file_name="speech_to_text.txt",
                mime="text/plain",
                key="stt_download"
            )

            # Call translation UI with the persisted text
            show_translation_ui(st.session_state.recognized_text, stt_lang)
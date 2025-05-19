# SpeakEasy: Speech to Text / Text to Speech Conversion

## Overview

SpeakEasy is a Streamlit-based application that provides a user-friendly interface for both Speech-to-Text (STT) and Text-to-Speech (TTS) conversion.  It allows users to either transcribe spoken language from microphone input or uploaded audio files, and synthesize speech from text input in various languages and voice options.  Additionally, it offers translation capabilities for the transcribed text.

## Features

* **Speech-to-Text (STT):**
    * Supports transcribing speech from microphone input.
    * Allows uploading audio files in multiple formats (`wav`, `mp3`, `ogg`, `flac`, `aac`, `m4a`).
    * Converts uploaded files to WAV format for processing.
    * Supports a selection of multiple languages for speech recognition.
    * Displays transcribed text.
    * Offers the option to download the transcribed text as a `.txt` file.
    * Integrates with the translation feature to translate the transcribed text.
* **Text-to-Speech (TTS):**
    * Synthesizes speech from user-provided text.
    * Supports multiple languages for speech synthesis.
    * Allows users to select the gender (Male or Female) of the voice.
    * Provides a slider to adjust the speech rate.
    * Offers both local (pyttsx3) and online (gTTS) text-to-speech engines.
    * Provides visual feedback during speech synthesis and playback.
    * Enables downloading the synthesized audio as an `.mp3` file.
* **Translation:**
    * Leverages the Gemini API to translate transcribed text into a user-selected target language.
    * Provides a user interface to select the target language.
    * Displays the translated text.
* **User Interface:**
    * Clean and modern design using custom CSS.
    * Responsive layout for different screen sizes.
    * Intuitive navigation between STT and TTS functionalities.
    * Clear visual cues and animations to enhance the user experience.

## Files Description

* `main.py`:  The main entry point of the Streamlit application. It sets up the UI, navigation between the Speech-to-Text and Text-to-Speech tabs, and handles overall application flow.
* `speech_to_text.py`:  Contains the logic for the Speech-to-Text functionality. It uses the `speech_recognition` library to transcribe audio, handles audio file uploads and microphone input, and provides the user interface for the STT tab.
* `text_to_speech.py`:  Implements the Text-to-Speech functionality. It uses the `pyttsx3` and `gTTS` libraries to synthesize speech from text, manages voice selection and speech rate, and provides the UI for the TTS tab.
* `translate.py`:  Handles the translation of text using the Gemini API.  It defines the language options and provides the translation UI.
* `utils.py`:  Contains utility functions, such as `convert_to_wav()` for converting audio files to WAV format, and a dictionary (`LANGUAGES`) that maps language names to language codes.
* `styles.py`:  Holds the custom CSS code used to style the Streamlit application, providing a consistent and visually appealing user interface.

## Dependencies

* streamlit
* speechrecognition
* tempfile
* os
* soundfile
* numpy
* pyttsx3
* gtts
* io
* time
* threading
* google.generativeai
* dotenv

## Setup

1.  **Install Python Dependencies:**

    ```bash
    pip install streamlit SpeechRecognition soundfile numpy pyttsx3 gTTS google-generativeai python-dotenv
    ```

2.  **Environment Variables:**

    * Create a `.env` file in the project directory.
    * Add your Gemini API key to the `.env` file:

        ```
        AIzaSyA68Fn2F620ByQZvM9pza37TgTuejNYS8M=YOUR_GEMINI_API_KEY
        ```

3.  **Run the Application:**

    ```bash
    streamlit run main.py
    ```

4.  The application will open in your default web browser.

## Usage

* **Speech to Text:**
    * Select the input language.
    * Choose the audio source (Microphone or Upload Audio File).
    * If uploading a file, select the file.
    * Click "Start Speech to Text".
    * View the transcribed text.
    * Download the text or translate it.

* **Text to Speech:**
    * Select the output language.
    * Choose the voice gender.
    * Adjust the speech rate.
    * Enter the text to be converted.
    * Click "Play Speech" to hear the audio.
    * Click "Download Audio" to save the audio file.

* **Translation:**
    * After transcribing text, click "Translate to other language".
    * Select the target language.
    * View the translated text.

## Credits

* This application utilizes the `streamlit`, `speech_recognition`, `pyttsx3`, `gTTS`, and `google.generativeai` libraries.
* The user interface is styled with custom CSS.

## License

[Your License - e.g., MIT License]  (Add your project's license information here)

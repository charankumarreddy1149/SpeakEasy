import streamlit as st
from speech_to_text import speech_to_text_tab
from text_to_speech import text_to_speech_tab
from styles import custom_css

def main():
    # Streamlit UI Configuration - MUST be first command
    st.set_page_config(
        page_title="SpeakEasy", 
        page_icon="🔊", 
        layout="wide",
        initial_sidebar_state="collapsed"
    )

    # Apply custom CSS
    st.markdown(custom_css, unsafe_allow_html=True)

    # App Header
    st.markdown("""
    <div class="header">
        <h1>SpeakEasy</h1>
        <p>Speech to Text / Text to Speech Conversion</p>
    </div>
    """, unsafe_allow_html=True)

    # Initialize session state
    if 'current_page' not in st.session_state:
        st.session_state.current_page = 'speech_to_text'  # Default page

    # Navigation buttons
    col1, col2 = st.columns(2)
    with col1:
        if st.button("🎤 Speech to Text", key="speech_to_text_button"):
            st.session_state.current_page = 'speech_to_text'
    with col2:
        if st.button("🔊 Text to Speech", key="text_to_speech_button"):
            st.session_state.current_page = 'text_to_speech'

    # Display the selected page with error handling
    try:
        if st.session_state.current_page == 'speech_to_text':
            speech_to_text_tab()
        else:
            text_to_speech_tab()
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")
        st.info("Please try again or check the console for details.")

    # Footer
    st.markdown("""
    <div class="footer">
        <p>SpeakEasy App • Speech to Text / Text to Speech Conversion</p>
    </div>
    """, unsafe_allow_html=True)

    # Remove Streamlit default elements
    hide_streamlit_style = """
                <style>
                #MainMenu {visibility: hidden;}
                footer {visibility: hidden;}
                header {visibility: hidden;}
                </style>
                """
    st.markdown(hide_streamlit_style, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
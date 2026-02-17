import streamlit as st
from src.agenticchat.ui.streamlitui.load_ui import LoadStreamLitUi

def load_agenticchat_app():
    """
    Load and runs the Agentic Chat
    """

    ui=LoadStreamLitUi()
    user_input=ui.load_streamlit_ui()

    if not user_input:
        st.error("Something is wrong")
        return

    user_message = st.chat_input("Enter your message:")
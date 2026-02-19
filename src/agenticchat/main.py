import streamlit as st
from src.agenticchat.graph.graph_builder import GraphBuilder
from src.agenticchat.ui.streamlitui.load_ui import LoadStreamLitUi
from src.agenticchat.LLMS.groq import GroqConnection
from src.agenticchat.ui.streamlitui.display_result import DisplayResultStreamLit

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

    if user_message:
        try:
            obj_llm_config=GroqConnection(user_controls_input=user_input)
            model = obj_llm_config.get_llm_model()

            if not model:
                st.error("Llm model could not be initialized")
                return 
            
            usecase=user_input.get("selected_usecase")

            if not usecase:
                st.error("Wrong usecase")
                return
            
            graph_builder=GraphBuilder(model)
            try: 
                graph=graph_builder.setup_graph(usecase)
                DisplayResultStreamLit(usecase, graph, user_message).display_result_on_ui()

            except Exception as e:
                st.error(f"Error: Graph set up failed {e}")
                return

        except Exception as e:
            st.error(f"Error: Graph set up failed {e}")
            return
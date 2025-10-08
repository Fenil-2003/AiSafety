import streamlit as st
import models
from colorama import Fore, Style

# --- Model Loading (with Caching) ---

@st.cache_resource
def load_cached_models():
    print(f"{Fore.CYAN}===========================================")
    print(f"{Fore.CYAN}  Loading AI Safety Models... ")
    print(f"{Fore.CYAN}==========================================={Style.RESET_ALL}")
    loaded_models = models.load_all_models()
    print(f"\n{Fore.GREEN}✅ All models loaded and cached!{Style.RESET_ALL}\n")
    return loaded_models

# --- Main App Logic ---

st.set_page_config(page_title="AI Safety Chat Simulator", page_icon="🛡️")

# Load the models and store the returned dictionary in a variable.
loaded_models = load_cached_models()

# --- State Initialization ---
if "messages" not in st.session_state:
    st.session_state.messages = []
if "escalation_history" not in st.session_state:
    models.CONVERSATION_HISTORY.clear()

# --- Sidebar ---
st.sidebar.title("Chat Controls")
st.sidebar.markdown("---")
current_user_name = st.sidebar.radio("Select User", ["User A", "User B"])
age_profile = st.sidebar.select_slider(
    f"Set Age Profile for {current_user_name}",
    options=["child", "teen", "adult"],
    value="adult" if current_user_name == "User A" else "child"
)

if st.sidebar.button("Clear Chat History"):
    st.session_state.messages = []
    models.CONVERSATION_HISTORY.clear()
    st.rerun()

# --- Main Chat ---
st.title("🛡️ AI Safety Chat Simulator")
st.markdown("Enter a message to see the real-time AI safety analysis.")

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
        if "analysis" in message:
            with st.expander("View AI Safety Analysis"):
                st.json(message["analysis"])

# ---    User Input ---
if prompt := st.chat_input("What do you want to say?"):
    user_message = {"role": current_user_name, "content": prompt}
    st.session_state.messages.append(user_message)
    with st.chat_message(current_user_name):
        st.markdown(prompt)

    # Pass the loaded_models dictionary into the analysis function
    user_profile = {"age_profile": age_profile}
    analysis_results = models.analyze_message_fully(prompt, user_profile, loaded_models)
    
    with st.chat_message("assistant", avatar="🛡️"):
        st.markdown("_Here is the AI's analysis of the message:_")
        with st.expander("View AI Safety Analysis"):
            st.json(analysis_results)
    
    user_message["analysis"] = analysis_results
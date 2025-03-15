import streamlit as st
from main_llms import invoke_llm

st.title("Echo Bot")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# React to user input
if prompt := st.chat_input("What is up?"):
    # Display user message in chat message container
    st.chat_message("user").markdown(prompt)
    

    response = f"Echo: {prompt}"
    response = invoke_llm(prompt)
    # Display assistant response in chat message container
    st.chat_message("assistant").markdown(response)

    # ============= adding to history =======================
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})
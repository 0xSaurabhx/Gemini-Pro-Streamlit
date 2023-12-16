import vertexai
from vertexai.preview.generative_models import GenerativeModel, Part
import streamlit as st

model = GenerativeModel("gemini-pro-vision")

st.set_page_config(
    page_title="Gemini Pro Streamlit App",
    page_icon="✪",
    layout="wide",
)

st.title("Gemini AI Chat")
st.markdown('By [Saurabh](https://linkedin.com/in/dev-saurabh)')


# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user input
if user_input := st.chat_input("You:"):
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)
    # Make API request
    responses = model.generate_content(
    user_input,
    generation_config={
        "max_output_tokens": 2048,
        "temperature": 0.4,
        "top_p": 1,
        "top_k": 32
    },
  stream=True,
  )
    for response in responses:
      #capture full response
      full_res = "" + response.candidates[0].content.parts[0].text
    # Display assistant response
    if response:
        with st.chat_message("assistant"):
          st.markdown(full_res)
        st.session_state.messages.append({"role": "assistant", "content": full_res})
    else:
        st.text("An error occurred while fetching the response.")

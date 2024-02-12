
import google.generativeai as genai
import streamlit as st

API_KEY = 'AIzaSyDYbYW4ghwOKoYou5LVV9mfyst4bt2uxMc'
genai.configure(api_key=API_KEY)
generation_config = {
  "temperature": 0.9,
  "top_p": 1,
  "top_k": 1,
  "max_output_tokens": 2048,
}


safety_settings = [
  {
    "category": "HARM_CATEGORY_HARASSMENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
]

model = genai.GenerativeModel(model_name="gemini-pro",
                              generation_config=generation_config,
                              safety_settings=safety_settings)
st.set_page_config(
    page_title="Gemini Pro Streamlit App",
    page_icon="✪",
    layout="wide",
)

st.title("Gemini AI Chat")

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

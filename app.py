import torch
from transformers import pipeline
import streamlit as st

import asyncio

try:
    asyncio.get_running_loop()
except RuntimeError:
    asyncio.run(asyncio.sleep(0))

# Load Hugging Face Model
model_name = "tiiuae/falcon-7b-instruct"  # Example model
pipe = pipeline(
    "text-generation",
    model="tiiuae/falcon-7b-instruct",
    device=0 if torch.cuda.is_available() else "cpu"  # Use CPU if no GPU
)



def get_ai_response(prompt):
    try:
        response = pipe(prompt, max_length=200, do_sample=True, temperature=0.7)
        return response[0]["generated_text"]
    except Exception as e:
        return f"Error: {str(e)}"

# Streamlit App
st.set_page_config(page_title="Solar Industry AI Assistant", layout="wide")
st.title("🌞 Solar Industry AI Assistant")
st.write("Ask me anything about solar energy, from technology to market trends!")

# Sidebar for additional options
st.sidebar.header("Options")
temp = st.sidebar.slider("Response Temperature", 0.1, 1.0, 0.7)
max_len = st.sidebar.slider("Max Response Length", 50, 500, 200)

# User input
user_input = st.text_area("Your Question:", height=100)
if st.button("Get Answer") and user_input:
    with st.spinner("Generating response..."):
        answer = get_ai_response(user_input)
    st.subheader("Response:")
    st.write(answer)

# Footer
st.markdown("---")
st.markdown("Developed with ❤️ for the solar industry.")

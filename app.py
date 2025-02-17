
import streamlit as st
from transformers import pipeline

# Load Hugging Face Model
qa_pipeline = pipeline("text-generation", model="HuggingFaceH4/zephyr-7b-alpha")

def solar_assistant(prompt):
    """Generate AI responses for solar industry queries."""
    response = qa_pipeline(prompt, max_length=512, do_sample=True)
    return response[0]['generated_text']

# Streamlit UI
st.title("☀️ Solar Industry AI Assistant")
st.write("Ask me anything about solar energy!")

user_input = st.text_input("Your Question:")
if st.button("Ask"):
    if user_input:
        response = solar_assistant(user_input)
        st.text_area("Response", value=response, height=200)
    else:
        st.warning("Please enter a question.")

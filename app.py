import torch
from transformers import pipeline
import gradio as gr

# Load Hugging Face Model
model_name = "tiiuae/falcon-7b-instruct"  # Example model
pipe = pipeline("text-generation", model=model_name, device=0 if torch.cuda.is_available() else -1)

def get_ai_response(prompt):
    response = pipe(prompt, max_length=200, do_sample=True, temperature=0.7)
    return response[0]["generated_text"]

# Gradio Interface
interface = gr.Interface(
    fn=get_ai_response,
    inputs=gr.Textbox(lines=2, placeholder="Ask me anything about solar energy..."),
    outputs="text",
    title="🌞 Solar Industry AI Assistant",
    description="This AI assistant provides insights into solar panel technology, installation, maintenance, costs, regulations, and market trends."
)

# Launch the Gradio app
if __name__ == "__main__":
    interface.launch()

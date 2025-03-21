
import torch
import gradio as gr
from transformers import pipeline, AutoModelForCausalLM, AutoTokenizer

# ✅ Load Falcon-7B-Instruct with CPU optimization
model_name = "tiiuae/falcon-7b-instruct"

# ✅ Set model to use CPU and prevent memory overflow
model = AutoModelForCausalLM.from_pretrained(
    model_name,
    device_map="auto",  # Uses CPU efficiently
    torch_dtype=torch.float16,  # Lower precision to save memory
    low_cpu_mem_usage=True  # Helps prevent RAM overload
)

tokenizer = AutoTokenizer.from_pretrained(model_name)

# ✅ Create a text-generation pipeline
pipe = pipeline(
    "text-generation",
    model=model,
    tokenizer=tokenizer,
    max_length=200,  # Prevents excessive output length
    temperature=0.7,  # Balanced randomness
    do_sample=True
)

# ✅ Function to generate AI responses
def get_ai_response(prompt):
    response = pipe(prompt)
    return response[0]["generated_text"]

# ✅ Gradio Interface for AI Assistant
interface = gr.Interface(
    fn=get_ai_response,
    inputs=gr.Textbox(lines=2, placeholder="Ask me anything about solar energy..."),
    outputs="text",
    title="🌞 Solar Industry AI Assistant",
    description="This AI assistant provides insights into solar panel technology, installation, maintenance, costs, and market trends."
)

# ✅ Launch the Gradio App
if __name__ == "__main__":
    interface.launch()

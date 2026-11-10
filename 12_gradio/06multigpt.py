import os
from dotenv import load_dotenv
from openai import OpenAI

import gradio as gr
from scraper import fetch_website_contents

load_dotenv(override=True)

openai = OpenAI()

sarvam_api_key = os.getenv('SARVAM_API_KEY')

sarvam_ai = OpenAI(
    base_url="https://api.sarvam.ai/v1",
    api_key=sarvam_api_key,  # Get it from dashboard.sarvam.ai
)


system_message = "You are a helpful assistant"

# Let's create a call that streams back results
# If you'd like a refresher on Generators (the "yield" keyword),
# Please take a look at the Intermediate Python guide in the guides folder

def stream_gpt(prompt):
    messages = [
        {"role": "system", "content": system_message},
        {"role": "user", "content": prompt}
      ]
    stream = openai.chat.completions.create(
        model='gpt-5-nano',
        messages=messages,
        stream=True
    )
    result = ""
    for chunk in stream:
        result += chunk.choices[0].delta.content or ""
        yield result

ollama_url = "http://localhost:11434/v1"
ollama = OpenAI(api_key="ollama", base_url=ollama_url)

def stream_ollama(prompt):
    messages = [
        {"role": "system", "content": system_message},
        {"role": "user", "content": prompt}
      ]
    stream = ollama.chat.completions.create(
        model='llama3.2:latest',
        messages=messages,
        stream=True
    )
    result = ""
    for chunk in stream:
        result += chunk.choices[0].delta.content or ""
        yield result

def stream_Sarvam(prompt):
    messages = [{"role": "system", "content": system_message}, {"role": "user", "content": prompt}]
    # print(f"messages ::: {messages}")
    stream = sarvam_ai.chat.completions.create(model="sarvam-105b", messages=messages,stream=True)
    result = ""

    for chunk in stream:
        result += chunk.choices[0].delta.content or ""
        yield result
    # print(f"response ::: {response}")

    

def stream_model(prompt, model):
    if model=="GPT":
        result = stream_gpt(prompt)
    elif model=="OLLAMA":
        result = stream_ollama(prompt)
    elif model=="SARVAM":
            result = stream_Sarvam(prompt)
    else:
        raise ValueError("Unknown model")
    yield from result

message_input = gr.Textbox(label="Your message:", info="Enter a message for the LLM", lines=7)
model_selector = gr.Dropdown(["GPT", "OLLAMA","SARVAM"], label="Select model", value="OLLAMA")
message_output = gr.Markdown(label="Response:")

view = gr.Interface(
    fn=stream_model,
    title="LLMs", 
    inputs=[message_input, model_selector], 
    outputs=[message_output], 
    examples=[
            ["Explain the Transformer architecture to a layperson", "GPT"],
            ["Explain the Transformer architecture to an aspiring AI engineer", "OLLAMA"],
            ["Explain the RAG architecture to an aspiring AI engineer", "SARVAM"],
        ], 
    flagging_mode="never"
    )
view.launch()
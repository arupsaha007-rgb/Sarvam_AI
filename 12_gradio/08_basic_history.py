import os
from dotenv import load_dotenv
from openai import OpenAI

import gradio as gr

load_dotenv(override=True)

# openai = OpenAI()

def chat(message, history):
    return f"You said {message} and the history is {history}."

gr.ChatInterface(fn=chat).launch()

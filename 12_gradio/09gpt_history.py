import os
from dotenv import load_dotenv
from openai import OpenAI

import gradio as gr

load_dotenv(override=True)

openai = OpenAI()
MODEL = 'gpt-5-nano'
# Again, I'll be in scientist-mode and change this global during the lab

system_message = "You are a helpful assistant"


def chat(message, history):
    history = [{"role":h["role"], "content":h["content"]} for h in history]
    messages = [{"role": "system", "content": system_message}] + history + [{"role": "user", "content": message}]
    response = openai.chat.completions.create(model=MODEL, messages=messages)
    return response.choices[0].message.content


gr.ChatInterface(fn=chat).launch()

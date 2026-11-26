import os
from dotenv import load_dotenv
from openai import OpenAI

import gradio as gr

load_dotenv(override=True)

# openai = OpenAI()

sarvam_api_key = os.getenv('SARVAM_API_KEY')

sarvam_ai = OpenAI(
    base_url="https://api.sarvam.ai/v1",
    api_key=sarvam_api_key,  # Get it from dashboard.sarvam.ai
)


system_message = "You are a helpful assistant"

def message_gpt(prompt):
    messages = [{"role": "system", "content": system_message}, {"role": "user", "content": prompt}]
    response = sarvam_ai.chat.completions.create(model="sarvam-105b", messages=messages)
    return response.choices[0].message.content

# This can reveal the "training cut off", or the most recent date in the training data

# print(message_gpt("What is today's date?"))

# And now - changing the function from "shout" to "message_gpt"

message_input = gr.Textbox(label="Your message:", info="Enter a message for AI", lines=7)
message_output = gr.Textbox(label="Response:", lines=8)

view = gr.Interface(
    fn=message_gpt,
    title="AI", 
    inputs=[message_input], 
    outputs=[message_output], 
    examples=["Write a python program to add 2 numbers", "What is the capital of France?"], 
    flagging_mode="never"
    )
view.launch()
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
    print(f"messages ::: {messages}")
    response = sarvam_ai.chat.completions.create(model="sarvam-105b", messages=messages)
    print(f"response ::: {response}")
    return response.choices[0].message.content

# Let's use Markdown
# Are you wondering why it makes any difference to set system_message when it's not referred to in the code below it?
# I'm taking advantage of system_message being a global variable, used back in the message_gpt function (go take a look)
# Not a great software engineering practice, but quite common during Jupyter Lab R&D!

system_message = "You are a helpful assistant that responds in markdown without code blocks"

message_input = gr.Textbox(label="Your message:", info="Enter a message for Sarvam AI", lines=7)
message_output = gr.Markdown(label="Response:")

view = gr.Interface(
    fn=message_gpt,
    title="GPT", 
    inputs=[message_input], 
    outputs=[message_output], 
    examples=[
        "Explain the Transformer architecture to a layperson",
        "Explain the Transformer architecture to an aspiring AI engineer",
        ], 
    flagging_mode="never"
    )
view.launch()
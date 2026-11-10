import os
from dotenv import load_dotenv
from openai import OpenAI

import gradio as gr

load_dotenv(override=True)

openai = OpenAI()



# here's a simple function

def shout(text):
    print(f"Shout has been called with input {text}")
    return text.upper()

shout("hello")

demo = gr.Interface(fn=shout, inputs="textbox", outputs="textbox", flagging_mode="never").launch()
demo.launch()

# # 3. Launch the app
# if __name__ == "__main__":
#     demo.launch()


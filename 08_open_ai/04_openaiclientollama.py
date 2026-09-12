# imports
import os
import requests
from dotenv import load_dotenv
# from scraper import fetch_website_contents
# from IPython.display import Markdown, display
from openai import OpenAI

# If you get an error running this cell, then please head over to the troubleshooting notebook!

# Load environment variables in a file called .env

load_dotenv(override=True)

print(requests.get("http://localhost:11434").content)

OLLAMA_BASE_URL = "http://localhost:11434/v1"

ollama = OpenAI(base_url=OLLAMA_BASE_URL, api_key='ollama')


system_prompt = """
You are a helpful assistant. Reply should be precise. No further followup questions/suggestions
Do not answer with full sentence. only provide basic answer. 
"""
user_prompt = """
    Tell me joke on AI.
"""
print(user_prompt)
print("Thinking.........")
# Step 2: Make the messages list

messages = [
    {"role": "system", "content": system_prompt},
    {"role": "user", "content": user_prompt}
] # fill this in

# Step 3: Call OpenAI
response = ollama.chat.completions.create(model="qwen3:1.7b", messages=messages)
print(response.choices[0].message.content)
# imports
import os
from dotenv import load_dotenv
# from scraper import fetch_website_contents
# from IPython.display import Markdown, display
from openai import OpenAI

# If you get an error running this cell, then please head over to the troubleshooting notebook!

# Load environment variables in a file called .env

load_dotenv(override=True)
api_key = os.getenv('OPENAI_API_KEY')
openai = OpenAI()
# Step 1: Create your prompts

system_prompt = """
You are a helpful assistant. Reply should be precise. No further followup questions/suggestions
Do not answer with full sentence. only provide basic answer. 
"""
user_prompt = """
    What is the distance between Bangalore to Chennai?
"""

# Step 2: Make the messages list

messages = [
    {"role": "system", "content": system_prompt},
    {"role": "user", "content": user_prompt}
] # fill this in

# Step 3: Call OpenAI
response = openai.chat.completions.create(model="gpt-4.1-nano", messages=messages)
print(response.choices[0].message.content)

# Step 4: print the result
# print(
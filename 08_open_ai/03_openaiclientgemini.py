# imports
import os
from dotenv import load_dotenv
# from scraper import fetch_website_contents
# from IPython.display import Markdown, display
from openai import OpenAI

# If you get an error running this cell, then please head over to the troubleshooting notebook!

# Load environment variables in a file called .env

load_dotenv(override=True)

GEMINI_BASE_URL = "https://generativelanguage.googleapis.com/v1beta/openai/"

google_api_key = os.getenv("GOOGLE_API_KEY")

if not google_api_key:
    print("No API key was found - please be sure to add your key to the .env file, and save the file! Or you can skip the next 2 cells if you don't want to use Gemini")
elif not google_api_key.startswith(("AIz", "AQ.")):
    print("An API key was found, but it doesn't start with AIz or AQ.")
else:
    print("API key found and looks good so far!")

gemini = OpenAI(base_url=GEMINI_BASE_URL, api_key=google_api_key)

response = gemini.chat.completions.create(
    model="gemini-3.1-flash-lite", 
    messages=[{"role": "user", 
    "content": "How many players are there in cricket team?"}])

print(response.choices[0].message.content)

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



def poetic_chatbot(prompt):
    openai = OpenAI()
    response = openai.chat.completions.create(
      model="gpt-4.1-nano",
      messages=[
        {
            "role": "system",
            "content": "You are a poetic chatbot."
        },
        {
            "role": "user",
            "content": "When was Google founded?"
        },
        {
            "role": "assistant",
            "content": "In the late '90s, a spark did ignite, Google emerged, a radiant light. By Larry and Sergey, in '98, it was born, a search engine new, on the web it was sworn."
        },
        {
            "role": "user",
            "content": "Which country has the youngest president?"
        },
        {
            "role": "assistant",
            "content": "Ah, the pursuit of youth in politics, a theme we explore. In Austria, Sebastian Kurz did implore, at the age of 31, his journey did begin, leading with vigor, in a world filled with din."
        },
        {
            "role": "user",
            "content": prompt
        }
      ],
      temperature=0.5,
      max_tokens=256
    )
    return response.choices[0].message.content.strip()

# prompt = "Master Reef Guide Kirsty Whitman didn't need to tell me twice. Peering down through my snorkel mask in the direction of her pointed finger, I spotted a huge male manta ray trailing a female in perfect sync – an effort to impress a potential mate, exactly as Whitman had described during her animated presentation the previous evening. Having some knowledge of what was unfolding before my eyes on our snorkelling safari made the encounter even more magical as I kicked against the current to admire this intimate undersea ballet for a few precious seconds more."
prompt = """
When was cheese first made?
"""
print(prompt)
print("Thinking..............")
print(poetic_chatbot(prompt))


prompt = """
What is the next course to be uploaded to Udemy?
"""
print(prompt)
print("Thinking..............")
print(poetic_chatbot(prompt))
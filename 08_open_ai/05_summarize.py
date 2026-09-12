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



def text_summarizer(prompt):
    openai = OpenAI()
    response = openai.chat.completions.create(
      model="gpt-4.1-nano",
      messages=[
        {
          "role": "system",
          "content": "You will be provided with a block of text, and your task is to extract a list of keywords from it."
        },
        {
          "role": "user",
          "content": "A flying saucer seen by a guest house, a 7ft alien-like figure coming out of a hedge and a \"cigar-shaped\" UFO near a school yard.\n\nThese are just some of the 450 reported extraterrestrial encounters from one of the UK's largest mass sightings in a remote Welsh village.\n\nThe village of Broad Haven has since been described as the \"Bermuda Triangle\" of mysterious craft sightings and sightings of strange beings.\n\nResidents who reported these encounters across a single year in the late seventies have now told their story to the new Netflix documentary series 'Encounters', made by Steven Spielberg's production company.\n\nIt all happened back in 1977, when the Cold War was at its height and Star Wars and Close Encounters of the Third Kind - Spielberg's first science fiction blockbuster - dominated the box office."
        },
        {
          "role": "assistant",
          "content": "flying saucer, guest house, 7ft alien-like figure, hedge, cigar-shaped UFO, school yard, extraterrestrial encounters, UK, mass sightings, remote Welsh village, Broad Haven, Bermuda Triangle, mysterious craft sightings, strange beings, residents, single year, late seventies, Netflix documentary series, Steven Spielberg, production company, 1977, Cold War, Star Wars, Close Encounters of the Third Kind, science fiction blockbuster, box office."
        },
        {
          "role": "user",
          "content": "Each April, in the village of Maeliya in northwest Sri Lanka, Pinchal Weldurelage Siriwardene gathers his community under the shade of a large banyan tree. The tree overlooks a human-made body of water called a wewa – meaning reservoir or \"tank\" in Sinhala. The wewa stretches out besides the village's rice paddies for 175-acres (708,200 sq m) and is filled with the rainwater of preceding months.    \n\nSiriwardene, the 76-year-old secretary of the village's agrarian committee, has a tightly-guarded ritual to perform. By boiling coconut milk on an open hearth beside the tank, he will seek blessings for a prosperous harvest from the deities residing in the tree. \"It's only after that we open the sluice gate to water the rice fields,\" he told me when I visited on a scorching mid-April afternoon.\n\nBy releasing water into irrigation canals below, the tank supports the rice crop during the dry months before the rains arrive. For nearly two millennia, lake-like water bodies such as this have helped generations of farmers cultivate their fields. An old Sinhala phrase, \"wewai dagabai gamai pansalai\", even reflects the technology's centrality to village life; meaning \"tank, pagoda, village and temple\"."
        },
        {
          "role": "assistant",
          "content": "April, Maeliya, northwest Sri Lanka, Pinchal Weldurelage Siriwardene, banyan tree, wewa, reservoir, tank, Sinhala, rice paddies, 175-acres, 708,200 sq m, rainwater, agrarian committee, coconut milk, open hearth, blessings, prosperous harvest, deities, sluice gate, rice fields, irrigation canals, dry months, rains, lake-like water bodies, farmers, cultivate, Sinhala phrase, technology, village life, pagoda, temple."
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
As Washington abandons talks with Iran for an aggressive economic pressure campaign,
a cornered Tehran is now threatening military escalation and a wider war to force
negotiators back to the table.
US President Donald Trump has dismissed diplomacy with the Islamic Republic, calling a June ceasefire agreement one that “isn’t worth the paper it’s written on.” His administration has instead piled pressure on Iran through a global sanctions campaign, military strikes and a maritime blockade that stops goods from leaving or entering the country.
The multifront campaign has put Iran under unprecedented pressure, forcing its fatigued population to endure still more strain. Iranian Supreme Leader Mojtaba Khamenei, meanwhile, remains conspicuously absent. Tuesday will mark his sixth month in hiding in an attempt to avoid the fate of his father and predecessor, Ayatollah Ali Khamenei, who was killed in an airstrike at the start of the US-Israeli war against Iran in late February.
"""

print(prompt)
print("Thinking..............")
print(text_summarizer(prompt))
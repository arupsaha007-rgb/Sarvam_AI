# from pathlib import Path
from dotenv import load_dotenv
from langchain_sarvam import ChatSarvam

from langchain.agents import create_agent

from langchain.messages import HumanMessage

from pprint import pprint



# load_dotenv(Path(__file__).resolve().parents[1] / ".env")
load_dotenv()
llm = ChatSarvam(model="sarvam-105b")

agent = create_agent(model=llm)

# query = "Extract enties and designate them from below : Krishna Pyde paid money to Arup Saha in India and Srilanka?"
# query = "Extract enties and designate them from below : Krishna Pyde paid money near Bank?"
query = "Translate to hindi : I am going to Kolkata."
print(query)
print("Thinking......................")

response = agent.invoke(
    {"messages": [HumanMessage(content=query)]}
)



# pprint(response)

print(response['messages'][-1].content)


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



response = agent.invoke(
    {"messages": [HumanMessage(content="What's the capital of the Moon?")]}
)



pprint(response)

print(response['messages'][-1].content)


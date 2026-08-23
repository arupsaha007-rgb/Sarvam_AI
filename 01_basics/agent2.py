# from pathlib import Path
from dotenv import load_dotenv
from langchain_sarvam import ChatSarvam
from langchain.agents import create_agent
from langchain.messages import HumanMessage
from langchain.messages import AIMessage
from pprint import pprint

# load_dotenv(Path(__file__).resolve().parents[1] / ".env")
load_dotenv()
llm = ChatSarvam(model="sarvam-105b" # Kwargs passed to the model:
    ,temperature=1.0, max_tokens = 60)

agent = create_agent(model=llm)


response = agent.invoke(
    {"messages": [HumanMessage(content="What's the capital of the Moon?"),
    AIMessage(content="The capital of the Moon is Luna City."),
    HumanMessage(content="Interesting, tell me more about Luna City")]}
)

pprint(response)

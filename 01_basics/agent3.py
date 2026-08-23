# from pathlib import Path
from dotenv import load_dotenv
from langchain_sarvam import ChatSarvam
from langchain.agents import create_agent
from langchain.messages import HumanMessage
from langchain.messages import AIMessage
from pprint import pprint

# load_dotenv(Path(__file__).resolve().parents[1] / ".env")
load_dotenv()
llm = ChatSarvam(model="sarvam-105b")

agent = create_agent(model=llm)

for token, metadata in agent.stream(
    {"messages": [HumanMessage(content="Tell me all about Luna City, the capital of the Moon")]},
    stream_mode="messages"
):

    # token is a message chunk with token content
    # metadata contains which node produced the token
    
    if token.content:  # Check if there's actual content
        print(token.content, end="", flush=True)  # Print token



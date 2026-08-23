from dotenv import load_dotenv

load_dotenv()

from langchain.agents import create_agent
from langchain.messages import HumanMessage

from langchain_ollama import ChatOllama

from langchain.tools import tool
from typing import Dict, Any
from tavily import TavilyClient

tavily_client = TavilyClient()

@tool
def web_search(query: str) -> Dict[str, Any]:

    """Search the web for information"""

    return tavily_client.search(query)
# from pprint import pprint
# pprint(web_search.invoke("Who is the current mayor of San Francisco?"))

# 1. Initialize the local Ollama chat model
# By default, it connects to http://localhost:11434
llm = ChatOllama(
    model="qwen3:1.7b",
    temperature=0.7
)

agent = create_agent(
    model=llm,
    tools=[web_search]
)

# # question = HumanMessage(content="How up to date is your training knowledge?")
question = HumanMessage(content="Who is the current mayor of San Francisco?")


response = agent.invoke(
    {"messages": [question]}
)

print(response['messages'][-1].content)

from pprint import pprint

pprint(response['messages'])
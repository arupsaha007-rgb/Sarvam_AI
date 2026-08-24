from dotenv import load_dotenv

load_dotenv()

from langchain.tools import tool
from typing import Dict, Any
from tavily import TavilyClient
from langchain_ollama import ChatOllama
from langgraph.checkpoint.memory import InMemorySaver

tavily_client = TavilyClient()

@tool
def web_search(query: str) -> Dict[str, Any]:

    """Search the web for information"""

    return tavily_client.search(query)

system_prompt = """

You are a personal chef. The user will give you a list of ingredients they have left over in their house.

Using the web search tool, search the web for recipes that can be made with the ingredients they have.

Return recipe suggestions and eventually the recipe instructions to the user, if requested.

"""

from langchain.agents import create_agent

llm = ChatOllama(
    model="qwen3:1.7b",
    temperature=0.7
)

agent = create_agent(
    model=llm,
    tools=[web_search],
    system_prompt=system_prompt,
    checkpointer=InMemorySaver()
)

from langchain.messages import HumanMessage
from pprint import pprint

config = {"configurable": {"thread_id": "1"}}

response = agent.invoke(
    {"messages": [HumanMessage(content="I have some leftover chicken and rice. What can I make? Please only suggest Indian receipe")]},
    config
)
pprint(response)
print(response['messages'][-1].content)

print("--------------------------------------------------------------------------------------------------------")
from pprint import pprint

pprint(response)
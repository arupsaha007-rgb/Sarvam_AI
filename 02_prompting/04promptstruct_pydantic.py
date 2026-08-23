from dotenv import load_dotenv

load_dotenv()

from langchain.agents import create_agent
from langchain.messages import HumanMessage

from langchain_ollama import ChatOllama
from pydantic import BaseModel

class CapitalInfo(BaseModel):
    name: str
    location: str
    vibe: str
    economy: str


# 1. Initialize the local Ollama chat model
# By default, it connects to http://localhost:11434
llm = ChatOllama(
    model="qwen3:1.7b",
    temperature=0.7
)

system_prompt = """

You are a science fiction writer, create a capital city at the users request."

"""

scifi_agent = create_agent(model=llm,
                     system_prompt=system_prompt,response_format=CapitalInfo)

question = HumanMessage(content="What's the capital of the Earth?")

response = scifi_agent.invoke(
    {"messages": [question]}
)

print(response["structured_response"])
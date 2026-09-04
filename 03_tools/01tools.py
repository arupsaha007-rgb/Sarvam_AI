from dotenv import load_dotenv

load_dotenv()

from langchain.agents import create_agent
from langchain.messages import HumanMessage

from langchain_ollama import ChatOllama

from langchain.tools import tool

from langchain.messages import HumanMessage

# 1. Initialize the local Ollama chat model
# By default, it connects to http://localhost:11434
llm = ChatOllama(
    model="qwen3:1.7b",
    temperature=0.7
)

# Use below for OpenAI
# from langchain_openai import ChatOpenAI
# llm = ChatOpenAI(model="gpt-5-mini")


@tool("square_root", description="Calculate the square root of a number")
def tool1(x: float) -> float:
    return x ** 0.5
    # return x * x

print(tool1.invoke({"x": 467}))

agent = create_agent(
    model=llm,
    tools=[tool1],
    system_prompt="You are an arithmetic wizard. Use your tools to calculate the square root and square of any number."
)

question = HumanMessage(content="What is the square root of 467?")

response = agent.invoke(
    {"messages": [question]}
)

print(response['messages'][-1].content)

from pprint import pprint

pprint(response['messages'])

print(response["messages"][1].tool_calls)
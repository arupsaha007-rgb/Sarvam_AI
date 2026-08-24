from dotenv import load_dotenv

load_dotenv()

from langchain.agents import create_agent
from langchain.messages import HumanMessage

from langchain_ollama import ChatOllama



llm = ChatOllama(
    model="qwen3:1.7b",
    temperature=0.7
)

agent = create_agent(
    model = llm
)

from langchain.messages import HumanMessage

question = HumanMessage(content="Hello my name is Seán and my favourite colour is green")

response = agent.invoke(
    {"messages": [question]} 
)

from pprint import pprint

# pprint(response)

print('-----------------------------------------------------------------')
print(response['messages'][-1].content)

question = HumanMessage(content="What's my favourite colour?")

response = agent.invoke(
    {"messages": [question]} 
)
print('-----------------------------------------------------------------')
# pprint(response)

print(response['messages'][-1].content)
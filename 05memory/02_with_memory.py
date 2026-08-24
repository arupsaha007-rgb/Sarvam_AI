from dotenv import load_dotenv

load_dotenv()

from langchain.agents import create_agent
from langchain.messages import HumanMessage

from langchain_ollama import ChatOllama

from langgraph.checkpoint.memory import InMemorySaver  



llm = ChatOllama(
    model="qwen3:1.7b",
    temperature=0.7
)

agent = create_agent(
    model = llm,
    checkpointer=InMemorySaver(),  
)

from langchain.messages import HumanMessage

question = HumanMessage(content="Hello my name is Arup and my favourite colour is green")
config = {"configurable": {"thread_id": "1"}}


response = agent.invoke(
    {"messages": [question]} ,
    config,  
)

from pprint import pprint

# pprint(response)

print('-----------------------------------------------------------------')
print(response['messages'][-1].content)

question = HumanMessage(content="What's my favourite colour?")

response = agent.invoke(
    {"messages": [question]},
    config,  
)
print('-----------------------------------------------------------------')
# pprint(response)

print(response['messages'][-1].content)


question = HumanMessage(content="What's my name?")

response = agent.invoke(
    {"messages": [question]},
    config,  
)
print('-----------------------------------------------------------------')
# pprint(response)

print(response['messages'][-1].content)
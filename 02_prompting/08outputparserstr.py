from dotenv import load_dotenv

load_dotenv()

from langchain.agents import create_agent
from langchain.messages import HumanMessage

from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate

from langchain_core.messages import HumanMessage
from langchain_core.output_parsers import StrOutputParser

# 1. Initialize the local Ollama chat model
# By default, it connects to http://localhost:11434
llm = ChatOllama(
    model="qwen3:1.7b",
    temperature=0.7
)
query = "Can you give me an interesting fact I probably didn't know about?"
print(query)
message_h = HumanMessage(content = query)
response = llm.invoke([message_h])

print(response)

str_output_parser = StrOutputParser()

response_parsed = str_output_parser.invoke(response)
print(response_parsed)

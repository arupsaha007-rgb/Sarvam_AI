from dotenv import load_dotenv

load_dotenv()

from langchain.agents import create_agent
from langchain.messages import HumanMessage

from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate

from langchain_core.messages import HumanMessage
from langchain_core.output_parsers import CommaSeparatedListOutputParser

# 1. Initialize the local Ollama chat model
# By default, it connects to http://localhost:11434
llm = ChatOllama(
    model="qwen3:1.7b",
    temperature=0.7
)
message_h = HumanMessage(content = f''' I want you to create synthetic data for Customer.
It should have name, date of birth, department. Create only 10 records.
Out put should be in comma separated values. It should have a header.
Ex: 
name,dob,department
Sachin Sharma,17-Jul-1980,HR
''')

print(message_h.content)


response = llm.invoke([message_h])

print(response.content)

list_output_parser = CommaSeparatedListOutputParser()

response_parsed = list_output_parser.invoke(response)
print(response_parsed)

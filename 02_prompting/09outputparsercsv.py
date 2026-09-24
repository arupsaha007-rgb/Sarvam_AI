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
message_h = HumanMessage(content = f''' I've recently adopted a dog. Could you suggest some dog names? 

{CommaSeparatedListOutputParser().get_format_instructions()}
''')

print(message_h.content)


response = llm.invoke([message_h])

print(response.content)

list_output_parser = CommaSeparatedListOutputParser()

response_parsed = list_output_parser.invoke(response)
print(response_parsed)

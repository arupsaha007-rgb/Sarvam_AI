from dotenv import load_dotenv

load_dotenv()

# from langchain.agents import create_agent
# from langchain.messages import HumanMessage

from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate

from langchain_core.messages import HumanMessage
from langchain_core.output_parsers import CommaSeparatedListOutputParser

# 1. Initialize the local Ollama chat model
# By default, it connects to http://localhost:11434
llm = ChatOllama(
    model="qwen3:1.7b",
    temperature=0.7
)
list_instructions = CommaSeparatedListOutputParser().get_format_instructions()
chat_template = ChatPromptTemplate.from_messages([
    ('human', 
     "I've recently adopted a {pet}. Could you suggest three {pet} names? \n" + list_instructions)])
print(f" chat_template ::{chat_template.messages[0].prompt.template}" )

list_output_parser = CommaSeparatedListOutputParser()

chat_template_result = chat_template.invoke({'pet':'dog'})

chat_result = llm.invoke(chat_template_result)

response_parsed = list_output_parser.invoke(chat_result)
print("---------------------------------------------------------")
print(chat_result.content)
print(response_parsed)

# This creates a chain 
chain = chat_template | llm | list_output_parser

response = chain.invoke({'pet':'dog'})
print("---------------------------------------------------------")
print(response)


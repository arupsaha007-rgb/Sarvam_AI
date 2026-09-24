from dotenv import load_dotenv

load_dotenv()

# from langchain.agents import create_agent
# from langchain.messages import HumanMessage

from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate

from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough



# 1. Initialize the local Ollama chat model
# By default, it connects to http://localhost:11434
llm = ChatOllama(
    model="qwen3:1.7b",
    temperature=0.7
)

# Test RunnablePassthrough
print(RunnablePassthrough().invoke([1, 2, 3]))

# Adding Job title tool
chat_template_tools = ChatPromptTemplate.from_template('''
What are the five most important tools a {job title} needs?
Answer only by listing the tools.
''')

# Adding strategy tool
chat_template_strategy = ChatPromptTemplate.from_template('''
Considering the tools provided, develop a strategy for effectively learning and mastering them:
{tools}
''')

print(f"chat_template_tools:::{chat_template_tools}")

string_parser = StrOutputParser()

chain_tools = (chat_template_tools | llm | string_parser | {'tools':RunnablePassthrough()})
chain_strategy = chat_template_strategy | llm | string_parser
print("----------------------------------------------------------------------------------")

print(chain_tools.invoke({'job title':'data scientist'}))

# Combining both the chains
chain_combined = chain_tools | chain_strategy
print(chain_combined.get_graph().print_ascii())
# print(chain_combined.invoke({'job title':'IT security specialist'}))

print("----------------------------------------------------------------------------------")
chain_long = (chat_template_tools | llm | string_parser | {'tools':RunnablePassthrough()} | 
              chat_template_strategy | llm | string_parser)
print(chain_long.get_graph().print_ascii())
# print(chain_long.invoke({'job title':'Project Manager'}))


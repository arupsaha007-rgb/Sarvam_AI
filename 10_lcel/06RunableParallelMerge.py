from dotenv import load_dotenv

load_dotenv()


# from langchain.agents import create_agent
# from langchain.messages import HumanMessage

from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate

from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel



# 1. Initialize the local Ollama chat model
# By default, it connects to http://localhost:11434
llm = ChatOllama(
    model="qwen3:1.7b",
    temperature=0.7
)

# Adding chat templates
chat_template_books = ChatPromptTemplate.from_template(
    '''
    Suggest three of the best intermediate-level {programming language} books. 
    Answer only by listing the books.
    '''
)

chat_template_projects = ChatPromptTemplate.from_template(
    '''
    Suggest three interesting {programming language} projects suitable for intermediate-level programmers. 
    Answer only by listing the projects.
    '''
)

chat_template_time = ChatPromptTemplate.from_template(
     '''
     I'm an intermediate level programmer.
     
     Consider the following literature:
     {books}
     
     Also, consider the following projects:
     {projects}
     
     Roughly how much time would it take me to complete the literature and the projects?
     
     '''
)

string_parser = StrOutputParser()

chain_books = chat_template_books | llm | string_parser

chain_projects = chat_template_projects | llm | string_parser

# Setting up the parallel chain. Out put is set in books and projects respectively
chain_parallel = RunnableParallel({'books':chain_books, 'projects':chain_projects})

# print(chain_parallel.get_graph().print_ascii())
import time


# print("------------------------------------------------------------------------------")
# print("------------------------------------------------------------------------------")
# start = time.perf_counter()
# print(chain_parallel.invoke({'programming language':'Python'}))
# end = time.perf_counter()
# print(f"Time taken by chain_parallel: {end - start:.4f} seconds")




chain_time2 = ({'books':chain_books, 
                'projects':chain_projects}
              | chat_template_time 
              | llm 
              | string_parser
             )
chain_time2.get_graph().print_ascii()
print("------------------------------------------------------------------------------")
print("------------------------------------------------------------------------------")
start = time.perf_counter()
print(chain_time2.invoke({'programming language':'Python'}))
end = time.perf_counter()
print(f"Time taken by chain_time2: {end - start:.4f} seconds")



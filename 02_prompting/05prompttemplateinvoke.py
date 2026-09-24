from dotenv import load_dotenv

load_dotenv()

from langchain.agents import create_agent
from langchain.messages import HumanMessage

from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate
from langchain_core.prompts import ChatPromptTemplate


# 1. Initialize the local Ollama chat model
# By default, it connects to http://localhost:11434
llm = ChatOllama(
    model="qwen3:1.7b",
    temperature=0.7
)

template = """
You are a helpful assistant.

Answer the following question in simple terms:

Question: {question}
"""

prompt = PromptTemplate(
    template=template,
    input_variables=["question"]
)

formatted_prompt = prompt.invoke({
    "question": "What is vector search?"
})

print(formatted_prompt.text)

print("2nd example.......................")
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are an AI tutor. Keep answers concise."),
    ("human", "Explain {topic} with an example.")
])

# Fill template variables and pass the resulting messages to the agent
messages = prompt.invoke({
    "topic": "RAG pipeline"
}).messages


tutor_agent = create_agent(model=llm)
result = tutor_agent.invoke({
    "messages": messages
})

print(result["messages"][-1].content)
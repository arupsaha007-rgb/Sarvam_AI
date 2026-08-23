from dotenv import load_dotenv

load_dotenv()

from langchain.agents import create_agent
from langchain.messages import HumanMessage

from langchain_ollama import ChatOllama

# 1. Initialize the local Ollama chat model
# By default, it connects to http://localhost:11434
llm = ChatOllama(
    model="qwen3:1.7b",
    temperature=0.7
)

system_prompt = """

You are a science fiction writer, create a space capital city at the users request.
Answer with one word.

User: What is the capital of mars?
Scifi Writer: Marsialis

User: What is the capital of Venus?
Scifi Writer: Venusovia

"""


scifi_agent = create_agent(model=llm,
                     system_prompt=system_prompt)

question = HumanMessage(content="What's the capital of the France?")

response = scifi_agent.invoke(
    {"messages": [question]}
)

print(response['messages'][1].content)
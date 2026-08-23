from pathlib import Path
from dotenv import load_dotenv
from langchain_sarvam import ChatSarvam

# load_dotenv(Path(__file__).resolve().parents[1] / ".env")
load_dotenv()
llm = ChatSarvam(model="sarvam-105b")

# from langchain_sarvam import ChatSarvam

# llm = ChatSarvam(model="sarvam-105b")

response = llm.invoke("What is the capital of France?'")
print(response.content)  
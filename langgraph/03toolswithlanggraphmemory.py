from typing import Annotated
from langgraph.graph import StateGraph, START
from langgraph.graph.message import add_messages
from dotenv import load_dotenv
from IPython.display import Image, display
import gradio as gr
from langgraph.prebuilt import ToolNode, tools_condition
import requests
import os
from langchain_openai import ChatOpenAI
from typing import TypedDict
from langchain_community.utilities import GoogleSerperAPIWrapper
from langchain_sarvam import ChatSarvam

from langgraph.checkpoint.memory import MemorySaver



# Our favorite first step! Crew was doing this for us, by the way.
load_dotenv(override=True)

from langchain.tools import tool
serper = GoogleSerperAPIWrapper()

@tool("serper_tool", description="Useful for when you need more information from an online search")
def serper_tool(search_string: str) -> str:
    print(f"serper_tool {search_string}")
    return serper.run(search_string)
    # return x * x


# print(serper.run("What is the capital of France?"))

from langchain_core.tools import Tool

# tool_search =Tool(
#         name="search",
#         func=serper.run,
#         description="Useful for when you need more information from an online search"
#     )

# print(tool_search.invoke("What is the capital of France?"))

pushover_token = os.getenv("PUSHOVER_TOKEN")
pushover_user = os.getenv("PUSHOVER_USER")
pushover_url = "https://api.pushover.net/1/messages.json"

def push(text: str):
    """Send a push notification to the user"""
    requests.post(pushover_url, data = {"token": pushover_token, "user": pushover_user, "message": text})

tool_push = Tool(
        name="send_push_notification",
        func=push,
        description="useful for when you want to send a push notification"
    )

# tool_push.invoke("Hello, me")

# tools = [tool_search, tool_push]
tools = [serper_tool, tool_push]


# Step 1: Define the State object
class State(TypedDict):
    messages: Annotated[list, add_messages]

# Step 2: Start the Graph Builder with this State class
graph_builder = StateGraph(State)
memory = MemorySaver()

# Step 3
# llm = ChatOpenAI(model="gpt-4o-mini")
llm = ChatSarvam(model="sarvam-105b")
llm_with_tools = llm.bind_tools(tools)

def chatbot(state: State):
    print(state)
    return {"messages": [llm_with_tools.invoke(state["messages"])]}

graph_builder.add_node("chatbot", chatbot)
graph_builder.add_node("tools", ToolNode(tools=tools))

# Step 4
graph_builder.add_conditional_edges( "chatbot", tools_condition, "tools")
graph_builder.add_edge("tools", "chatbot")
graph_builder.add_edge(START, "chatbot")

# Step 5
graph = graph_builder.compile(checkpointer=memory)
# display(Image(graph.get_graph().draw_mermaid_png()))

config = {"configurable": {"thread_id": "1"}}

# def chat(user_input: str, history):
#     result = graph.invoke({"messages": [{"role": "user", "content": user_input}]}, config=config)
#     return result["messages"][-1].content

def chat(user_input: str, history):
    message = {"role": "user", "content": user_input}
    messages = [message]
    state = State(messages=messages)
    result = graph.invoke(state, config=config)
    print(result)
    print(result["messages"][-1].content)
    return result["messages"][-1].content


gr.ChatInterface(chat).launch()

graph.get_state(config)

# Most recent first

list(graph.get_state_history(config))
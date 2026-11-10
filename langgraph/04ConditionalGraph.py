from langgraph.graph import START, END, StateGraph
from typing_extensions import TypedDict
# from langchain_openai.chat_models import ChatOpenAI
from langchain_sarvam import ChatSarvam
from langchain_core.messages import HumanMessage, BaseMessage
from collections.abc import Sequence
from typing import Literal

from dotenv import load_dotenv
# Our favorite first step! Crew was doing this for us, by the way.
load_dotenv(override=True)

# Define the state
class State(TypedDict):
    messages: Sequence[BaseMessage]

chat = ChatSarvam(model="sarvam-105b",
                  temperature = 0, 
                  max_completion_tokens = 100)

# chat = ChatOpenAI(model = "gpt-4o-mini", 
#                   seed = 365, 
#                   temperature = 0, 
#                   max_completion_tokens = 100)

def ask_question(state: State) -> State:
    
    print(f"\n-------> ENTERING ask_question:")
    
    print("What is your question?")
    
    return State(messages = [HumanMessage(input())])

# print(ask_question(State(messages = [])))

def chatbot(state: State) -> State:
    
    print(f"\n-------> ENTERING chatbot:")
    
    response = chat.invoke(state["messages"])
    response.pretty_print()
    
    return State(messages = [response])

def ask_another_question(state: State) -> State:
    
    print(f"\n-------> ENTERING ask_another_question:")
    
    print("Would you like to ask one more question (yes/no)?")
    
    return State(messages = [HumanMessage(input())])

# print(ask_another_question(State(messages = [])))

def routing_function(state: State) -> Literal["ask_question","__end__"]:
    
    if state["messages"][-1].content.strip().lower() == "yes":
        return "ask_question"
    else:
        return "__end__"

# Define the graph
graph = StateGraph(State)

graph.add_node("ask_question", ask_question)
graph.add_node("chatbot", chatbot)
graph.add_node("ask_another_question", ask_another_question)

graph.add_edge(START, "ask_question")
graph.add_edge("ask_question", "chatbot")
graph.add_edge("chatbot", "ask_another_question")
graph.add_conditional_edges(source = "ask_another_question", 
                            path = routing_function)

graph_compiled = graph.compile()
print(graph_compiled.get_graph().draw_ascii())

graph_compiled.invoke(State(messages = []))
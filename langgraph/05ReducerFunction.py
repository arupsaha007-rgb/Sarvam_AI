from langgraph.graph import START, END, StateGraph, add_messages
from typing_extensions import TypedDict
# from langchain_openai.chat_models import ChatOpenAI
from langchain_core.messages import AIMessage, HumanMessage, BaseMessage
from collections.abc import Sequence
from typing import Literal, Annotated
from langchain_sarvam import ChatSarvam


from dotenv import load_dotenv
# Our favorite first step! Crew was doing this for us, by the way.
load_dotenv(override=True)

my_list = add_messages([HumanMessage("Hi! I'm Oscar."), 
                        AIMessage("Hey, Oscar. How can I assist you?")],
                       [HumanMessage("Could you summarize today's news?")])

print(my_list)

class State(TypedDict):
    messages: Annotated[Sequence[BaseMessage], add_messages]

chat = ChatSarvam(model="sarvam-105b" ,
                  temperature = 0, 
                  max_completion_tokens = 100)

def ask_question(state: State) -> State:
    
    print(f"\n-------> ENTERING ask_question:")
    for i in state["messages"]:
        i.pretty_print()
    
    question = "What is your question?"
    print(question)
    
    return State(messages = [AIMessage(question), HumanMessage(input())])

def chatbot(state: State) -> State:
    
    print(f"\n-------> ENTERING chatbot:")
    for i in state["messages"]:
        i.pretty_print()
    
    response = chat.invoke(state["messages"])
    response.pretty_print()
    
    return State(messages = [response])

def ask_another_question(state: State) -> State:
    
    print(f"\n-------> ENTERING ask_another_question:")
    for i in state["messages"]:
        i.pretty_print()
    
    question = "Would you like to ask one more question (yes/no)?"
    print(question)
    
    return State(messages = [AIMessage(question), HumanMessage(input())])

def routing_function(state: State) -> Literal["ask_question", "__end__"]:
    
    if state["messages"][-1].content == "yes":
        return "ask_question"
    else:
        return "__end__"

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

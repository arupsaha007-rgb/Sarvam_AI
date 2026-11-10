from langgraph.graph import START, END, StateGraph, add_messages, MessagesState
from typing_extensions import TypedDict
# from langchain_openai.chat_models import ChatOpenAI
from langchain_core.messages import AIMessage, HumanMessage, BaseMessage, RemoveMessage
from collections.abc import Sequence
from typing import Literal, Annotated
from langchain_sarvam import ChatSarvam


from dotenv import load_dotenv
# Our favorite first step! Crew was doing this for us, by the way.
load_dotenv(override=True)

my_list = add_messages([AIMessage("What is your question?"), 
                        HumanMessage("Could you tell me a grook by Piet Hein?"),
                        AIMessage("Certainly! Here's a well-known grook by Piet Hein..."),
                        AIMessage("Would you like to ask one more question?"),
                        HumanMessage("yes"),
                        AIMessage("What is your question?"),
                        HumanMessage("Where was the poet born?"),
                        AIMessage("Piet Hein was born in Copenhagen, Denmark, on December 16, 1905."),
                        AIMessage("Would you like to ask one more question?")],
                       [HumanMessage("yes")]
                      )

# print(my_list)
# print("-------------------------------------------------------------------------")

# print(my_list[:-5])
# print("-------------------------------------------------------------------------")

# remove_messages = [RemoveMessage(id = i.id) for i in my_list[:-5]]

# print(f"remove_messages {remove_messages}")
# print("-------------------------------------------------------------------------")

chat = ChatSarvam(model="sarvam-105b" ,
                  temperature = 0, 
                  max_completion_tokens = 100)

def ask_question(state: MessagesState) -> MessagesState:
    
    print(f"\n-------> ENTERING ask_question:")
    for i in state["messages"]:
        i.pretty_print()
    
    question = "What is your question?"
    print(question)
    
    return MessagesState(messages = [AIMessage(question), HumanMessage(input())])

def chatbot(state: MessagesState) -> MessagesState:
    
    print(f"\n-------> ENTERING chatbot:")
    for i in state["messages"]:
        i.pretty_print()
    
    response = chat.invoke(state["messages"])
    response.pretty_print()
    
    return MessagesState(messages = [response])


def ask_another_question(state: MessagesState) -> MessagesState:
    
    print(f"\n-------> ENTERING ask_another_question:")
    for i in state["messages"]:
        i.pretty_print()
    
    question = "Would you like to ask one more question (yes/no)?"
    print(question)
    
    return MessagesState(messages = [AIMessage(question), HumanMessage(input())])

def trim_messages(state: MessagesState) -> MessagesState:
    print(f"\n-------> ENTERING trim_messages:")
    
    remove_messages = [RemoveMessage(id = i.id) for i in state["messages"][:-5]]
    
    return MessagesState(messages = remove_messages)

def routing_function(state: MessagesState) -> Literal["trim_messages", "__end__"]:
    
    if state["messages"][-1].content == "yes":
        return "trim_messages"
    else:
        return "__end__"

graph = StateGraph(MessagesState)

graph.add_node("ask_question", ask_question)
graph.add_node("chatbot", chatbot)
graph.add_node("ask_another_question", ask_another_question)
graph.add_node("trim_messages", trim_messages)

graph.add_edge(START, "ask_question")
graph.add_edge("ask_question", "chatbot")
graph.add_edge("chatbot", "ask_another_question")
graph.add_conditional_edges(source = "ask_another_question", 
                            path = routing_function)
graph.add_edge("trim_messages", "ask_question")

graph_compiled = graph.compile()
print(graph_compiled.get_graph().draw_ascii())

graph_compiled.invoke(MessagesState(messages = []))
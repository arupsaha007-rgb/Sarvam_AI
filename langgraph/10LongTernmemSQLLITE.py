from langgraph.graph import StateGraph, START, END, MessagesState
from langchain_openai.chat_models import ChatOpenAI
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage, RemoveMessage
from typing import Literal
import sqlite3
from langgraph.checkpoint.sqlite import SqliteSaver


from langchain_sarvam import ChatSarvam


from dotenv import load_dotenv
# Our favorite first step! Crew was doing this for us, by the way.
load_dotenv(override=True)

class State(MessagesState):
    summary: str

test_state = State()

print(test_state.get("summary", ""))
print(bool(test_state.get("summary", "")))

# chat = ChatSarvam(model="sarvam-105b" ,
#                   temperature = 0, 
#                   max_completion_tokens = 100)

# chat = ChatOpenAI(model = "gpt-4o-mini", 
#                   seed = 365, 
#                   temperature = 0, 
#                   max_completion_tokens = 100)

from langchain_ollama import ChatOllama

# 1. Initialize the local Ollama chat model
# By default, it connects to http://localhost:11434
chat = ChatOllama(
    model="qwen3:1.7b",
    temperature=0.7
)

def ask_question(state: MessagesState) -> MessagesState:
    
    print(f"\n-------> ENTERING ask_question:")
    for i in state["messages"]:
        i.pretty_print()
    
    question = "What is your question?"
    print(question)
    
    return MessagesState(messages = [AIMessage(question), HumanMessage(input())])

def chatbot(state: State) -> State:
    
    print(f"\n-------> ENTERING chatbot:")
    for i in state["messages"]:
        i.pretty_print()

    print(f"Summary :::::::: {state.get("summary", "")}")
    system_message = f'''
    Here's a quick summary of what's been discussed so far:
    {state.get("summary", "")}
    
    Keep this in mind as you answer the next question.
    '''
    
    response = chat.invoke([SystemMessage(system_message)] + state["messages"])
    response.pretty_print()
    
    return State(messages = [response])



# def ask_another_question(state: State) -> State:
    
#     print(f"\n-------> ENTERING ask_another_question:")
    
#     question = "Would you like to ask one more question (yes/no)?"
#     print(question)
    
#     return State(messages = [AIMessage(question), HumanMessage(input())])


def summarize_and_delete_messages(state: State) -> State:
    print(f"\n-------> ENTERING summarize_and_delete_messages:")
    
    new_conversation = ""
    for i in state["messages"]:
        new_conversation += f"{i.type}: {i.content}\n\n"
        
    summary_instructions = f'''
Update the ongoing summary by incorporating the new lines of conversation below.  
Build upon the previous summary rather than repeating it so that the result  
reflects the most recent context and developments.


Previous Summary:
{state.get("summary", "")}

New Conversation:
{new_conversation}
'''
    
    print(summary_instructions)
    
    summary = chat.invoke([HumanMessage(summary_instructions)])
    
    remove_messages = [RemoveMessage(id = i.id) for i in state["messages"][:]]
    
    return State(messages = remove_messages, summary = summary.content)

# def routing_function(state: State) -> Literal["summarize_and_delete_messages", "__end__"]:
    
#     if state["messages"][-1].content == "yes":
#         return "summarize_and_delete_messages"
#     else:
#         return "__end__"



graph = StateGraph(State)

graph.add_node("ask_question", ask_question)
graph.add_node("chatbot", chatbot)
# graph.add_node("ask_another_question", ask_another_question)
graph.add_node("summarize_and_delete_messages", summarize_and_delete_messages)

graph.add_edge(START, "ask_question")
graph.add_edge("ask_question", "chatbot")
graph.add_edge("chatbot", "summarize_and_delete_messages")
graph.add_edge("summarize_and_delete_messages", END)

# graph_compiled = graph.compile()


# graph_compiled.invoke(State(messages = []))

db_path = "C:/SQLLITE_DB/langgraph.db"
con = sqlite3.connect(database = db_path, check_same_thread = False)
checkpointer = SqliteSaver(con)
graph_compiled = graph.compile(checkpointer)

print(graph_compiled.get_graph().draw_ascii())
config1 = {"configurable": {"thread_id": "1"}}
# config2 = {"configurable": {"thread_id": "2"}}
graph_compiled.invoke(State(), config1)

print("-------------------------------------------------------------------------------")
print("Again!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
print("-------------------------------------------------------------------------------")

while True:
    option = input("Do you want to continue (Y/N):")
    
    # Check the condition at the end of the iteration
    if option.strip().upper() in ['N', 'NO']:
        break  # Exit loop if input is valid
        
    graph_compiled.invoke(State(), config1)

print(f"Thank you!")
















from dotenv import load_dotenv

load_dotenv()

from langchain.agents import create_agent
from langchain.messages import HumanMessage

from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate

from langchain_core.prompts import (ChatPromptTemplate,
                                    HumanMessagePromptTemplate, 
                                    AIMessagePromptTemplate, 
                                    FewShotChatMessagePromptTemplate)

# 1. Initialize the local Ollama chat model
# By default, it connects to http://localhost:11434
llm = ChatOllama(
    model="qwen3:1.7b",
    temperature=0.7
)

TEMPLATE_H = '''I've recently adopted a {pet}. 
Could you suggest some {pet} names?'''
TEMPLATE_AI = '''{response}'''

message_template_h = HumanMessagePromptTemplate.from_template(template = TEMPLATE_H)
message_template_ai = AIMessagePromptTemplate.from_template(template = TEMPLATE_AI)

example_template = ChatPromptTemplate.from_messages([message_template_h, 
                                                     message_template_ai])

examples = [{'pet':'dog', 
             'response':'''Oh, absolutely. Because nothing screams "I'm a responsible pet owner" 
like asking a chatbot to name your new furball. How about "Bark Twain" (if it's a literary hound)? '''}, 
            
            {'pet':'cat', 
             'response':'''Oh, absolutely. Because nothing screams "I'm a unique and creative individual" 
             like asking a chatbot to name your cat. How about "Furry McFurFace", "Sir Meowsalot", or "Catastrophe"? '''}, 
            
            {'pet':'fish', 
             'response':
             '''Oh, absolutely. Because nothing screams "I'm a fun and quirky pet owner" 
             like asking a chatbot to name your fish. How about "Fin Diesel", "Gill Gates", or "Bubbles"?'''}]


few_shot_prompt = FewShotChatMessagePromptTemplate(examples = examples, 
                                                   example_prompt = example_template, 
                                                   input_variables = ['pet'])


chat_template = ChatPromptTemplate.from_messages([few_shot_prompt, 
                                                  message_template_h])

# LangChain v1 uses runnable pipelines in place of the removed LLMChain API.
chain = chat_template | llm


response = chain.invoke({'pet':'rabbit'})

print(response.content)



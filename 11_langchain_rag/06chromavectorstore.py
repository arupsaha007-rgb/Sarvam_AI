# pip install -U langchain-chroma langchain


from langchain_community.document_loaders import Docx2txtLoader
from langchain_text_splitters.markdown import MarkdownHeaderTextSplitter
from langchain_text_splitters.character import CharacterTextSplitter
from langchain_openai.embeddings import OpenAIEmbeddings
import numpy as np
from dotenv import load_dotenv
from langchain_chroma import Chroma


from pathlib import Path

load_dotenv(override=True)

doc_Path = Path(__file__).with_name("Introduction_to_Data_and_Data_Science_2.docx")


loader = Docx2txtLoader(doc_Path)
pages = loader.load()

md_splitter = MarkdownHeaderTextSplitter(
    headers_to_split_on = [("#", "Course Title"), 
                           ("##", "Lecture Title")]
)

pages_md_split = md_splitter.split_text(pages[0].page_content)

# print(pages_md_split)

for i in range(len(pages_md_split)):
    # print("-------------------------------------------------------------------------------")
    # print("-------------------------------------------------------------------------------")
    # print(i)
    # print("-------------------------------------------------------------------------------")
    pages_md_split[i].page_content = ' '.join(pages_md_split[i].page_content.split())
    # print(pages_md_split[i].page_content)
    
char_splitter = CharacterTextSplitter(
    separator = ".",
    chunk_size = 500,
    chunk_overlap  = 50
)

pages_char_split = char_splitter.split_documents(pages_md_split)

# print(pages_char_split)

# Open AI Embedding model
embedding = OpenAIEmbeddings(model = "text-embedding-3-small")
print("-------------------------------------------------------------------------------")
# 
print("-------------------------------------------------------------------------------")

# Create the Chroma Vector Store
vectorstore = Chroma.from_documents(documents = pages_char_split, 
                                    embedding = embedding, 
                                    persist_directory = "./intro-to-ds-lectures")


# Load the Vector Store
vectorstore_from_directory = Chroma(persist_directory = "./intro-to-ds-lectures", 
                                    embedding_function = embedding)


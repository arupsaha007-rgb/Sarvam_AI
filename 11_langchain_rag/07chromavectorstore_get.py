# pip install -U langchain-chroma langchain


from langchain_community.document_loaders import Docx2txtLoader
from langchain_text_splitters.markdown import MarkdownHeaderTextSplitter
from langchain_text_splitters.character import CharacterTextSplitter
from langchain_openai.embeddings import OpenAIEmbeddings
import numpy as np
from dotenv import load_dotenv
from langchain_chroma import Chroma
from langchain_core.documents import Document


from pathlib import Path

load_dotenv(override=True)

# Open AI Embedding model
embedding = OpenAIEmbeddings(model = "text-embedding-3-small")

# Load the Vector Store
vectorstore_from_directory = Chroma(persist_directory = "./intro-to-ds-lectures", 
                                    embedding_function = embedding)

# print(vectorstore_from_directory.get())
# print(vectorstore_from_directory.get())
# 0939cba0-1a89-4f5d-aca8-9cb395be4e8a

print(vectorstore_from_directory.get(ids = "0939cba0-1a89-4f5d-aca8-9cb395be4e8a", 
                               include = ["embeddings"]))

# New document to be added
# added_document = Document(page_content='Alright! So… Let’s discuss the not-so-obvious differences between the terms analysis and analytics. Due to the similarity of the words, some people believe they share the same meaning, and thus use them interchangeably. Technically, this isn’t correct. There is, in fact, a distinct difference between the two. And the reason for one often being used instead of the other is the lack of a transparent understanding of both. So, let’s clear this up, shall we? First, we will start with analysis', 
#                           metadata={'Course Title': 'Introduction to Data and Data Science', 
#                                     'Lecture Title': 'Analysis vs Analytics'})
# print(vectorstore_from_directory.add_documents([added_document]))
# 3a0e3c5c-5125-4caf-9776-a98200b99174

print(vectorstore_from_directory.get("3a0e3c5c-5125-4caf-9776-a98200b99174"))



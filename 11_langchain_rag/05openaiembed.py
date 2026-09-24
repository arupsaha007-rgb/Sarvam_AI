from langchain_community.document_loaders import Docx2txtLoader
from langchain_text_splitters.markdown import MarkdownHeaderTextSplitter
from langchain_text_splitters.character import CharacterTextSplitter
from langchain_openai.embeddings import OpenAIEmbeddings
import numpy as np
from dotenv import load_dotenv

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
print("3-------------------------------------------------------------------------------")
print("-------------------------------------------------------------------------------")
print(pages_char_split[3])
print("-------------------------------------------------------------------------------")
print("-------------------------------------------------------------------------------")

print("5-------------------------------------------------------------------------------")
print("-------------------------------------------------------------------------------")
print(pages_char_split[5])
print("-------------------------------------------------------------------------------")
print("-------------------------------------------------------------------------------")


print("18-------------------------------------------------------------------------------")
print("-------------------------------------------------------------------------------")
print(pages_char_split[18])
print("-------------------------------------------------------------------------------")
print("-------------------------------------------------------------------------------")


vector1 = embedding.embed_query(pages_char_split[3].page_content)
vector2 = embedding.embed_query(pages_char_split[5].page_content)
vector3 = embedding.embed_query(pages_char_split[18].page_content)

print(len(vector1), len(vector2), len(vector3))
print("-------------------------------------------------------------------------------")
print(np.dot(vector1, vector2), np.dot(vector1, vector3), np.dot(vector2, vector3))
print("-------------------------------------------------------------------------------")
print(np.linalg.norm(vector1), np.linalg.norm(vector2), np.linalg.norm(vector3))
print("-------------------------------------------------------------------------------")
# Example: Split a Word document, embed its chunks, and persist them in Chroma.
# pip install -U langchain-chroma langchain


from langchain_community.document_loaders import Docx2txtLoader
from langchain_text_splitters.markdown import MarkdownHeaderTextSplitter
from langchain_text_splitters.character import CharacterTextSplitter
from langchain_openai.embeddings import OpenAIEmbeddings
import numpy as np
from dotenv import load_dotenv
from langchain_chroma import Chroma


from pathlib import Path

# Load API credentials from .env, replacing matching environment variables.
load_dotenv(override=True)

# Locate the source document beside this script and extract its text.
doc_Path = Path(__file__).with_name("Introduction_to_Data_and_Data_Science_2.docx")


loader = Docx2txtLoader(doc_Path)
pages = loader.load()

# Split on literal Markdown headings and retain course/lecture names as metadata.
# This reads text markers, not Word heading styles.
md_splitter = MarkdownHeaderTextSplitter(
    headers_to_split_on = [("#", "Course Title"), 
                           ("##", "Lecture Title")]
)

pages_md_split = md_splitter.split_text(pages[0].page_content)

# print(pages_md_split)

# Normalize whitespace within each section before creating smaller chunks.
for i in range(len(pages_md_split)):
    # print("-------------------------------------------------------------------------------")
    # print("-------------------------------------------------------------------------------")
    # print(i)
    # print("-------------------------------------------------------------------------------")
    pages_md_split[i].page_content = ' '.join(pages_md_split[i].page_content.split())
    # print(pages_md_split[i].page_content)
    
# Target 500-character chunks at period boundaries with 50-character overlap.
# Segments without suitable boundaries can exceed the target size.
char_splitter = CharacterTextSplitter(
    separator = ".",
    chunk_size = 500,
    chunk_overlap  = 50
)

# Split the text while retaining each source section's metadata.
pages_char_split = char_splitter.split_documents(pages_md_split)

# print(pages_char_split)

# Open AI Embedding model
# Configure the embedding model for stored text and later queries.
embedding = OpenAIEmbeddings(model = "text-embedding-3-small")
print("-------------------------------------------------------------------------------")
# 
print("-------------------------------------------------------------------------------")

# Create the Chroma Vector Store
# Embed chunks through OpenAI and persist their text, metadata, and vectors locally.
# The persistence path is relative to the working directory.
# Re-running this insertion can add duplicate content with new generated IDs.
vectorstore = Chroma.from_documents(documents = pages_char_split, 
                                    embedding = embedding, 
                                    persist_directory = "./intro-to-ds-lectures")


# Load the Vector Store
# Reopen the saved collection with the same embedding model for future queries.
vectorstore_from_directory = Chroma(persist_directory = "./intro-to-ds-lectures", 
                                    embedding_function = embedding)


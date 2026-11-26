# Example: Embed selected text chunks and compare their vector similarity.
from langchain_community.document_loaders import Docx2txtLoader
from langchain_text_splitters.markdown import MarkdownHeaderTextSplitter
from langchain_text_splitters.character import CharacterTextSplitter
from langchain_openai.embeddings import OpenAIEmbeddings
import numpy as np
from dotenv import load_dotenv

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
# Configure the model that converts text into numerical vectors.
embedding = OpenAIEmbeddings(model = "text-embedding-3-small")
# Inspect three sample chunks; the selected indexes require at least 19 chunks.
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


# Request embeddings for the three samples through the OpenAI API.
vector1 = embedding.embed_query(pages_char_split[3].page_content)
vector2 = embedding.embed_query(pages_char_split[5].page_content)
vector3 = embedding.embed_query(pages_char_split[18].page_content)

# Compare vector dimensions, which should match for the same embedding model.
print(len(vector1), len(vector2), len(vector3))
print("-------------------------------------------------------------------------------")
# Pairwise dot products equal cosine similarity when the vectors have unit length.
print(np.dot(vector1, vector2), np.dot(vector1, vector3), np.dot(vector2, vector3))
print("-------------------------------------------------------------------------------")
# Check whether the vector lengths are approximately one (unit-normalized).
print(np.linalg.norm(vector1), np.linalg.norm(vector2), np.linalg.norm(vector3))
print("-------------------------------------------------------------------------------")


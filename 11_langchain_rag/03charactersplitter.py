# Example: Split Word document text into smaller chunks for retrieval.
from langchain_community.document_loaders import Docx2txtLoader
from langchain_text_splitters.character import CharacterTextSplitter
from pathlib import Path

# Resolve the input document relative to this script.
doc_Path = Path(__file__).with_name("Introduction_to_Data_and_Data_Science.docx")


# Load the Word document as LangChain Documents.
loader = Docx2txtLoader(doc_Path)
pages = loader.load()
# Collapse repeated whitespace, including newlines and tabs, into single spaces.
for i in range(len(pages)):
    pages[i].page_content = ' '.join(pages[i].page_content.split())

print("----------------------------------------------------------------------")
print("----------------------------------------------------------------------")
# Display the first loaded document's character count.
print(len(pages[0].page_content))

# Optional alternative: an empty separator splits text into individual characters.
# print("Split with space!!!")
# char_splitter = CharacterTextSplitter(separator = "", 
#                                       chunk_size = 500, 
#                                       chunk_overlap = 50)

# Use periods as the chunk boundaries.
print("Split with .!!!")
# Target 500-character chunks at period boundaries with 50-character overlap.
# Segments without suitable boundaries can exceed the target size.
char_splitter = CharacterTextSplitter(separator = ".", 
                                      chunk_size = 500, 
                                      chunk_overlap = 50)

# Split the text while retaining each source section's metadata.
pages_char_split = char_splitter.split_documents(pages)
print(f"Number of chunks:: {len(pages_char_split)}")
print("----------------------------------------------------------------------")
print("----------------------------------------------------------------------")
# Inspect the first chunk's text.
print("----------------------------------------------------------------------")
print("----------------------------------------------------------------------")
print("First Chunk !!!!!!!!!!!!!!!!!!!!!!!!!")
print(pages_char_split[0].page_content)
print("----------------------------------------------------------------------")
print("----------------------------------------------------------------------")
print("Second Chunk !!!!!!!!!!!!!!!!!!!!!!!!!")
print(pages_char_split[1].page_content)


# print(8259/500)
# print(0.518*500)
# Inspect the seventeenth chunk; this assumes at least 17 chunks were produced.
print(f"Last chunk size :{len(pages_char_split[16].page_content)}")

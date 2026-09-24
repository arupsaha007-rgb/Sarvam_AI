from langchain_community.document_loaders import Docx2txtLoader
from langchain_text_splitters.character import CharacterTextSplitter
from pathlib import Path

doc_Path = Path(__file__).with_name("Introduction_to_Data_and_Data_Science.docx")


loader = Docx2txtLoader(doc_Path)
pages = loader.load()
for i in range(len(pages)):
    pages[i].page_content = ' '.join(pages[i].page_content.split())

print("----------------------------------------------------------------------")
print("----------------------------------------------------------------------")
print(len(pages[0].page_content))

# # split wih space
# print("Split with space!!!")
# char_splitter = CharacterTextSplitter(separator = "", 
#                                       chunk_size = 500, 
#                                       chunk_overlap = 50)

# split wih .
print("Split with .!!!")
char_splitter = CharacterTextSplitter(separator = ".", 
                                      chunk_size = 500, 
                                      chunk_overlap = 50)

pages_char_split = char_splitter.split_documents(pages)
print(f"Number of chunks:: {len(pages_char_split)}")
print("----------------------------------------------------------------------")
print("----------------------------------------------------------------------")
print(pages_char_split[0].page_content)

# print(8259/500)
# print(0.518*500)
print(len(pages_char_split[16].page_content))

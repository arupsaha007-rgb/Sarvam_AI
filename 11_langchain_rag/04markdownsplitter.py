from langchain_community.document_loaders import Docx2txtLoader
from langchain_text_splitters.markdown import MarkdownHeaderTextSplitter
from pathlib import Path

doc_Path = Path(__file__).with_name("Introduction_to_Data_and_Data_Science_2.docx")


loader = Docx2txtLoader(doc_Path)
pages = loader.load()
# print(pages)

print("----------------------------------------------------------------------")
print("----------------------------------------------------------------------")
md_splitter = MarkdownHeaderTextSplitter(headers_to_split_on = [("#", "Course Title"), 
                                                                ("##", "Lecture Title")])

pages_md_split = md_splitter.split_text(pages[0].page_content)

print(pages_md_split)
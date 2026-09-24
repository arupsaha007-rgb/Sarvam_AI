from langchain_community.document_loaders import Docx2txtLoader
from pathlib import Path

doc_Path = Path(__file__).with_name("Introduction_to_Data_and_Data_Science.docx")
print(f"Loading file from {doc_Path}")
loader_docx = Docx2txtLoader(doc_Path)

pages_docx = loader_docx.load()

print(pages_docx)
# Example: Extract text and metadata from a Word document.
# Use LangChain's loader to extract text from a Word (.docx) document.
from langchain_community.document_loaders import Docx2txtLoader
from pathlib import Path

# Resolve the document relative to this script, regardless of the working directory.
doc_Path = Path(__file__).with_name("Introduction_to_Data_and_Data_Science.docx")
# Display the resolved path to show which file is being loaded.
print(f"Loading file from {doc_Path}")
# Create a loader for the Word document.
loader_docx = Docx2txtLoader(doc_Path)

# Load the document's text and source metadata into a list of LangChain Documents.
# This loader treats the file as one document rather than splitting it into pages.
pages_docx = loader_docx.load()

# Display the extracted content and its metadata.
print(pages_docx)

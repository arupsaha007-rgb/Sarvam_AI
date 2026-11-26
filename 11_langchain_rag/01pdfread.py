# Example: Load a PDF and compare original text with whitespace-normalized text.
# Install the PDF loader and its PDF parsing dependency:
# pip install langchain-community pypdf
from pathlib import Path
import copy

from langchain_community.document_loaders import PyPDFLoader
# Resolve the PDF relative to this script so it can be run from any directory.
pdf_path = Path(__file__).with_name("Introduction_to_Data_and_Data_Science.pdf")
# PyPDFLoader expects the file path as a string.
loader_pdf = PyPDFLoader(str(pdf_path))


# Load each PDF page as a LangChain Document with text and page metadata.
pages_pdf = loader_pdf.load()
# Display the page count and the complete list of loaded documents.
print("---------------------------------------------------------------------------------")
print(f"Length of pdf {len(pages_pdf)}")
print("---------------------------------------------------------------------------------")
print("Contents!!!!!!!!!!!")
print(pages_pdf)
print("---------------------------------------------------------------------------------")
# Deep-copy the documents so text cleanup leaves the original pages unchanged.
pages_pdf_cut = copy.deepcopy(pages_pdf)

for doc in pages_pdf_cut:
    # Collapse repeated whitespace (including newlines and tabs) into single spaces.
    doc.page_content = " ".join(doc.page_content.split())

# print(pages_pdf_cut)

print("---------------------------------------------------------------------------------")

# Compare the first page's original text with its whitespace-normalized copy.
# These indexes assume the PDF contains at least one page.
print(pages_pdf[0].page_content)
print("---------------------------------------------------------------------------------")
print(pages_pdf_cut[0].page_content)








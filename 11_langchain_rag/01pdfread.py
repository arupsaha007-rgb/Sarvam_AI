# pip install langchain-community pypdf
from pathlib import Path
import copy

from langchain_community.document_loaders import PyPDFLoader

pdf_path = Path(__file__).with_name("Introduction_to_Data_and_Data_Science.pdf")
loader_pdf = PyPDFLoader(str(pdf_path))


pages_pdf = loader_pdf.load()
print(f"Length of pdf {len(pages_pdf)}")

print(pages_pdf)

pages_pdf_cut = copy.deepcopy(pages_pdf)
# ' '.join(pages_pdf_cut[0].page_content.split())

for doc in pages_pdf_cut:
    doc.page_content = " ".join(doc.page_content.split())

# print(pages_pdf_cut)

print("---------------------------------------------------------------------------------")

print(pages_pdf[0].page_content, pages_pdf_cut[0].page_content)








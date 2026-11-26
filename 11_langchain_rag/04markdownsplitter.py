# Example: Split extracted Word text using Markdown-style heading markers.
from langchain_community.document_loaders import Docx2txtLoader
from langchain_text_splitters.markdown import MarkdownHeaderTextSplitter
from pathlib import Path

# Locate the source document beside this script.
doc_Path = Path(__file__).with_name("Introduction_to_Data_and_Data_Science_2.docx")


# Extract document text, including any literal # and ## heading markers.
loader = Docx2txtLoader(doc_Path)
pages = loader.load()
# print(pages)

print("----------------------------------------------------------------------")
print("----------------------------------------------------------------------")
# Split on literal Markdown headings and retain course/lecture names as metadata.
# This reads text markers, not Word heading styles.
md_splitter = MarkdownHeaderTextSplitter(headers_to_split_on = [("#", "Course Title"), 
                                                                ("##", "Lecture Title")])

# Split the first loaded document into sections at the configured headings.
pages_md_split = md_splitter.split_text(pages[0].page_content)

# Display section text and its course/lecture metadata.
print(pages_md_split)
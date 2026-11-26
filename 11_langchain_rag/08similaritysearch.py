# Example: Add a document to Chroma and retrieve text related to a question.
from langchain_openai.embeddings import OpenAIEmbeddings
from langchain_chroma import Chroma
from langchain_core.documents import Document
from dotenv import load_dotenv

# Load API credentials from .env, replacing matching environment variables.
load_dotenv(override=True)

# Open AI Embedding model
# Use the same embedding model as the stored collection to compare vectors.
embedding = OpenAIEmbeddings(model = "text-embedding-3-small")

# Open the local collection using a path relative to the working directory.
vectorstore = Chroma(persist_directory = "./intro-to-ds-lectures", 
                     embedding_function = embedding)

# Attach course and lecture metadata to the sample text for later display.
added_document = Document(page_content='Alright! So… How are the techniques used in data, business intelligence, or predictive analytics applied in real life? Certainly, with the help of computers. You can basically split the relevant tools into two categories—programming languages and software. Knowing a programming language enables you to devise programs that can execute specific operations. Moreover, you can reuse these programs whenever you need to execute the same action', 
                          metadata={'Course Title': 'Introduction to Data and Data Science', 
                                    'Lecture Title': 'Programming Languages & Software Employed in Data Science - All the Tools You Need'})

# Embed and persist the sample through OpenAI, then print its generated ID.
# Each run inserts another copy because no fixed document ID is supplied.
print(vectorstore.add_documents([added_document]))
# Define the natural-language query to embed and compare with stored chunks.
question = "What programming languages do data scientists use?"
print(question)

# Return up to five documents closest to the query embedding.
retrieved_docs = vectorstore.similarity_search(query = question, 
                                               k = 5)

# Display each match and its lecture title; this assumes that metadata key exists.
for i in retrieved_docs:
    print(f"Page Content: {i.page_content}\n----------\nLecture Title:{i.metadata['Lecture Title']}\n")


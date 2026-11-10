from langchain_openai.embeddings import OpenAIEmbeddings
from langchain_chroma import Chroma
from langchain_core.documents import Document
from dotenv import load_dotenv

load_dotenv(override=True)

# Open AI Embedding model
embedding = OpenAIEmbeddings(model = "text-embedding-3-small")

vectorstore = Chroma(persist_directory = "./intro-to-ds-lectures", 
                     embedding_function = embedding)

added_document = Document(page_content='Alright! So… How are the techniques used in data, business intelligence, or predictive analytics applied in real life? Certainly, with the help of computers. You can basically split the relevant tools into two categories—programming languages and software. Knowing a programming language enables you to devise programs that can execute specific operations. Moreover, you can reuse these programs whenever you need to execute the same action', 
                          metadata={'Course Title': 'Introduction to Data and Data Science', 
                                    'Lecture Title': 'Programming Languages & Software Employed in Data Science - All the Tools You Need'})

print(vectorstore.add_documents([added_document]))
question = "What programming languages do data scientists use?"
print(question)

retrieved_docs = vectorstore.similarity_search(query = question, 
                                               k = 5)

for i in retrieved_docs:
    print(f"Page Content: {i.page_content}\n----------\nLecture Title:{i.metadata['Lecture Title']}\n")


from dotenv import load_dotenv
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import WebBaseLoader
from langchain_community.vectorstores import Chroma
from langchain.embeddings import HuggingFaceEmbeddings

load_dotenv()

urls = [
    "https://www.erbakan.edu.tr/tr/sayfa/hakkimizda-genel-bakis",
    "https://erbakan.edu.tr/tr/anasayfa",
    "https://erbakan.edu.tr/tr/sayfa/arastirma-genel-bakis",
]

docs = [WebBaseLoader(url).load() for url in urls]
docs_list = [item for sublist in docs for item in sublist]

text_splitter = RecursiveCharacterTextSplitter.from_tiktoken_encoder(
    chunk_size=250, chunk_overlap=0
)
doc_splits = text_splitter.split_documents(docs_list)

vectorstore = Chroma.from_documents(
     documents=doc_splits,
     collection_name="rag-chroma",
     embedding=HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2"),
     persist_directory="./.chroma_vector_db",
 )

retriever = Chroma(
    collection_name="rag-chroma",
    persist_directory="./.chroma_vector_db",
    embedding_function=HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2"),
).as_retriever()
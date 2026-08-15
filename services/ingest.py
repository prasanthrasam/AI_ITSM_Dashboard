import os
from dotenv import load_dotenv

from langchain_community.document_loaders import PyPDFDirectoryLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma

print("🚀 Starting document ingestion...")

# Load .env
load_dotenv()

# Folder containing PDFs
DOCUMENT_PATH = "documents"

# Chroma database folder
DB_PATH = "chroma_db"

# Check folder exists
if not os.path.exists(DOCUMENT_PATH):
    raise FileNotFoundError(f"Folder '{DOCUMENT_PATH}' not found!")

# Load PDFs
loader = PyPDFDirectoryLoader(DOCUMENT_PATH)
documents = loader.load()

print(f"✅ Loaded {len(documents)} pages")

# Split documents
splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200
)

chunks = splitter.split_documents(documents)

print(f"✅ Created {len(chunks)} chunks")

# Create embeddings
embeddings = OpenAIEmbeddings(
    model="text-embedding-3-small"
)

# Create Chroma database
vectordb = Chroma.from_documents(
    documents=chunks,
    embedding=embeddings,
    persist_directory=DB_PATH
)

print("🎉 ChromaDB created successfully!")
print(f"Database stored in: {DB_PATH}")
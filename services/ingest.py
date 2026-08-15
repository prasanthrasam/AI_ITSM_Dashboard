import os

from dotenv import load_dotenv

from langchain_community.document_loaders import PyPDFDirectoryLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma


load_dotenv()

DOCUMENT_PATH = "documents"
DB_PATH = "chroma_db"


def ingest_documents():

    print("🚀 Starting document ingestion...")

    # ------------------------------------------------------
    # Check documents folder
    # ------------------------------------------------------

    if not os.path.exists(DOCUMENT_PATH):
        raise FileNotFoundError(
            f"Folder '{DOCUMENT_PATH}' not found!"
        )

    # ------------------------------------------------------
    # Check PDF files
    # ------------------------------------------------------

    pdf_files = [
        f for f in os.listdir(DOCUMENT_PATH)
        if f.lower().endswith(".pdf")
    ]

    if not pdf_files:
        raise FileNotFoundError(
            "No PDF files found in documents folder!"
        )

    print(f"📄 Found {len(pdf_files)} PDF file(s)")

    # ------------------------------------------------------
    # Load PDFs
    # ------------------------------------------------------

    loader = PyPDFDirectoryLoader(DOCUMENT_PATH)

    documents = loader.load()

    print(f"✅ Loaded {len(documents)} pages")

    if not documents:
        raise ValueError("No content found in PDF files.")

    # ------------------------------------------------------
    # Split documents
    # ------------------------------------------------------

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )

    chunks = splitter.split_documents(documents)

    print(f"✅ Created {len(chunks)} chunks")

    # ------------------------------------------------------
    # Create embeddings
    # ------------------------------------------------------

    embeddings = OpenAIEmbeddings(
        model="text-embedding-3-small"
    )

    # ------------------------------------------------------
    # Create Chroma database
    # ------------------------------------------------------

    vectordb = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory=DB_PATH
    )

    print("🎉 ChromaDB created successfully!")

    print(
        f"Database stored in: {DB_PATH}"
    )

    return len(chunks)
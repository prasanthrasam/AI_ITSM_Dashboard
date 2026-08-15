from dotenv import load_dotenv

from langchain_community.vectorstores import Chroma
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

# ==========================================================
# Load Embedding Model
# ==========================================================
embedding = OpenAIEmbeddings(
    model="text-embedding-3-small"
)

# ==========================================================
# Load Chroma Database
# ==========================================================
vectordb = Chroma(
    persist_directory="chroma_db",
    embedding_function=embedding
)

# ==========================================================
# Retriever
# ==========================================================
retriever = vectordb.as_retriever(
    search_type="mmr",
    search_kwargs={
        "k": 5,
        "fetch_k": 20
    }
)

# ==========================================================
# Prompt Template
# ==========================================================
PROMPT = """
You are an expert IT Service Management (ITSM) AI Assistant.

Use ONLY the provided context to answer the user's question.

Instructions:
- Answer only from the provided context.
- If the answer exists, explain it clearly and professionally.
- If the answer is partially available, answer with the available information.
- Only reply with:
"I couldn't find that information in the uploaded documents."
if the context truly does not contain the answer.

Context:
{context}

Question:
{question}

Answer:
"""

prompt = ChatPromptTemplate.from_template(PROMPT)

# ==========================================================
# LLM
# ==========================================================
llm = ChatOpenAI(
    model="gpt-4o",
    temperature=0
)

# ==========================================================
# RAG Function
# ==========================================================
def ask_rag(question: str):

    docs = retriever.invoke(question)

    print("\n" + "=" * 80)
    print("QUESTION:")
    print(question)
    print("=" * 80)

    print(f"\nRetrieved {len(docs)} document(s)\n")

    if not docs:
        return (
            "I couldn't find that information in the uploaded documents.",
            []
        )

    # ------------------------------------------------------
    # Print retrieved chunks for debugging
    # ------------------------------------------------------
    for i, doc in enumerate(docs):

        print(f"\n---------- DOCUMENT {i+1} ----------")

        page = doc.metadata.get("page", "Unknown")

        print(f"Page : {page}")
        print(doc.page_content[:1000])

    print("\n" + "=" * 80)

    # ------------------------------------------------------
    # Combine retrieved context
    # ------------------------------------------------------
    context = "\n\n".join(
        doc.page_content
        for doc in docs
    )

    # ------------------------------------------------------
    # Invoke LLM
    # ------------------------------------------------------
    chain = prompt | llm

    response = chain.invoke(
        {
            "context": context,
            "question": question
        }
    )

    return response.content, docs
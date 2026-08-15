from dotenv import load_dotenv
from langchain_community.vectorstores import Chroma
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

DB_PATH = "chroma_db"

embedding = OpenAIEmbeddings(
    model="text-embedding-3-small"
)


def get_retriever():

    vectordb = Chroma(
        persist_directory=DB_PATH,
        embedding_function=embedding
    )

    return vectordb.as_retriever(
        search_type="similarity",
        search_kwargs={"k": 5}
    )


PROMPT = """
You are an ITSM Knowledge Assistant.

Use ONLY the information provided in the context.

If the answer is not present in the context, say:

"I couldn't find that information in the uploaded documents."

Context:
{context}

Question:
{question}
"""

prompt = ChatPromptTemplate.from_template(PROMPT)

llm = ChatOpenAI(
    model="gpt-4o",
    temperature=0
)


def ask_rag(question: str):

    retriever = get_retriever()

    docs = retriever.invoke(question)

    print("\n" + "=" * 80)
    print("QUESTION:")
    print(question)
    print("=" * 80)

    print(f"Retrieved {len(docs)} document(s)")

    if not docs:
        return (
            "I couldn't find that information in the uploaded documents.",
            []
        )

    context = "\n\n".join(
        doc.page_content
        for doc in docs
    )

    response = (prompt | llm).invoke(
        {
            "context": context,
            "question": question
        }
    )

    return response.content, docs
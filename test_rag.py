from services.rag_service import ask_rag

while True:

    question = input("\nAsk your question (type 'exit' to quit): ")

    if question.lower() == "exit":
        break

    answer, docs = ask_rag(question)

    print("\n" + "=" * 60)
    print("ANSWER")
    print("=" * 60)
    print(answer)

    print("\nRetrieved Documents")
    print("=" * 60)

    for i, doc in enumerate(docs, start=1):
        print(f"{i}. {doc.metadata.get('source')}")
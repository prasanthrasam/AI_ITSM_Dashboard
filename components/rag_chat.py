import streamlit as st
from services.rag_service import ask_rag


def rag_chat():

    st.markdown("---")
    st.subheader("💬 AI Knowledge Assistant")

    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Display chat history
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # User input
    question = st.chat_input("Ask anything about ITSM...")

    if question:

        # Show user message
        st.session_state.messages.append(
            {"role": "user", "content": question}
        )

        with st.chat_message("user"):
            st.markdown(question)

        # Generate response
        with st.spinner("Searching knowledge base..."):

            answer, docs = ask_rag(question)

            sources = []

            for doc in docs:
                source = doc.metadata.get("source", "")
                filename = source.split("\\")[-1]
                if filename not in sources:
                    sources.append(filename)

            response = answer

            if sources:
                response += "\n\n---\n**📄 Sources**\n"

                for s in sources:
                    response += f"- {s}\n"

        # Save response
        st.session_state.messages.append(
            {"role": "assistant", "content": response}
        )

        with st.chat_message("assistant"):
            st.markdown(response)

    st.write("")

    if st.button("🗑 Clear Chat"):
        st.session_state.messages = []
        st.rerun()
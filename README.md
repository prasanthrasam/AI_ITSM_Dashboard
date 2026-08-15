# 🤖 AI-Powered ITSM Knowledge Assistant

[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://ai-itsm-dashboard.streamlit.app/)

An AI-powered **IT Service Management (ITSM) Knowledge Assistant** built using **Retrieval-Augmented Generation (RAG)**.

The application allows users to ask ITSM-related questions in natural language and receive answers grounded in uploaded ITSM knowledge documents.

---

## 🚀 Live Application

### 🌐 Streamlit Cloud

👉 **https://ai-itsm-dashboard.streamlit.app/**

Try questions such as:

- What is an incident?
- What is a problem?
- What is the difference between Incident and Problem Management?
- What is a P1 incident?
- What is Root Cause Analysis?
- What is MTTR?
- What is a standard change?

---

## 📌 Project Objective

Traditional ITSM knowledge management often requires service desk analysts to manually search through large documentation repositories.

This project demonstrates how **Generative AI + RAG** can be used to create an intelligent ITSM knowledge assistant.

The solution can:

1. Understand natural-language questions.
2. Search relevant ITSM knowledge.
3. Retrieve the most relevant document content.
4. Provide the retrieved context to an LLM.
5. Generate a concise, grounded answer.
6. Avoid generating unsupported information when the answer is not available in the knowledge base.

---

# 🏗️ Solution Architecture

```text
                         ┌─────────────────────────┐
                         │       ITSM PDF          │
                         │                         │
                         │ Incident Management     │
                         │ Problem Management      │
                         │ Change Management       │
                         │ RCA / ITSM Metrics      │
                         └────────────┬────────────┘
                                      │
                                      ▼
                         ┌─────────────────────────┐
                         │      PDF Loader         │
                         │                         │
                         │ PyPDFDirectoryLoader    │
                         └────────────┬────────────┘
                                      │
                                      ▼
                         ┌─────────────────────────┐
                         │     Text Splitting      │
                         │                         │
                         │ Chunk Size: 1500        │
                         │ Overlap: 300            │
                         └────────────┬────────────┘
                                      │
                                      ▼
                         ┌─────────────────────────┐
                         │   OpenAI Embeddings     │
                         │                         │
                         │ text-embedding-3-small  │
                         └────────────┬────────────┘
                                      │
                                      ▼
                         ┌─────────────────────────┐
                         │       ChromaDB          │
                         │                         │
                         │ Vector Database         │
                         └────────────┬────────────┘
                                      │
                                      │
                    User Question    │
                         │            │
                         ▼            │
                ┌────────────────┐    │
                │ Streamlit Chat │    │
                │      UI        │    │
                └───────┬────────┘    │
                        │             │
                        ▼             │
                ┌────────────────┐    │
                │ Similarity     │◄───┘
                │ Search         │
                └───────┬────────┘
                        │
                        ▼
                ┌────────────────┐
                │ Relevant       │
                │ Document       │
                │ Chunks         │
                └───────┬────────┘
                        │
                        ▼
                ┌────────────────┐
                │ RAG Prompt     │
                │ Context +      │
                │ Question       │
                └───────┬────────┘
                        │
                        ▼
                ┌────────────────┐
                │ OpenAI GPT-4o  │
                │ LLM            │
                └───────┬────────┘
                        │
                        ▼
                ┌────────────────┐
                │ Grounded ITSM  │
                │ Answer         │
                └────────────────┘

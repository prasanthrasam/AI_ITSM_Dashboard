# 📊 ITSM Dashboard

The application provides an interactive ITSM dashboard in addition to the AI Knowledge Assistant.

The dashboard is designed to provide a consolidated view of ITSM operational performance and trends.

## Dashboard Capabilities

The dashboard provides:

- 📌 ITSM KPI cards
- 📊 Incident analysis
- 📈 Trend visualizations
- 📉 Performance analysis
- 🔎 Interactive filtering
- 📋 Operational data views
- 📊 Plotly-based charts
- 🤖 AI-powered ITSM knowledge assistance

## Dashboard Workflow

```text
ITSM Data
    |
    v
Data Processing
    |
    v
Pandas
    |
    v
KPI Calculation
    |
    +-------------------+
    |                   |
    v                   v
KPI Cards          Plotly Charts
    |                   |
    +---------+---------+
              |
              v
       Streamlit Dashboard


AI Knowledge Assistant Workflow

ITSM Documents
      |
      v
PDF Loader
      |
      v
Text Chunking
      |
      v
OpenAI Embeddings
      |
      v
ChromaDB
      |
      |
User Question
      |
      v
Similarity Search
      |
      v
Relevant Context
      |
      v
RAG Prompt
      |
      v
GPT-4o
      |
      v
Grounded ITSM Answer


🏗️ Complete Platform Architecture

                         ITSM AI PLATFORM
                              |
          +-------------------+-------------------+
          |                                       |
          ▼                                       ▼
   ITSM DASHBOARD                         AI KNOWLEDGE ASSISTANT
          |                                       |
          ▼                                       ▼
    ITSM Data Sources                       ITSM Documents
          |                                       |
          ▼                                       ▼
    Data Processing                          PDF Loader
          |                                       |
          ▼                                       ▼
       Pandas                               Text Chunking
          |                                       |
          ▼                                       ▼
   KPI Calculation                      OpenAI Embeddings
          |                                       |
          ▼                                       ▼
    Plotly Charts                            ChromaDB
          |                                       |
          |                                  User Question
          |                                       |
          |                                       ▼
          |                                  Similarity
          |                                   Search
          |                                       |
          |                                       ▼
          |                                  RAG Context
          |                                       |
          |                                       ▼
          |                                    GPT-4o
          |                                       |
          |                                       ▼
          |                                  AI Response
          |                                       |
          +-------------------+-------------------+
                              |
                              ▼
                       STREAMLIT APPLICATION
                              |
                              ▼
                    STREAMLIT CLOUD DEPLOYMENT

🔹 Technology Stack

Python | Streamlit | Pandas | Plotly | LangChain | OpenAI | ChromaDB | RAG | GitHub | Streamlit Cloud

Author: Prasanth Rasam
ITSM | Service Management | Data Analytics | Generative AI | RAG

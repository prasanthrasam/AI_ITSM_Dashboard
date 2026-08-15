AI-POWERED ITSM DASHBOARD & RAG KNOWLEDGE ASSISTANT

**LIVE APPLICATION**
Streamlit: https://ai-itsm-dashboard.streamlit.app/
GitHub: https://github.com/prasanthrasam/AI_ITSM_Dashboard

(Use the Excel file placed in "data" folder to upload)

**PROJECT OVERVIEW**
This project is an AI-powered IT Service Management (ITSM) platform combining an interactive ITSM dashboard with KPI cards, graphical analytics, trend analysis, and an AI-powered RAG Knowledge Assistant.

**KEY CAPABILITIES**
•	Interactive ITSM Dashboard
•	KPI cards and operational metrics
•	Interactive Plotly graphs and trend analysis
•	ITSM performance visualization
•	AI-powered ITSM Knowledge Assistant
•	Retrieval-Augmented Generation (RAG)
•	PDF knowledge-base ingestion
•	Semantic similarity search
•	OpenAI GPT-4o
•	OpenAI text-embedding-3-small
•	ChromaDB vector database
•	Streamlit Cloud deployment

**SOLUTION ARCHITECTURE**

                         AI-POWERED ITSM PLATFORM
                                  |
                 +----------------+----------------+
                 |                                 |
                 v                                 v
          ITSM DASHBOARD                    AI KNOWLEDGE
                                            ASSISTANT
                 |                                 |
                 v                                 v
          ITSM Data Sources                  ITSM PDF Documents
                 |                                 |
                 v                                 v
             Pandas                         PDF Loader
                 |                                 |
                 v                                 v
        Data Processing                    Text Chunking
                 |                                 |
                 v                                 v
        KPI Calculations                OpenAI Embeddings
                 |                                 |
          +------+-------+                         v
          |              |                      ChromaDB
          v              v                         |
       KPI Cards      Plotly Graphs                |
          |              |                    User Question
          +------+-------+                         |
                 |                                 v
                 |                         Similarity Search
                 |                                 |
                 |                                 v
                 |                         Relevant Context
                 |                                 |
                 |                                 v
                 |                              GPT-4o
                 |                                 |
                 |                                 v
                 |                          AI ITSM Answer
                 |                                 |
                 +---------------+-----------------+
                                 |
                                 v
                         STREAMLIT APPLICATION
                                 |
                                 v
                         STREAMLIT CLOUD

I**TSM DASHBOARD**
The dashboard provides a visual view of ITSM operational data and performance.

**Dashboard capabilities:**
•	KPI cards
•	Interactive charts
•	Trend analysis
•	Performance visualization
•	Data filtering
•	Operational data analysis
•	Plotly-based graphs
•	ITSM performance insights

**Dashboard workflow:**

ITSM Data
  ↓
Data Processing using Pandas
  ↓
KPI Calculation
  ↓
Performance Analysis
  ↓
Plotly Visualizations
  ↓
Interactive Streamlit Dashboard

The dashboard transforms ITSM data into meaningful operational insights through KPIs, trends, and graphical analysis.

**AI KNOWLEDGE ASSISTANT**
The second major component is a RAG-based ITSM Knowledge Assistant.

**Example questions:**
•	What is an incident?
•	What is a problem?
•	What is a P1 incident?
•	What is the difference between Incident and Problem Management?
•	What is the incident management lifecycle?

**RAG WORKFLOW**

ITSM PDF DOCUMENTS
        ↓
PDF Loader
        ↓
Text Extraction
        ↓
Text Chunking (1500 / 300)
        ↓
OpenAI Embeddings
(text-embedding-3-small)
        ↓
ChromaDB Vector Database
        ↓
User Question
        ↓
Semantic Similarity Search
        ↓
Relevant Document Chunks
        ↓
RAG Prompt
        ↓
GPT-4o
        ↓
Grounded ITSM Answer

**GROUNDED AI RESPONSE**
The assistant is instructed to use only information retrieved from the uploaded ITSM documents.

If the answer is not available in the retrieved context, it responds:
"I couldn't find that information in the uploaded documents."

This helps keep the assistant focused on the knowledge base and reduce unsupported answers.

**TECHNOLOGY STACK**
•	Python – application development
•	Streamlit – web application and dashboard
•	Pandas – data processing and analytics
•	Plotly – interactive graphs and visualizations
•	LangChain – RAG orchestration
•	OpenAI – embeddings and LLM
•	GPT-4o – natural-language response generation
•	text-embedding-3-small – document embeddings
•	ChromaDB – vector database
•	PyPDF – PDF processing
•	GitHub – source-code management
•	Streamlit Cloud – cloud deployment

**PROJECT STRUCTURE
**
AI_ITSM_Dashboard/
│
├── app.py
├── services/
│   ├── ingest.py
│   └── rag_service.py
├── components/
│   └── rag_chat.py
├── documents/
│   └── ITSM_RAG_Test_Sample.pdf
├── chroma_db/
├── requirements.txt
├── .gitignore
├── README.md
└── .env

Note: chroma_db/ and .env are excluded from GitHub through .gitignore.

**END-TO-END APPLICATION WORKFLOW**

                    USER
                      |
             +--------+--------+
             |                 |
             v                 v
       View Dashboard      Ask AI Question
             |                 |
             v                 v
        ITSM Analytics     Vector Search
             |                 |
             v                 v
       KPI + Graphs       Relevant Context
             |                 |
             |                 v
             |               GPT-4o
             |                 |
             |                 v
             |            AI ITSM Answer
             |                 |
             +--------+--------+
                      |
                      v
              Streamlit Interface

CLOUD DEPLOYMENT

GitHub Repository
       ↓
Streamlit Cloud
       ↓
Python Environment
       ↓
Install requirements.txt
       ↓
Load Streamlit Secrets
       ↓
Run app.py
       ↓
Live ITSM Dashboard + AI Assistant

OpenAI API credentials are stored securely using Streamlit Secrets and are not hard-coded in the application.

**SECURITY**
•	API keys are not stored in source code.
•	Local configuration uses environment variables.
•	Cloud configuration uses Streamlit Secrets.
•	The OpenAI API key should never be committed to GitHub.

**ITSM USE CASES**
•	Incident Management
•	Problem Management
•	Change Management
•	ITSM KPI monitoring
•	Operational performance analysis
•	Knowledge Management
•	Service Desk analytics
•	Incident trend analysis
•	ITSM process knowledge retrieval
•	AI-assisted service management

**BUSINESS VALUE**

Traditional ITSM Analytics:
ITSM Data → Pandas → KPIs → Graphs → Operational Insights

**AI Knowledge Management:**
ITSM Documents → Embeddings → Vector Database → RAG → GPT-4o → Knowledge Answer

**Combined solution:**
ITSM Data + ITSM Knowledge
        ↓
AI-Powered ITSM Platform
        ↓
Dashboard + RAG Assistant
        ↓
KPIs, Graphs and AI Answers
        ↓
Better ITSM Insights

**TESTING**
The RAG assistant was tested with:
•	What is an incident? – Correct
•	What is a problem? – Correct
•	What is the difference between incident and problem management? – Correct
•	What is a P1 incident? – Correct
•	What is the incident management lifecycle? – Correct

The application was tested locally and on Streamlit Cloud.

L**OCAL SETUP**

git clone https://github.com/prasanthrasam/AI_ITSM_Dashboard.git
cd AI_ITSM_Dashboard

python -m venv venv
venv\Scripts\activate

pip install -r requirements.txt

Configure .env:
OPENAI_API_KEY=your_api_key

Run:
streamlit run app.py

KNOWLEDGE BASE CREATION

PDF
 ↓
Text Extraction
 ↓
Chunking
 ↓
OpenAI Embeddings
 ↓
ChromaDB

**Current configuration:**
•	Chunk size: 1500
•	Chunk overlap: 300
•	Embedding model: text-embedding-3-small
•	Vector database: ChromaDB
•	Retrieval: Similarity Search
•	Retrieved documents: Top 5
•	LLM: GPT-4o

**FUTURE ENHANCEMENTS**
•	Real-time ITSM data integration
•	ServiceNow integration
•	Incident prediction
•	Automated RCA generation
•	AI-based incident classification
•	Problem identification
•	Change risk prediction
•	SLA breach prediction
•	Agentic AI workflows
•	Voice-based ITSM assistant
•	Role-based dashboards
•	Advanced ITSM analytics
•	Feedback-based RAG improvement

**KEY LEARNING OUTCOMES**
•	ITSM process knowledge
•	Data analytics
•	Python programming
•	Pandas
•	Data visualization
•	Streamlit application development
•	Generative AI
•	Retrieval-Augmented Generation
•	Vector databases
•	LangChain
•	OpenAI APIs
•	Cloud deployment
•	GitHub
•	AI-assisted knowledge management

**AUTHOR**
Prasanth Rasam

ITSM | Service Management | Data Analytics | Python | Generative AI | RAG | Agentic AI | Lean Six Sigma

**PROJECT LINKS**
Live Streamlit Application:
https://ai-itsm-dashboard.streamlit.app/

GitHub Repository:
https://github.com/prasanthrasam/AI_ITSM_Dashboard

PROJECT STATUS
Completed and deployed successfully on Streamlit Cloud.

This project demonstrates how ITSM operational dashboards, analytics, and Generative AI/RAG can be combined into one practical enterprise-style solution.

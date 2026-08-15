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
End-to-End Workflow
1️⃣ Document Ingestion

The application reads ITSM PDF documents from:

documents/

Example:

documents/
└── ITSM_RAG_Test_Sample.pdf

The document contains ITSM knowledge such as:

Incident Management
Problem Management
Change Management
Incident Prioritization
Impact and Urgency
Root Cause Analysis
ITSM Metrics
Continual Improvement
2️⃣ PDF Loading

The application loads the PDF and converts each page into a document object that can be processed by LangChain.

PDF Document
     ↓
PDF Loader
     ↓
Document Pages
3️⃣ Text Chunking

Large documents are divided into smaller chunks to improve retrieval accuracy.

Current configuration:

Chunk Size   = 1500
Chunk Overlap = 300

Workflow:

Large Document
      ↓
Text Splitting
      ↓
Smaller Chunks

Chunk overlap helps maintain context between adjacent sections.

4️⃣ Generate Embeddings

Each document chunk is converted into a numerical vector using:

OpenAI text-embedding-3-small

Conceptually:

Text
  ↓
Embedding Model
  ↓
Vector Representation

The embedding represents the semantic meaning of the document content.

5️⃣ Store Vectors in ChromaDB

The generated embeddings are stored in:

chroma_db/

ChromaDB acts as the vector database.

It enables semantic similarity search between the user's question and the stored ITSM knowledge.

🔎 User Query Workflow

When a user asks:

What is an incident?

the following process occurs:

User Question
     │
     ▼
"What is an incident?"
     │
     ▼
Generate Query Embedding
     │
     ▼
Search ChromaDB
     │
     ▼
Retrieve Relevant Chunks
     │
     ▼
Build RAG Context
     │
     ▼
Send Context + Question
to GPT-4o
     │
     ▼
Generate Answer
     │
     ▼
Display Answer in Streamlit
🧠 Retrieval-Augmented Generation (RAG)

The project follows the RAG architecture:

               ┌───────────────┐
               │ User Question │
               └───────┬───────┘
                       │
                       ▼
               ┌───────────────┐
               │   Embedding   │
               └───────┬───────┘
                       │
                       ▼
               ┌───────────────┐
               │   ChromaDB    │
               │ Vector Search │
               └───────┬───────┘
                       │
                       ▼
               ┌───────────────┐
               │ Relevant      │
               │ Context       │
               └───────┬───────┘
                       │
                       ▼
             ┌───────────────────┐
             │ RAG Prompt        │
             │ Context + Query   │
             └─────────┬─────────┘
                       │
                       ▼
             ┌───────────────────┐
             │     GPT-4o        │
             │   Generation      │
             └─────────┬─────────┘
                       │
                       ▼
             ┌───────────────────┐
             │ Final ITSM Answer │
             └───────────────────┘
🛡️ Grounded Response Strategy

The RAG prompt instructs the LLM to use only the retrieved context.

If the required information is not available in the uploaded documents, the assistant responds:

I couldn't find that information in the uploaded documents.

This approach helps reduce unsupported or hallucinated responses.

💬 Example
User Question
What is an incident?
AI Assistant Response
An incident is an unplanned interruption to an IT service,
or a reduction in the quality of an IT service.


The primary objective of Incident Management is to restore
normal service operation as quickly as possible and minimize
the impact on users and the business.
🧪 Testing

The application was tested with multiple ITSM questions.

Question	Expected Result
What is an incident?	Incident definition
What is a problem?	Problem definition
What is a P1 incident?	Critical priority
What is impact vs urgency?	Difference explained
What is RCA?	Root Cause Analysis
What is MTTR?	Mean Time to Restore
What is a standard change?	Change definition
Incident vs Problem Management?	Comparison
📁 Project Structure
AI_ITSM_Dashboard/
│
├── app.py
│
├── requirements.txt
├── README.md
├── .gitignore
│
├── documents/
│   └── ITSM_RAG_Test_Sample.pdf
│
├── services/
│   ├── ingest.py
│   └── rag_service.py
│
├── components/
│   └── rag_chat.py
│
├── data/
│   └── Incident_Report.xlsx
│
└── chroma_db/
    └── Generated locally during ingestion

Note: chroma_db/ is excluded from GitHub using .gitignore and is generated during application execution.

📌 Main Components
app.py

Main Streamlit application.

Responsibilities:

Dashboard UI
Navigation
RAG knowledge-base initialization
ITSM assistant interface
Streamlit session management
services/ingest.py

Responsible for document ingestion.

Workflow:

PDF
 ↓
Load
 ↓
Split Text
 ↓
Create Embeddings
 ↓
Store in ChromaDB

The ingestion process creates the vector database from the ITSM knowledge documents.

services/rag_service.py

Responsible for the RAG query pipeline.

Workflow:

Question
 ↓
Similarity Search
 ↓
Retrieve Documents
 ↓
Build Context
 ↓
RAG Prompt
 ↓
GPT-4o
 ↓
Answer
components/rag_chat.py

Responsible for the conversational Streamlit interface.

Features:

Chat input
Conversation history
AI assistant responses
Source display
Clear chat functionality
🧰 Technology Stack
Technology	Purpose
Python	Application development
Streamlit	Web application and UI
LangChain	RAG orchestration
LangChain Chroma	ChromaDB integration
OpenAI	LLM and embeddings
GPT-4o	Answer generation
text-embedding-3-small	Text embeddings
ChromaDB	Vector database
PyPDF	PDF processing
Pandas	Data processing
Plotly	Dashboard visualization
Git	Version control
GitHub	Source code repository
Streamlit Community Cloud	Cloud deployment
🔐 Security

The OpenAI API key is not stored in the source code.

For local development, the API key can be stored in:

.env

Example:

OPENAI_API_KEY=your_openai_api_key

For Streamlit Cloud, the API key is stored securely using Streamlit Secrets.

Example:

OPENAI_API_KEY="your-openai-api-key"

The following sensitive/local files are excluded from Git:

.env
.env.*
.streamlit/secrets.toml
chroma_db/
.venv/
venv/
__pycache__/
☁️ Cloud Deployment Architecture
              GitHub Repository
                     │
                     │ Push
                     ▼
          Streamlit Community Cloud
                     │
                     ▼
          Install requirements.txt
                     │
                     ▼
                Start app.py
                     │
                     ▼
            Load Streamlit Secrets
                     │
                     ▼
              Load ITSM PDF
                     │
                     ▼
               Build ChromaDB
                     │
                     ▼
             Start RAG Assistant
                     │
                     ▼
             Public Web Application
🚀 Local Setup
1. Clone Repository
git clone https://github.com/prasanthrasam/AI_ITSM_Dashboard.git
cd AI_ITSM_Dashboard
2. Create Virtual Environment
python -m venv .venv

Activate the environment on Windows:

.venv\Scripts\activate
3. Install Dependencies
pip install -r requirements.txt
4. Configure OpenAI API Key

Create a .env file in the project root:

OPENAI_API_KEY=your_openai_api_key

Never commit your API key to GitHub.

5. Build the Knowledge Base

Run:

python services\ingest.py

The application will:

Load PDF
   ↓
Split Text
   ↓
Create Embeddings
   ↓
Create ChromaDB
6. Start Streamlit

Run:

streamlit run app.py

The Streamlit application will start locally.

☁️ Streamlit Cloud Deployment

The application is deployed using Streamlit Community Cloud.

Deployment workflow:

GitHub
   │
   ▼
Repository
   │
   ▼
Streamlit Community Cloud
   │
   ├── requirements.txt
   ├── app.py
   ├── documents/
   └── Streamlit Secrets
   │
   ▼
Live RAG Application

The application automatically uses the dependencies specified in requirements.txt.

The OpenAI API key is configured through Streamlit Cloud Secrets.

🌐 Live Demo
AI ITSM Knowledge Assistant

👉 https://ai-itsm-dashboard.streamlit.app/

🔗 GitHub Repository

👉 https://github.com/prasanthrasam/AI_ITSM_Dashboard

📊 Potential ITSM Use Cases

The current architecture can be extended for real-world ITSM environments.

Incident Management
Incident Description
        ↓
RAG Knowledge Search
        ↓
Relevant Knowledge Articles
        ↓
Suggested Resolution
Problem Management
Incident History
       ↓
Pattern Detection
       ↓
Potential Problem
       ↓
RCA Assistance
Service Desk
User Question
      ↓
AI Knowledge Assistant
      ↓
Relevant ITSM Knowledge
      ↓
Suggested Resolution
ITSM Reporting

The same architecture can be extended to answer questions related to:

Incident volume
MTTR
SLA compliance
SLA breaches
Incident backlog
Change success rate
Major incidents
Service availability
Problem trends
Service credits
🔮 Future Enhancements

Potential future enhancements include:

 Multiple ITSM document sources
 Page-level source citations
 Conversation memory
 Incident classification
 Automatic P1-P4 priority recommendation
 Incident summarization
 RCA assistant
 FMEA assistant
 Problem identification
 ITSM dashboard analytics
 Excel/CSV knowledge ingestion
 ServiceNow integration
 Enterprise authentication
 Agentic AI workflow
 Human-in-the-loop approval
 Feedback and answer-quality tracking
 Langfuse observability and tracing
🎯 Key Learning Outcomes

This project demonstrates practical experience with:

Generative AI
LLM integration
Prompt engineering
Grounded generation
Context-aware responses
Retrieval-Augmented Generation
Document ingestion
PDF processing
Text chunking
Embeddings
Vector databases
Similarity search
Context retrieval
Prompt construction
Grounded answer generation
ITSM
Incident Management
Problem Management
Change Management
Root Cause Analysis
Incident Prioritization
Impact and Urgency
ITSM metrics
Continual Improvement
Cloud
GitHub-based deployment
Streamlit Community Cloud
Secrets management
Dependency management
💼 Project Portfolio Description
AI-Powered ITSM Knowledge Assistant using RAG

Built a production-style Retrieval-Augmented Generation (RAG) application using Python, LangChain, OpenAI, ChromaDB and Streamlit to provide grounded ITSM knowledge responses from enterprise documentation.

The solution demonstrates the complete AI knowledge workflow including document ingestion, text chunking, embeddings, vector search, context retrieval, LLM-based response generation and cloud deployment.

🧑‍💻 Author
Prasanth Rasam

ITSM | Service Management | Service Level Management | Lean Six Sigma | Python | Generative AI | RAG | Agentic AI

🔗 Project Links
🌐 Live Streamlit Application

https://ai-itsm-dashboard.streamlit.app/

💻 GitHub Repository

https://github.com/prasanthrasam/AI_ITSM_Dashboard

📚 Streamlit Documentation

https://docs.streamlit.io/

⭐ Project Highlights
ITSM Knowledge
      +
Document Intelligence
      +
OpenAI Embeddings
      +
ChromaDB
      +
RAG
      +
GPT-4o
      +
Streamlit
      +
Cloud Deployment
      =
AI-Powered ITSM Knowledge Assistant
⭐ If you find this project useful

Feel free to explore the repository and try the live application.

Live Demo:
https://ai-itsm-dashboard.streamlit.app/

GitHub:
https://github.com/prasanthrasam/AI_ITSM_Dashboard



**That's the entire README.** You can copy the whole block at once and paste it into `README.md`.

# DocRAG AI — Intelligent Financial Document Analysis & RAG Platform

[![Python](https://img.shields.io/badge/Python-3.11%20%7C%203.12-blue?logo=python&logoColor=white)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.110+-009688?logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![React](https://img.shields.io/badge/React-19.0-61DAFB?logo=react&logoColor=black)](https://react.dev/)
[![TailwindCSS](https://img.shields.io/badge/Tailwind_CSS-v4.0-38B2AC?logo=tailwind-css&logoColor=white)](https://tailwindcss.com/)
[![ChromaDB](https://img.shields.io/badge/Vector_DB-ChromaDB-orange)](https://www.trychroma.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

> **DocRAG AI** is a full-stack, enterprise-grade financial intelligence system engineered to transform dense corporate annual reports (PDFs) into structured, queryable data and interactive analytics. Built with an advanced **Hybrid Retrieval-Augmented Generation (RAG)** pipeline combining semantic embeddings, lexical BM25 retrieval, and neural cross-encoder reranking.

---

## 📑 Table of Contents

- [Overview](#-overview)
- [System Architecture](#-system-architecture)
- [Key Features](#-key-features)
- [Engineering & Technical Highlights](#-engineering--technical-highlights)
  - [1. Document Ingestion & Semantic Chunking](#1-document-ingestion--semantic-chunking)
  - [2. Multi-Stage Hybrid Retrieval](#2-multi-stage-hybrid-retrieval)
  - [3. Financial Metric Extraction & Dual-Format Parsing](#3-financial-metric-extraction--dual-format-parsing)
  - [4. Multi-Tenant User Isolation](#4-multi-tenant-user-isolation)
  - [5. Grounded Q&A Chat Pipeline](#5-grounded-qa-chat-pipeline)
  - [6. Comparative Company Intelligence](#6-comparative-company-intelligence)
- [Technology Stack](#-technology-stack)
- [API Reference](#-api-reference)
- [Project Directory Structure](#-project-directory-structure)
- [Getting Started](#-getting-started)
  - [Prerequisites](#prerequisites)
  - [Backend Setup](#backend-setup)
  - [Frontend Setup](#frontend-setup)
  - [Environment Variables](#environment-variables)
- [Author & Acknowledgments](#-author--acknowledgments)

---

## 💡 Overview

Public company annual reports (such as SEC 10-K filings) often exceed 100 pages, packed with audited income statements, balance sheets, cash flow tables, and qualitative risks. Navigating and cross-analyzing these reports manually is tedious and prone to oversight.

**DocRAG AI** solves this problem by automating the entire lifecycle of financial report comprehension:
1. **Parses complex PDF financial reports** while preserving table integrity into clean Markdown.
2. **Indexes report contents** into dense vector spaces (ChromaDB) and sparse term frequencies (Rank-BM25).
3. **Extracts critical financial KPIs** (Revenue, Net Income, Operating Cash Flow, Total Debt, Operating Margin, R&D Expenses) into normalized relational records.
4. **Visualizes performance** using responsive charts and real-time LLM-generated executive risk/strength syntheses.
5. **Facilitates cross-firm comparison** and contextual, multi-turn conversational Q&A strictly grounded in source documentation.

---

## 🏛️ System Architecture

DocRAG AI employs a decoupled, asynchronous micro-service inspired architecture featuring a React 19 client and a high-throughput FastAPI backend.

```
                         ┌─────────────────────────────────┐
                         │   Modern React 19 UI (Vite)     │
                         │   Tailwind CSS v4 + Chart.js    │
                         └────────────────┬────────────────┘
                                          │  RESTful API / JSON
                                          ▼
                         ┌─────────────────────────────────┐
                         │       FastAPI Gateway           │
                         │   OAuth2 JWT Auth & Security    │
                         └────────────────┬────────────────┘
                                          │
       ┌───────────────────┬──────────────┴───────────────┬───────────────────┐
       ▼                   ▼                              ▼                   ▼
┌──────────────┐   ┌──────────────┐             ┌──────────────────┐   ┌──────────────┐
│ Auth Router  │   │ Upload &     │             │ RAG Chat &       │   │ Dashboard &  │
│ User DB      │   │ Ingestion    │             │ Q&A Engine       │   │ Comparison   │
└──────────────┘   └───────┬──────┘             └─────────┬────────┘   └──────┬───────┘
                           │                              │                   │
                           ▼                              │                   │
                  ┌─────────────────┐                     │                   │
                  │  PyMuPDF4LLM    │                     │                   │
                  │  (Markdown)     │                     │                   │
                  └────────┬────────┘                     │                   │
                           ▼                              │                   │
                  ┌─────────────────┐                     │                   │
                  │ Semantic        │                     │                   │
                  │ Chunking Engine │                     │                   │
                  └────────┬────────┘                     │                   │
                           ▼                              │                   │
          ┌────────────────┴────────────────┐             │                   │
          ▼                                 ▼             │                   │
  ┌───────────────┐                 ┌───────────────┐     │                   │
  │ ChromaDB      │                 │ Rank-BM25     │◄────┤                   │
  │ Dense Vectors │                 │ Sparse Index  │     │                   │
  └───────┬───────┘                 └───────┬───────┘     │                   │
          └────────────────┬────────────────┘             │                   │
                           ▼                              │                   │
                  ┌─────────────────┐                     │                   │
                  │ Hybrid Fusion   │◄────────────────────┘                   │
                  └────────┬────────┘                                         │
                           ▼                                                  │
                  ┌─────────────────┐                                         │
                  │ Cross-Encoder   │ (ms-marco-MiniLM-L-6-v2)                │
                  │ Neural Reranker │                                         │
                  └────────┬────────┘                                         │
                           ▼                                                  │
                  ┌─────────────────┐                                         │
                  │ LLM Generation  │ (OpenAI GPT-4o-mini)                    │
                  └────────┬────────┘                                         │
                           ▼                                                  ▼
                  ┌─────────────────┐                               ┌─────────────────┐
                  │ KPI Parser &    │──────────────────────────────►│ SQLite Database │
                  │ Normalizer      │                               │ Financial Store │
                  └─────────────────┘                               └─────────────────┘
```

---

## ✨ Key Features

- **Automated Financial Report Ingestion**: Upload any corporate annual filing in PDF format with designated company name and fiscal period.
- **Smart Semantic Text Chunking**: Splits markdown-converted documents along topical and structural boundaries rather than arbitrary character cuts, retaining financial table cohesion.
- **Dual Retrieval (Dense + Sparse)**: Bridges semantic conceptual queries with exact numerical/financial phrase lookups via hybrid ChromaDB + BM25 indexing.
- **Neural Re-ranking Pipeline**: Utilizes a lightweight cross-encoder (`ms-marco-MiniLM-L-6-v2`) to score query-document pairs, eliminating irrelevant chunks before feeding context to the LLM.
- **Automated KPI Extraction & Normalization**: Accurately extracts 6 fundamental metrics (Revenue, Net Income, Cash Flow, Debt, Margin, R&D) and automatically normalizes currencies/units (e.g., "$97.69B" $\rightarrow$ `97690000000`) for visualization while retaining raw audited strings.
- **Executive AI Synthesis**: Generates targeted management-style summaries, highlighting operational strengths, emerging risks, strategic outlook, and a confidence score.
- **Cross-Entity Comparison Engine**: Side-by-side metric comparison and automated comparative synthesis between different companies or historical fiscal years.
- **Zero-Hallucination Grounded Chat**: An interactive chat assistant bound by strict source-only constraints with 6-turn conversational context tracking.
- **Secure Multi-User Tenant Isolation**: All ingested documents, vector collections, and relational records are partitioned strictly by user ID via JWT authentication.
- **Complete Resource Cleanup**: Cascading deletion endpoint that purges local raw PDFs, vector collections, and database records simultaneously.

---

## 🔬 Engineering & Technical Highlights

### 1. Document Ingestion & Semantic Chunking
Raw PDF files are parsed using `pymupdf4llm`, converting complex financial layouts and balance sheets into clean Markdown tables rather than flat, unstructured text. The parsed document is segmented using semantic chunking heuristics with proportional overlap, preserving contextual meaning and avoiding table fragment severance.

### 2. Multi-Stage Hybrid Retrieval
Standard vector search frequently struggles with financial terminology, specific ticker tags, and exact numerical balance-sheet line items. DocRAG AI addresses this using a three-tier retrieval pipeline:
1. **Query Expansion**: The user query is rewritten via LLM into financial search terminology.
2. **Parallel Hybrid Search**:
   - **Dense Retrieval**: Embedding similarity query executed over ChromaDB with `$and` metadata filters (`user_id`, `company`, `year`).
   - **Sparse Retrieval**: BM25 keyword matching via `rank-bm25` targeting specific audited keywords.
3. **Reciprocal Dedup & Cross-Encoder Reranking**: The union of candidates is scored using `cross-encoder/ms-marco-MiniLM-L-6-v2`, returning the top $k$ highest-confidence context chunks.

```
User Query ──► Query Expander ──┬──► ChromaDB Vector Search ──┐
                                └──► Rank-BM25 Keyword Search ─┴──► Cross-Encoder ──► Top Context Chunks
```

### 3. Financial Metric Extraction & Dual-Format Parsing
Extracting financial figures requires handling diverse international accounting notations (`$`, `€`, `₹`, `million`, `billion`, `crore`, `lakh`, `%`). 

The extraction engine instructs the LLM to output exact audit-preserved strings without speculative math. The backend `financial_parser.py` then produces a dual payload:
```json
{
  "display": "$97,690 million",
  "value": 97690000000.0
}
```
This enables the frontend to display human-readable strings on KPI cards while feeding clean floating-point values into Chart.js without UI-layer regex hacks.

### 4. Multi-Tenant User Isolation
Every ingestion record, ChromaDB embedding document, and relational database row is tagged with the authenticated user's ID. This prevents cross-account data leakage in shared environments and enables distinct report versions per user.

### 5. Grounded Q&A Chat Pipeline
The conversational assistant operates under strict system constraints:
- Must only answer using the retrieved context chunks.
- Refuses to speculate or invent unstated financial figures.
- Retains conversational history across the last 6 message turns.
- Translates balance sheet and operating performance into investor-relevant takeaways.

### 6. Comparative Company Intelligence
Users can select any two uploaded reports (e.g., *Tesla 2024* vs. *Tesla 2025*, or *Apple 2024* vs. *Microsoft 2024*). The system aggregates metrics from both entities and prompts the LLM to deliver a rigorous comparative breakdown covering margin resilience, leverage ratios, and capital deployment.

---

## 🛠️ Technology Stack

| Layer | Technologies |
| :--- | :--- |
| **Frontend** | React 19, Vite, Tailwind CSS v4, Chart.js, react-chartjs-2, React Router v7, Lucide Icons, React Hot Toast, React Markdown |
| **Backend API** | Python 3.11+, FastAPI, Uvicorn, Pydantic, Python-Multipart |
| **Security & Auth** | OAuth2 Password Bearer, JWT (Python-Jose), Bcrypt (Passlib) |
| **Database & ORM** | SQLite / PostgreSQL, SQLAlchemy, Alembic |
| **Vector Store** | ChromaDB (Persistent Disk Storage with Metadata Filters) |
| **Retrieval & NLP** | Rank-BM25, Sentence-Transformers (`ms-marco-MiniLM-L-6-v2`), LangChain |
| **LLM & Embeddings**| OpenAI GPT-4o-mini, OpenAI Embeddings (`text-embedding-3-small` / HuggingFace) |
| **PDF Processing** | PyMuPDF, PyMuPDF4LLM |

---

## 🔌 API Reference

### Authentication
| Method | Endpoint | Description |
| :--- | :--- | :--- |
| `POST` | `/auth/register` | Register a new user account |
| `POST` | `/auth/login` | Authenticate and obtain JWT access token |

### Ingestion & Documents
| Method | Endpoint | Description |
| :--- | :--- | :--- |
| `POST` | `/upload/` | Upload PDF report, trigger ingestion, chunking, and KPI extraction |
| `DELETE` | `/reports/{company}/{year}` | Cascade delete report PDF, database metrics, and vector records |

### Dashboard & Analytics
| Method | Endpoint | Description |
| :--- | :--- | :--- |
| `GET` | `/dashboard/companies/list` | Retrieve list of all uploaded companies and fiscal years for user |
| `GET` | `/dashboard/{company}/{year}` | Fetch parsed financial KPIs for a specific company report |
| `GET` | `/dashboard/{company}/{year}/insights` | Generate AI executive analysis (Strengths, Risks, Outlook) |

### Comparative Analytics
| Method | Endpoint | Description |
| :--- | :--- | :--- |
| `GET` | `/comparison/` | Retrieve comparative metrics for two selected entities |
| `GET` | `/comparison/insights` | Generate deep LLM comparative synthesis between two companies |

### Chat & Q&A
| Method | Endpoint | Description |
| :--- | :--- | :--- |
| `POST` | `/chat/` | Query report using multi-turn conversational hybrid RAG pipeline |

### System
| Method | Endpoint | Description |
| :--- | :--- | :--- |
| `GET` | `/health/` | API liveness and readiness probe |

---

## 📂 Project Directory Structure

```text
RAGBasedDocAnalysis/
├── auth/                       # JWT authentication, token generation, user validation
│   ├── __init__.py
│   └── oauth2.py
├── database/                   # SQLAlchemy models, sessions, and persistence helpers
│   ├── create_table.py
│   ├── db.py                   # Engine configuration & DB session generator
│   ├── delete_report.py        # Relational record cleanup
│   ├── metrics.py              # FinancialMetric ORM model
│   ├── save_metrics.py         # KPI insertion and update logic
│   └── user.py                 # User ORM model
├── ingestion/                  # PDF extraction, parsing, and text segmentation
│   ├── ingest_document.py      # Unified ingestion orchestrator
│   ├── pdf_to_markdown.py      # PyMuPDF4LLM table-preserving parser
│   └── semantic_chunker.py     # Structural & semantic text chunking
├── llm/                        # Model client configurations (OpenAI / HuggingFace)
│   └── openai_client.py
├── rag/                        # Core RAG pipelines and prompt orchestrators
│   ├── ai_insights.py          # Executive analysis & risk synthesis
│   ├── comparison_insights.py  # Multi-company comparison generator
│   ├── extract_metric.py       # Single-metric targeted extraction
│   ├── kpi_extractor_rag.py    # Automated 6-KPI extraction pipeline
│   └── rag_pipeline.py         # Multi-turn conversational Q&A engine
├── retrieval/                  # Hybrid retrieval mechanisms
│   ├── bm25_retriever.py       # Rank-BM25 sparse search engine
│   ├── hybrid_retriever.py     # Combined vector + keyword candidate retrieval
│   ├── query_expander.py       # LLM query reformulation
│   └── reranker.py             # Cross-Encoder neural re-ranking
├── routes/                     # FastAPI route definitions
│   ├── auth.py
│   ├── chat.py
│   ├── comparison.py
│   ├── dashboard.py
│   ├── health.py
│   ├── report.py
│   └── upload.py
├── storage/                    # Local raw PDF file storage & cleanup utilities
│   └── delete_pdf.py
├── utils/                      # Financial parsing and normalization utilities
│   └── financial_parser.py
├── vectorstore/                # ChromaDB collection management
│   ├── chroma_db.py
│   └── delete_vectors.py
├── frontend/                   # Modern React 19 single-page application
│   ├── src/
│   │   ├── api/                # Axios API client & interceptors
│   │   ├── components/         # Reusable UI components (Navbar, Sidebar, Cards)
│   │   ├── context/            # Authentication & State providers
│   │   ├── pages/              # Landing, Dashboard, Comparison, Chat, Upload, Auth
│   │   └── App.jsx
│   ├── package.json
│   └── vite.config.js
├── app.py                      # FastAPI application definition and CORS setup
├── main.py                     # Entry point (Uvicorn runner)
├── requirements.txt            # Python dependencies
└── README.md
```

---

## 🚀 Getting Started

### Prerequisites

- **Python**: `3.11` or `3.12`
- **Node.js**: `v18.0.0` or later
- **OpenAI API Key**: Required for embeddings and LLM generation

### Backend Setup

1. **Clone the repository**:
   ```bash
   git clone https://github.com/nototiger0227/RAGBasedDocAnalysis.git
   cd RAGBasedDocAnalysis
   ```

2. **Create and activate a virtual environment**:
   - **Windows (PowerShell)**:
     ```powershell
     python -m venv .venv
     .venv\Scripts\Activate.ps1
     ```
   - **Linux / macOS**:
     ```bash
     python3 -m venv .venv
     source .venv/bin/activate
     ```

3. **Install Python dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment variables**:
   Create a `.env` file in the project root (see [Environment Variables](#environment-variables) below).

5. **Initialize database & launch backend**:
   ```bash
   python main.py
   ```
   The backend API will be available at `http://127.0.0.1:8000`.  
   Interactive Swagger docs are accessible at `http://127.0.0.1:8000/docs`.

### Frontend Setup

1. **Navigate to the frontend directory**:
   ```bash
   cd frontend
   ```

2. **Install dependencies**:
   ```bash
   npm install
   ```

3. **Run the Vite development server**:
   ```bash
   npm run dev
   ```
   The application UI will be accessible at `http://localhost:5173`.

### Environment Variables

Create a `.env` file in the root directory:

```env
# AI Model Configuration
OPENAI_API_KEY=sk-your-openai-api-key-here

# Security & Authentication
SECRET_KEY=your_super_secret_hex_key_here
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=1440

# Database Configuration (SQLite default; PostgreSQL also supported)
DATABASE_URL=sqlite:///./DocRAG.db

# Frontend CORS Origin
BASE_URL=http://localhost:5173
```

---

## 👨‍💻 Author & Acknowledgments

**Vansh Gupta**  
*Department of Computer Engineering*  
*National Institute of Technology (NIT), Kurukshetra*  
GitHub: [@nototiger0227](https://github.com/nototiger0227)

DocRAG AI was created as an advanced, end-to-end investigation into production-grade Information Retrieval, combining modern Generative AI pipelines with real-world financial data engineering.
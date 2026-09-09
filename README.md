# FinSight AI

> AI-Powered Financial Intelligence Platform for Annual Report Analysis

FinSight AI is an AI-powered financial analysis platform that transforms annual reports into structured financial insights.

Users can upload company annual reports, automatically extract important financial metrics, explore financial KPIs through an interactive dashboard, and ask questions about uploaded financial documents using a Retrieval-Augmented Generation (RAG) pipeline.

The system combines document processing, semantic chunking, vector search, BM25 retrieval, reranking, LLM-based extraction, financial parsing, and an interactive React dashboard.

---

## 🚀 Features

### 📄 Annual Report Upload

Upload annual reports in PDF format with:

- Company name
- Financial year
- PDF document

The system processes the report through an automated pipeline:

```text
PDF
 ↓
Markdown
 ↓
Semantic Chunking
 ↓
Embeddings
 ↓
ChromaDB
 ↓
Financial Metric Extraction
 ↓
SQLite


## 🚀 Features

### 📄 Annual Report Upload

Upload annual reports in PDF format with:

- Company name
- Financial year
- PDF document

The system processes the report through an automated pipeline:

```text
PDF
 ↓
Markdown
 ↓
Semantic Chunking
 ↓
Embeddings
 ↓
ChromaDB
 ↓
Financial Metric Extraction
 ↓
SQLite
```

### 📊 Financial KPI Dashboard

The dashboard provides a structured overview of important financial metrics:

- Revenue
- Net Income
- Operating Cash Flow
- Debt
- Operating Margin
- R&D Expense

Each metric contains both its original display value and a parsed numerical value.

Example:

```json
{
    "display": "$97,690 million",
    "value": 97690000000
}
```

### 🏢 Company + Year Report Selection

FinSight AI supports multiple annual reports for the same company.

Example:

```text
Tesla (2025)
Tesla (2024)
Apple (2024)
Microsoft (2024)
```

Reports are identified using:

```text
User ID
+
Company
+
Financial Year
```

### 📈 Financial Visualization

The dashboard provides interactive financial visualizations using Chart.js.

The visualization supports:

- Revenue
- Net Income
- Operating Cash Flow
- Debt
- Responsive charts
- Animated presentation
- Formatted financial values
- Interactive tooltips

### 🤖 AI Financial Analysis

FinSight AI generates automated financial analysis using an LLM.

The analysis can provide:

- Executive Summary
- Financial Strengths
- Financial Risks
- Overall Financial Outlook
- Confidence Score

### 💬 AI Financial Chat

Users can ask questions about uploaded financial reports.

Example questions:

```text
What was the company's revenue?

What was the operating cash flow?

How much debt did the company have?

What are the major financial risks?

Why is the company's cash flow important?
```

The chatbot retrieves relevant information from the selected financial report before generating an answer.


# 🧠 RAG Architecture

FinSight AI uses a Hybrid Retrieval-Augmented Generation architecture.

```text
                  User Question
                       │
                       ▼
                Query Expansion
                       │
             ┌─────────┴─────────┐
             │                   │
             ▼                   ▼
        Semantic Search       BM25 Search
          ChromaDB             Keyword
             │                   │
             └─────────┬─────────┘
                       │
                       ▼
                Hybrid Retrieval
                       │
                       ▼
                    Reranker
                       │
                       ▼
                Relevant Chunks
                       │
                       ▼
                     LLM
                       │
                       ▼
                  Final Answer
```

Retrieval is scoped using:

```text
User ID
Company
Year
```

This allows the system to distinguish between different annual reports belonging to the same company.

# 🔍 Hybrid Retrieval

FinSight AI combines semantic and lexical retrieval.

## Semantic Retrieval

Semantic retrieval uses embeddings to find documents based on meaning and contextual similarity.

```text
User Query
    ↓
Embedding Model
    ↓
ChromaDB
    ↓
Similarity Search
```

## BM25 Retrieval

BM25 provides keyword-based retrieval.

This is particularly useful for financial documents because exact terms such as:

```text
Revenue
Net Income
Operating Cash Flow
Long-term Debt
Research and Development
```

can be highly important.

## Reranking

Results from the retrieval stage are passed through a reranker to improve relevance before being provided to the LLM.

The final retrieval pipeline is:

```text
Query
  ↓
Query Expansion
  ↓
Semantic Search + BM25
  ↓
Hybrid Results
  ↓
Reranking
  ↓
Relevant Context
  ↓
LLM
```


# 🧩 Financial Metric Extraction

The system extracts important financial metrics from annual reports.

Supported metrics include:

```text
Revenue
Net Income
Operating Cash Flow
Debt
Operating Margin
R&D Expense
```

The extraction pipeline is:

```text
Question
   ↓
Query Expansion
   ↓
Hybrid Retrieval
   ↓
Reranking
   ↓
Relevant Document Chunks
   ↓
LLM Extraction
   ↓
Financial Value
```

The extraction system is instructed to preserve financial units such as:

```text
$
%
million
billion
crore
lakh
```

For example:

```text
97,690
+
Amounts in millions
```

is returned as:

```text
$97,690 million
```

rather than simply:

```text
97690
```

The system also avoids calculating values when the requested metric cannot be directly extracted from the report.


# 💰 Financial Value Parser

FinSight AI includes a reusable financial parser that converts extracted financial values into numerical representations.

Supported units include:

```text
thousand
million
billion
trillion
lakh
crore
```

Example:

```text
$118.5 billion
```

is converted internally to:

```text
118500000000
```

while the original display value is preserved:

```text
$118.5 billion
```

Percentage values are handled separately.

This allows the application to use the same financial value for both:

- Human-readable dashboard display
- Numerical visualization and analysis


# 🏗️ System Architecture

```text
                         ┌──────────────────┐
                         │   React Frontend │
                         └────────┬─────────┘
                                  │
                                  ▼
                         ┌──────────────────┐
                         │    FastAPI API   │
                         └────────┬─────────┘
                                  │
             ┌────────────────────┼────────────────────┐
             │                    │                    │
             ▼                    ▼                    ▼
        Dashboard              Upload               AI Chat
             │                    │                    │
             │                    ▼                    │
             │             PDF Processing             │
             │                    │                    │
             │                    ▼                    │
             │             Semantic Chunking           │
             │                    │                    │
             │                    ▼                    │
             │               Embeddings                │
             │                    │                    │
             │                    ▼                    │
             │               ChromaDB ◄────────────────┘
             │                    │
             │                    ▼
             │             Hybrid Retrieval
             │                    │
             │                    ▼
             │                 Reranker
             │                    │
             │                    ▼
             │                    LLM
             │
             ▼
       SQLite Database
       Financial Metrics
```

# 🛠️ Tech Stack

## Frontend

- React 19
- React Router
- Tailwind CSS
- Axios
- Lucide React
- React Hot Toast
- React Markdown
- Chart.js
- react-chartjs-2
- Vite

## Backend

- Python
- FastAPI
- Uvicorn
- SQLAlchemy
- SQLite

## AI / RAG

- LangChain
- OpenAI GPT-4o-mini
- Embedding Models
- ChromaDB
- BM25
- Rank-BM25
- Reranking
- Query Expansion

## Document Processing

- PDF to Markdown conversion
- Semantic Chunking
- Embedding Generation


# 📁 Project Structure

```text
finsight-ai/
│
├── auth/
│   └── oauth2.py
│
├── database/
│   ├── db.py
│   ├── user.py
│   ├── metrics.py
│   └── save_metrics.py
│
├── ingestion/
│   ├── pdf_to_markdown.py
│   ├── semantic_chunker.py
│   └── ingest_document.py
│
├── llm/
│   └── openai_client.py
│
├── rag/
│   ├── ai_insights.py
│   ├── extract_metric.py
│   ├── kpi_extractor_rag.py
│   └── rag_pipeline.py
│
├── retrieval/
│   ├── hybrid_retriever.py
│   ├── bm25_retriever.py
│   ├── reranker.py
│   └── query_expander.py
│
├── routes/
│   ├── dashboard.py
│   ├── upload.py
│   └── chat.py
│
├── schemas/
│   └── chat.py
│
├── utils/
│   └── financial_parser.py
│
├── vectorstore/
│   └── chroma_db.py
│
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   │   ├── dashboard/
│   │   │   └── common/
│   │   ├── pages/
│   │   ├── layouts/
│   │   ├── context/
│   │   ├── api/
│   │   └── App.jsx
│   │
│   ├── package.json
│   └── vite.config.js
│
├── data/
│   └── raw_pdfs/
│
├── main.py
├── app.py
├── requirements.txt
└── README.md
```


# ⚙️ Installation

## 1. Clone the Repository

```bash
git clone https://github.com/rahillll16/finsight-ai-investor-intelligence-platform.git
cd finsight-ai
```

## 2. Create a Python Virtual Environment

### Windows

```bash
python -m venv .venv
.venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv .venv
source .venv/bin/activate
```

## 3. Install Backend Dependencies

```bash
pip install -r requirements.txt
```

## 4. Install Frontend Dependencies

```bash
cd frontend
npm install
```


# 🔐 Environment Variables

Create a `.env` file in the project root.

Example:

```env
OPENAI_API_KEY=your_api_key
DATABASE_URL=sqlite:///./finsight.db
SECRET_KEY=your_secret_key
```

Never commit `.env` or API keys to Git.

Recommended `.gitignore` entries:

```text
.env
.venv/
__pycache__/
*.pyc
finsight.db
data/raw_pdfs/
chroma/
node_modules/
dist/
```


# 🚀 Running the Project

## Start the Backend

From the project root:

```bash
python main.py
```

The backend typically runs at:

```text
http://127.0.0.1:8000
```

FastAPI documentation:

```text
http://127.0.0.1:8000/docs
```

## Start the Frontend

Open another terminal:

```bash
cd frontend
npm run dev
```

The frontend typically runs at:

```text
http://localhost:5173
```



# 👨‍💻 Author

## Vansh Gupta

Computer Engineering  
NIT Kurukshetra

FinSight AI was developed as a full-stack AI/RAG financial intelligence platform combining:

- Full-Stack Development
- React
- FastAPI
- SQLAlchemy
- LLMs
- Retrieval-Augmented Generation
- Vector Databases
- Hybrid Information Retrieval
- BM25
- Semantic Search
- Reranking
- Financial Document Processing
- Financial Data Extraction
- Interactive Financial Analytics
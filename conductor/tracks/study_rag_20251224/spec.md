# Specification: Study - Complete RAG Pipelines

## 1. Overview
This study track focuses on building and validating a complete, end-to-end Retrieval-Augmented Generation (RAG) pipeline. The goal is to experiment with sample data (clinical notes), verify the ingestion process, and ensure accurate retrieval and generation before integrating these components into the main production codebase.

## 2. Goals
- **Data Preparation:** Create and organize a set of synthetic or anonymized clinical notes for testing.
- **Pipeline Implementation:** Build a standalone script or module that handles:
    - Document Ingestion (Loading & Splitting)
    - Embedding Generation (using OpenAI or local models)
    - Vector Storage (ChromaDB)
    - Retrieval (Semantic Search)
    - Generation (Answer synthesis based on retrieved context)
- **Validation:** Verify that the pipeline can accurately answer questions based *only* on the provided context.
- **Comparison:** (Optional) Compare performance between different chunking strategies or embedding models.

## 3. Requirements

### 3.1 Functional Requirements
- **Input:** A folder of `.txt` or `.md` files representing clinical notes.
- **Process:**
    - Load files from the directory.
    - Split text into manageable chunks (e.g., 500-1000 tokens).
    - Generate embeddings.
    - Store embeddings in a transient or local persistent ChromaDB instance.
    - Accept a natural language query.
    - Retrieve top-k relevant chunks.
    - Pass context + query to an LLM.
- **Output:** A natural language answer derived from the context, with citations if possible.

### 3.2 Non-Functional Requirements
- **Code Quality:** Code should be modular and readable, adhering to the project's Python style guide.
- **Reproducibility:** The study should be reproducible via a single script or notebook.
- **Documentation:** Findings and observations should be recorded.

## 4. Out of Scope
- Building the full production API (FastAPI integration is for later).
- Frontend UI development.
- Extensive performance tuning or load testing.
- MCP integration (reserved for the main track).

## 5. Success Criteria
- A functional Python script runs the full pipeline without errors.
- The system correctly answers 3/3 test questions based on the sample data.
- A brief report (markdown file) summarizing what worked, what didn't, and recommended parameters for the production implementation.

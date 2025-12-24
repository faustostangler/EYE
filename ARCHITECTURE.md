Goal: Deep technical dive without clogging the README.

Structure:

1. System Design:
High-level data flow Diagram (Ingestion -> Vector DB -> Inference).
2. Components:
Ingestion Engine: Details on ingestion service, chunking strategies.
Inference Engine: Details on inference service (Ollama settings, model quantization).
Vector Database: Schema details for ChromaDB.
3. Data Flow:
Sequence diagram of a user query.
4. Decisions: Why FastApi? Why Chroma? (ADR - Architecture Decision Records).

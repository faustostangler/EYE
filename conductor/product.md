# Product Guide - EYE (Enhanced Yardstick Engine)

## Initial Concept
Enhanced Yardstick Engine (EYE): extração clínica semântica determinística com MCP + RAG.

## Target Audience
The primary users of EYE are **ophthalmologists and doctors** who require efficient and accurate clinical data management.

## Project Goals
- **Automated Extraction:** Convert unstructured clinical notes into structured, actionable data automatically.
- **Deterministic Decision Support:** Provide a verifiable and reliable clinical decision support system.
- **Natural Language Querying:** Enable doctors to query clinical documentation and medical literature using natural language via RAG (Retrieval-Augmented Generation).

## Key Features
- **Structured Semantic Extraction:** Utilize `Instructor` for high-precision extraction of clinical entities like diagnoses, medications, and procedures into structured formats.
- **MCP Integration:** Leverage the Model Context Protocol to integrate with external medical databases and knowledge graphs.
- **Medical Retrieval Pipeline:** A specialized RAG pipeline designed for indexing and searching medical literature and local patient histories.

## Value Proposition
EYE solves critical workflow challenges for medical professionals by:
- **Saving Time:** Significantly reducing the manual effort required to transcribe patient notes into EHRs.
- **Improving Accuracy:** Minimizing human errors and omissions in clinical data capture.
- **Enhancing Knowledge Access:** Providing immediate, context-aware access to medical literature and past cases directly within the clinical workflow.

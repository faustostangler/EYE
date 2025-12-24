# Plan: Study - Complete RAG Pipelines

## Phase 1: Setup and Data Preparation
- [ ] Task: Create a dedicated directory `studies/rag_pipeline` to keep study code separate from `app/`.
- [ ] Task: Create a set of 3-5 synthetic clinical notes (anonymized) in `studies/rag_pipeline/data/` to serve as the ground truth.
- [ ] Task: Create a `README.md` in the study folder to document the objective and how to run the scripts.
- [ ] Task: Conductor - User Manual Verification 'Setup and Data Preparation' (Protocol in workflow.md)

## Phase 2: Ingestion and Storage Implementation
- [ ] Task: Implement `ingest.py` in the study folder.
    - [ ] Subtask: Write tests for document loading.
    - [ ] Subtask: Implement document loading using `langchain_community.document_loaders`.
    - [ ] Subtask: Write tests for text splitting.
    - [ ] Subtask: Implement text splitting (RecursiveCharacterTextSplitter).
    - [ ] Subtask: Write tests for vector store creation.
    - [ ] Subtask: Implement embedding generation and ChromaDB storage.
- [ ] Task: Verify the vector store contains the expected number of chunks.
- [ ] Task: Conductor - User Manual Verification 'Ingestion and Storage Implementation' (Protocol in workflow.md)

## Phase 3: Retrieval and Generation Implementation
- [ ] Task: Implement `query.py` (or extend the script).
    - [ ] Subtask: Write tests for the retrieval function.
    - [ ] Subtask: Implement retrieval logic (query embedding -> similarity search).
    - [ ] Subtask: Write tests for the generation function.
    - [ ] Subtask: Implement the generation chain (Context + Question -> LLM -> Answer).
- [ ] Task: Create a `main.py` or `run_experiment.py` that ties ingestion and querying together for a seamless demo.
- [ ] Task: Conductor - User Manual Verification 'Retrieval and Generation Implementation' (Protocol in workflow.md)

## Phase 4: Validation and Reporting
- [ ] Task: Define 3 test questions based on the synthetic data.
- [ ] Task: Run the pipeline against these questions and record the answers.
- [ ] Task: Create a `REPORT.md` summarizing the findings:
    - Optimal chunk size observed.
    - Quality of answers.
    - Any issues encountered with the libraries.
- [ ] Task: Conductor - User Manual Verification 'Validation and Reporting' (Protocol in workflow.md)

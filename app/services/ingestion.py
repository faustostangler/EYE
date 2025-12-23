import os
from typing import List

from dotenv import load_dotenv
from langchain_community.document_loaders import DirectoryLoader, TextLoader
from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings
from langchain_text_splitters import CharacterTextSplitter
from langchain_core.documents import Document

# Attempt to import logger, fall back to print if app module not found (e.g. running script directly improperly)
try:
    from app.core.logger import logger
except ImportError:
    import logging
    logger = logging.getLogger("ingestion")
    logging.basicConfig(level=logging.INFO)

load_dotenv()

def load_documents(docs_path: str = "docs") -> List[Document]:
    """Load all text files from the docs directory"""
    logger.info(f"Loading documents from {docs_path}...")
    
    if not os.path.exists(docs_path):
        msg = f"The directory {docs_path} does not exist. Please create it and add your company files."
        logger.error(msg)
        raise FileNotFoundError(msg)
    
    loader = DirectoryLoader(
        path=docs_path,
        glob="*.txt",
        loader_cls=TextLoader
    )
    
    documents = loader.load()
    
    if len(documents) == 0:
        msg = f"No .txt files found in {docs_path}. Please add your company documents."
        logger.warning(msg)
        raise FileNotFoundError(msg)
    
    for i, doc in enumerate(documents[:2]):
        logger.debug(f"Document {i+1} preview: {doc.metadata.get('source', 'unknown')} - {doc.page_content[:100]}...")

    return documents

def split_documents(documents: List[Document], chunk_size: int = 1000, chunk_overlap: int = 0) -> List[Document]:
    """Split documents into smaller chunks with overlap"""
    logger.info("Splitting documents into chunks...")
    
    text_splitter = CharacterTextSplitter(
        chunk_size=chunk_size, 
        chunk_overlap=chunk_overlap
    )
    
    chunks = text_splitter.split_documents(documents)
    
    if chunks:
        logger.info(f"Created {len(chunks)} chunks.")
        for i, chunk in enumerate(chunks[:2]):
            logger.debug(f"Chunk {i+1} preview: {chunk.page_content[:50]}...")
            
    return chunks

def create_vector_store(chunks: List[Document], persist_directory: str = "db/chroma_db") -> Chroma:
    """Create and persist ChromaDB vector store"""
    logger.info("Creating embeddings and storing in ChromaDB...")
    
    if not os.getenv("OPENAI_API_KEY"):
         logger.error("OPENAI_API_KEY not found in environment variables.")
    
    embedding_model = OpenAIEmbeddings(model="text-embedding-3-small")
    
    # Create ChromaDB vector store
    vectorstore = Chroma.from_documents(
        documents=chunks,
        embedding=embedding_model,
        persist_directory=persist_directory, 
        collection_metadata={"hnsw:space": "cosine"}
    )
    logger.info(f"Vector store created and saved to {persist_directory}")
    return vectorstore

def run_ingestion_pipeline(docs_path: str = "docs", persist_directory: str = "db/chroma_db", force_refresh: bool = False):
    """Main ingestion pipeline logic"""
    logger.info("=== Starting RAG Document Ingestion Pipeline ===")
    
    # Check if vector store already exists and we are not forcing refresh.
    # Note: If you want to APPEND to existing store, you should not check existence here like this.
    # But based on user request ("No need to re-process"), we stick to this logic.
    if os.path.exists(persist_directory) and not force_refresh:
        logger.info("Vector store already exists. Use force_refresh=True to overwrite or recreate.")
        
        embedding_model = OpenAIEmbeddings(model="text-embedding-3-small")
        vectorstore = Chroma(
            persist_directory=persist_directory,
            embedding_function=embedding_model, 
            collection_metadata={"hnsw:space": "cosine"}
        )
        # Using Try/Except in case the DB is empty or corrupted
        try:
            count = vectorstore._collection.count()
            logger.info(f"Loaded existing vector store with {count} documents")
        except Exception as e:
            logger.warning(f"Could not count documents in existing store: {e}")
            
        return vectorstore

    logger.info(f"Initializing vector store in {persist_directory}...")
    
    documents = load_documents(docs_path)
    chunks = split_documents(documents)
    vectorstore = create_vector_store(chunks, persist_directory)
    
    logger.info("Ingestion complete!")
    return vectorstore

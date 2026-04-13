#!/usr/bin/env python3
"""
Indexer for Analog Devices Knowledge Base.
Supports Batch Processing to avoid Google API Rate Limits (Error 429).
"""

import os
import glob
import argparse
import time
from dotenv import load_dotenv
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import MarkdownTextSplitter
from langchain_community.vectorstores import Chroma

# Load environment variables
load_dotenv()

# ==========================================
# Configuration & DYNAMIC ABSOLUTE PATHS
# ==========================================
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.abspath(os.path.join(SCRIPT_DIR, "..", ".."))

# Based on your last output, your data is currently here:
INPUT_DIR = os.path.join(PROJECT_ROOT, "src", "scraper", "data", "markdown")
CHROMA_PATH = os.path.join(PROJECT_ROOT, "src", "scraper", "data", "chroma_db")

# Local Setup
OLLAMA_BASE_URL = "http://localhost:11434"
LOCAL_EMBEDDING_MODEL = "nomic-embed-text"

# External API Setup (Using the stable model ID you found)
GOOGLE_EMBEDDING_MODEL = "models/gemini-embedding-001"

def parse_arguments():
    parser = argparse.ArgumentParser(description="Run the Vector Indexer with Batching.")
    parser.add_argument(
        '--mode', 
        choices=['local', 'ext-api'], 
        required=True, 
        help="Choose mode."
    )
    return parser.parse_args()

def load_documents() -> list:
    md_files = glob.glob(os.path.join(INPUT_DIR, "*.md"))
    documents = []
    for filepath in md_files:
        loader = TextLoader(filepath, encoding='utf-8')
        documents.extend(loader.load())
    print(f"[+] Loaded {len(documents)} documents.")
    return documents

def split_text(documents: list) -> list:
    print("[*] Splitting documents into chunks...")
    text_splitter = MarkdownTextSplitter(chunk_size=1000, chunk_overlap=150)
    chunks = text_splitter.split_documents(documents)
    print(f"[+] Generated {len(chunks)} chunks.")
    return chunks

def get_embeddings_instance(mode: str):
    if mode == 'local':
        from langchain_community.embeddings import OllamaEmbeddings
        return OllamaEmbeddings(base_url=OLLAMA_BASE_URL, model=LOCAL_EMBEDDING_MODEL)
    elif mode == 'ext-api':
        from langchain_google_genai import GoogleGenerativeAIEmbeddings
        if not os.getenv("GOOGLE_API_KEY"):
            raise ValueError("[!] GOOGLE_API_KEY is missing in your .env file.")
        return GoogleGenerativeAIEmbeddings(model=GOOGLE_EMBEDDING_MODEL)

def create_vector_db(chunks: list, embeddings):
    """
    Saves chunks to ChromaDB in batches to respect Google's 100 RPM rate limit.
    """
    BATCH_SIZE = 90  # Safe margin below the 100 limit
    WAIT_TIME = 65   # Seconds to wait between batches
    
    print(f"[*] Starting Batch Processing: {len(chunks)} chunks in groups of {BATCH_SIZE}...")
    
    # 1. Initialize the Chroma instance with the first batch
    db = Chroma.from_documents(
        documents=chunks[:BATCH_SIZE],
        embedding=embeddings,
        persist_directory=CHROMA_PATH
    )
    print(f"[+] Initialized DB with first {min(BATCH_SIZE, len(chunks))} chunks.")
    
    # 2. Loop through the remaining chunks in batches
    for i in range(BATCH_SIZE, len(chunks), BATCH_SIZE):
        print(f"[*] Quota Cooldown: Waiting {WAIT_TIME} seconds before the next batch...")
        time.sleep(WAIT_TIME)
        
        batch = chunks[i : i + BATCH_SIZE]
        db.add_documents(batch)
        print(f"[+] Successfully added batch: {i} to {min(i + BATCH_SIZE, len(chunks))}")

    db.persist()
    print(f"\n[+++] Success! Vector database saved at: {CHROMA_PATH}")

def main():
    args = parse_arguments()
    if not os.path.exists(INPUT_DIR) or not os.listdir(INPUT_DIR):
        print(f"[!] Critical Error: Markdown directory EMPTY at: {INPUT_DIR}")
        return

    documents = load_documents()
    chunks = split_text(documents)
    embeddings = get_embeddings_instance(args.mode)
    
    start_time = time.time()
    create_vector_db(chunks, embeddings)
    end_time = time.time()
    
    duration = (end_time - start_time) / 60
    print(f"[*] Total indexing time: {duration:.2f} minutes.")

if __name__ == "__main__":
    main()
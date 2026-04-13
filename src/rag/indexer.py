"""
Indexer for Analog Devices Knowledge Base.
Supports both Local (Ollama) and External API (Google AI Studio) modes via CLI.
"""

import os
import glob
import argparse
from dotenv import load_dotenv
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import MarkdownTextSplitter
from langchain_community.vectorstores import Chroma

# Load environment variables from .env file (for GOOGLE_API_KEY)
load_dotenv()

# ==========================================
# Configuration & Constants
# ==========================================
INPUT_DIR = os.path.join("data", "markdown")
CHROMA_PATH = os.path.join("data", "chroma_db")

# Local Setup
OLLAMA_BASE_URL = "http://localhost:11434" # Change this to your VM IP later
LOCAL_EMBEDDING_MODEL = "nomic-embed-text"

# External API Setup (Google)
GOOGLE_EMBEDDING_MODEL = "models/text-embedding-004"

def parse_arguments():
    """Parses command line arguments to determine the execution mode."""
    parser = argparse.ArgumentParser(description="Run the Vector Indexer.")
    parser.add_argument(
        '--mode', 
        choices=['local', 'ext-api'], 
        required=True, 
        help="Choose '--mode local' for Ollama or '--mode ext-api' for Google AI Studio."
    )
    return parser.parse_args()

def load_documents() -> list:
    print("[*] Loading Markdown documents...")
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
    """Returns the correct embedding class based on the chosen mode."""
    if mode == 'local':
        print(f"[*] Initializing LOCAL embeddings: {LOCAL_EMBEDDING_MODEL}")
        from langchain_community.embeddings import OllamaEmbeddings
        return OllamaEmbeddings(base_url=OLLAMA_BASE_URL, model=LOCAL_EMBEDDING_MODEL)
    
    elif mode == 'ext-api':
        print(f"[*] Initializing EXTERNAL embeddings: Google {GOOGLE_EMBEDDING_MODEL}")
        from langchain_google_genai import GoogleGenerativeAIEmbeddings
        
        if not os.getenv("GOOGLE_API_KEY"):
            raise ValueError("[!] GOOGLE_API_KEY is missing in .env file.")
            
        return GoogleGenerativeAIEmbeddings(model=GOOGLE_EMBEDDING_MODEL)

def create_vector_db(chunks: list, embeddings):
    print("[*] Generating embeddings and saving to ChromaDB...")
    db = Chroma.from_documents(
        documents=chunks, 
        embedding=embeddings, 
        persist_directory=CHROMA_PATH
    )
    db.persist()
    print(f"[+] Vector database successfully saved to: {CHROMA_PATH}")

def main():
    args = parse_arguments()
    
    if not os.path.exists(INPUT_DIR) or not os.listdir(INPUT_DIR):
        print("[!] No Markdown files found. Please run the parser first.")
        return

    documents = load_documents()
    chunks = split_text(documents)
    
    # Initialize the chosen embedding model
    embeddings = get_embeddings_instance(args.mode)
    
    # Store in database
    create_vector_db(chunks, embeddings)

if __name__ == "__main__":
    main()
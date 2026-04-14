#!/usr/bin/env python3
"""
Indexer for Analog Devices Knowledge Base.
Features: Eager Disk Writing Cache (True Bulletproof), Local & API Routing.
"""

import os
import glob
import json
import hashlib
import argparse
import time
from typing import List
from dotenv import load_dotenv
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import MarkdownTextSplitter
from langchain_community.vectorstores import Chroma

load_dotenv()

# ==========================================
# Configuration & Absolute Paths
# ==========================================
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.abspath(os.path.join(SCRIPT_DIR, "..", ".."))

INPUT_DIR = os.path.join(PROJECT_ROOT, "src", "scraper", "data", "markdown")
CHROMA_PATH = os.path.join(PROJECT_ROOT, "src", "scraper", "data", "chroma_db")
CACHE_DIR = os.path.join(PROJECT_ROOT, "src", "scraper", "data", "custom_cache")

# ==========================================
# Universal Resilient Cache Wrapper (Eager Write)
# ==========================================
class BulletproofCacheEmbeddings:
    def __init__(self, base_model, cache_directory: str):
        self.model = base_model
        self.cache_dir = cache_directory
        os.makedirs(self.cache_dir, exist_ok=True)
        
    def embed_documents(self, texts: List[str]) -> List[List[float]]:
        final_embeddings = [None] * len(texts)
        texts_to_fetch = []
        indices_to_fetch = []
        
        # 1. Load existing cache
        for i, text in enumerate(texts):
            text_hash = hashlib.md5(text.encode('utf-8')).hexdigest()
            cache_file = os.path.join(self.cache_dir, f"{text_hash}.json")
            
            if os.path.exists(cache_file):
                with open(cache_file, 'r') as f:
                    final_embeddings[i] = json.load(f)
            else:
                texts_to_fetch.append(text)
                indices_to_fetch.append(i)
                
        # 2. Fetch and EAGER SAVE
        if texts_to_fetch:
            print(f"[*] Cache MISS: Fetching {len(texts_to_fetch)} new embeddings...")
            BATCH_SIZE = 50 
            SLEEP_TIME = 1  
            
            for i in range(0, len(texts_to_fetch), BATCH_SIZE):
                batch = texts_to_fetch[i : i + BATCH_SIZE]
                batch_indices = indices_to_fetch[i : i + BATCH_SIZE]
                print(f"    -> Processing and saving batch {i} to {min(i + BATCH_SIZE, len(texts_to_fetch))}...")
                
                try:
                    # Get embeddings from the model
                    batch_embeddings = self.model.embed_documents(batch)
                    
                    # IMMEDIATELY write to disk (Eager Writing)
                    for local_idx, text, vec in zip(batch_indices, batch, batch_embeddings):
                        text_hash = hashlib.md5(text.encode('utf-8')).hexdigest()
                        cache_file = os.path.join(self.cache_dir, f"{text_hash}.json")
                        with open(cache_file, 'w') as f:
                            json.dump(vec, f)
                        final_embeddings[local_idx] = vec
                        
                    time.sleep(SLEEP_TIME)
                except Exception as e:
                    print(f"\n[!] Error during batch processing: {e}")
                    print("[!] Saved progress up to the crash point. Aborting.")
                    break 
        else:
            print("[*] Cache HIT: 100% of embeddings loaded from local storage.")
                
        return [emb for emb in final_embeddings if emb is not None]

    def embed_query(self, text: str) -> List[float]:
        return self.model.embed_query(text)

# ==========================================
# Main Pipeline
# ==========================================
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--mode', choices=['local', 'ext-api', 'ollama-cloud'], required=True)
    args = parser.parse_args()

    md_files = glob.glob(os.path.join(INPUT_DIR, "*.md"))
    documents = [doc for filepath in md_files for doc in TextLoader(filepath, encoding='utf-8').load()]
    print(f"[+] Loaded {len(documents)} documents.")
    
    chunks = MarkdownTextSplitter(chunk_size=1000, chunk_overlap=100).split_documents(documents)
    print(f"[+] Generated {len(chunks)} chunks.")

    print(f"[*] Initializing connection for mode: {args.mode.upper()}")
    
    if args.mode == 'ext-api':
        from langchain_google_genai import GoogleGenerativeAIEmbeddings
        base_model = GoogleGenerativeAIEmbeddings(model="models/gemini-embedding-001")
        
    elif args.mode == 'local':
        from langchain_ollama import OllamaEmbeddings
        base_model = OllamaEmbeddings(base_url="http://localhost:11434", model="nomic-embed-text")
        
    elif args.mode == 'ollama-cloud':
        from langchain_ollama import OllamaEmbeddings
        ollama_key = os.getenv("OLLAMA_API_KEY")
        if not ollama_key:
            raise ValueError("[!] OLLAMA_API_KEY is missing in your .env file.")
        base_model = OllamaEmbeddings(
            base_url="https://ollama.com", 
            model="nomic-embed-text", 
            client_kwargs={"headers": {"Authorization": f"Bearer {ollama_key}"}}
        )

    embeddings = BulletproofCacheEmbeddings(base_model, CACHE_DIR)

    print("[*] Saving to ChromaDB...")
    db = Chroma.from_documents(chunks, embeddings, persist_directory=CHROMA_PATH)
    print(f"[+] Success! Database saved to: {CHROMA_PATH}")

if __name__ == "__main__":
    main()
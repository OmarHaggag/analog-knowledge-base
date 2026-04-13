# Analog Knowledge Base: Project Explanation

This document explains the architecture and the data pipeline of the "Analog Knowledge Base" project. The goal of this project is to build a local, privacy-respecting AI assistant capable of answering highly technical questions based on the Analog Devices training courses.

## The Problem

Large Language Models (LLMs) are trained on general internet data. They often hallucinate or provide superficial answers when asked highly specific, niche engineering questions (e.g., advanced analog circuit design).

## The Solution

We use a Retrieval-Augmented Generation (RAG) architecture. Instead of relying on the LLM's internal memory, we provide it with a highly specialized, locally stored engineering textbook right before it answers.

## The 4-Phase Data Pipeline

#####  This project is broken down into four distinct, modular phases:

###  Phase 1: Data Acquisition (The Crawler)

1. What it does: 
A Python script (src/scraper/crawler.py) visits the Analog Devices educational website.

2. How it works: 
It acts as an automated robot, sending HTTP requests to the server, navigating through the course pages, and downloading the raw HTML files to our local data/raw_html/ directory.

3. Why it's needed: 
We cannot feed a live website directly into an LLM efficiently. We need the data stored offline on our own hardware first.

### Phase 2: Data Cleaning (The Parser)

1. What it does: 
Converts messy HTML into clean, readable text (src/scraper/parser.py).

2. How it works: 
Raw HTML contains navigation bars, footers, scripts, and styling tags that are useless to the AI. The parser strips all of this away, extracts only the core educational content (text, tables, equations), and saves it as clean Markdown (.md) files in the data/markdown/ directory.

### Phase 3: Vectorization (The Indexer)

1. What it does: 
Translates human text into machine mathematics (src/rag/indexer.py).

2. How it works: 
AI models do not understand English or C++; they understand relationships between numbers. We use an "Embedding Model" (running locally via Ollama) to convert our Markdown chunks into high-dimensional vectors (arrays of numbers). These vectors are then stored in a local, serverless database called ChromaDB.

### Phase 4: Retrieval & Generation (The RAG Agent)
1. What it does: Connects the user to the knowledge (src/rag/retriever.py & main.py).

2. How it works: 
a. The user asks a technical question.
b. The system converts the question into a vector.
c. It searches ChromaDB for the closest matching vectors (conceptually similar text).
d. It retrieves those specific paragraphs from the Analog Devices course.
e. It hands both the user's question AND the retrieved paragraphs to the LLM (e.g., Qwen2.5-Coder or Gemini) to formulate a precise, highly accurate, and grounded answer.
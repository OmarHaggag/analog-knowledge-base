#!/usr/bin/env python3
import streamlit as st
import os
from dotenv import load_dotenv
from langchain_community.vectorstores import Chroma
from langchain_classic.chains import RetrievalQA
from langchain_core.prompts import PromptTemplate

# Import Local/Cloud Ollama
from langchain_ollama import OllamaEmbeddings, ChatOllama
# Import Google Gemini
from langchain_google_genai import GoogleGenerativeAIEmbeddings, ChatGoogleGenerativeAI

# Load .env variables (GOOGLE_API_KEY and OLLAMA_API_KEY)
load_dotenv()

# ==========================================
# 1. Absolute Path Configuration
# ==========================================
# Assuming app.py is in the root directory or src/rag/
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

# Adjust this dynamically to reach the ChromaDB folder based on where you run app.py
# If app.py is in the root folder, use this:
PROJECT_ROOT = SCRIPT_DIR 
# If app.py is inside src/rag/, uncomment the next line instead:
# PROJECT_ROOT = os.path.abspath(os.path.join(SCRIPT_DIR, "..", ".."))

CHROMA_PATH = os.path.join(PROJECT_ROOT, "src", "scraper", "data", "chroma_db")

# ==========================================
# Streamlit UI Setup
# ==========================================
st.set_page_config(page_title="Analog Knowledge Base", page_icon="🔌", layout="wide")
st.title("🔌 Analog Knowledge Base")

# --- Sidebar Configuration ---
st.sidebar.title("⚙️ RAG Engine Settings")

st.sidebar.markdown("### 1. Database Match (Embeddings)")
embedding_choice = st.sidebar.radio(
    "Which model built your ChromaDB?",
    ["Local (nomic-embed-text)", "Google (gemini-embedding-001)"],
    help="CRITICAL: This MUST match the --mode you used in indexer.py!"
)

st.sidebar.markdown("### 2. Chat Brain (LLM)")
llm_choice = st.sidebar.radio(
    "Choose your Inference Engine:",
    ["Local Ollama (CPU)", "Ollama Cloud (API)", "Google Gemini (API)"]
)

# ==========================================
# RAG Initialization Function
# ==========================================
@st.cache_resource(show_spinner="Initializing RAG Pipeline...")
def init_rag(embed_mode, llm_mode):
    # ----------------------------------
    # Step A: Setup Embeddings (Search)
    # ----------------------------------
    if "Local" in embed_mode:
        embeddings = OllamaEmbeddings(base_url="http://localhost:11434", model="nomic-embed-text")
    else:
        embeddings = GoogleGenerativeAIEmbeddings(model="models/gemini-embedding-001")
        
    # Load Database with Absolute Path
    if not os.path.exists(CHROMA_PATH):
        st.error(f"[!] ChromaDB not found at absolute path: {CHROMA_PATH}")
        st.stop()
        
    db = Chroma(persist_directory=CHROMA_PATH, embedding_function=embeddings)
    
    # ----------------------------------
    # Step B: Setup LLM (Answer)
    # ----------------------------------
    if "Local" in llm_mode:
        # 1. Local Option
        llm = ChatOllama(base_url="http://localhost:11434", model="qwen2.5:1.5b")
        
    elif "Cloud" in llm_mode:
        # 2. Ollama Cloud Option
        ollama_key = os.getenv("OLLAMA_API_KEY")
        if not ollama_key:
            st.sidebar.error("Missing OLLAMA_API_KEY in .env")
            st.stop()
        # Using a proven generative model from their cloud
        llm = ChatOllama(
            base_url="https://ollama.com", 
            model="gpt-oss:120b", 
            client_kwargs={"headers": {"Authorization": f"Bearer {ollama_key}"}}
        )
        
    elif "Google" in llm_mode:
        # 3. Gemini Option
        google_key = os.getenv("GOOGLE_API_KEY")
        if not google_key:
            st.sidebar.error("Missing GOOGLE_API_KEY in .env")
            st.stop()
        llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", temperature=0.3)

# ----------------------------------
    # Step C: Combine into QA Chain
    # ----------------------------------
    custom_prompt_template = """Use the following pieces of context to answer the question at the end. 
    If you don't know the answer, just say that you don't know.
    
    CRITICAL FORMATTING RULE: You MUST format all mathematical variables, formulas, and equations using standard LaTeX delimiters. 
    Use a single $ for inline math (e.g., $V_{{GS}}$ or $I_{{D}}$) and double $$ for display/block math. 
    Never use parentheses like (V_{{GS}}) for mathematical notation.

    Context: {context}

    Question: {question}
    Helpful Answer:"""
    
    QA_PROMPT = PromptTemplate(
        template=custom_prompt_template, 
        input_variables=["context", "question"]
    )

    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",
        retriever=db.as_retriever(search_kwargs={"k": 4}),
        chain_type_kwargs={"prompt": QA_PROMPT}
    )
    return qa_chain

# Initialize the chain based on sidebar selections
try:
    qa_chain = init_rag(embedding_choice, llm_choice)
except Exception as e:
    st.error(f"Error initializing RAG: {e}")
    st.stop()

# ==========================================
# Chat Interface
# ==========================================
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display Chat History
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Handle User Input
if prompt := st.chat_input("Ask a technical question (e.g., How does an Op-Amp work?)..."):
    # Add user message to state and display
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Get and display AI response
    with st.chat_message("assistant"):
        with st.spinner(f"Thinking using {llm_choice}..."):
            try:
                response = qa_chain.invoke(prompt)
                answer = response["result"]
                st.markdown(answer)
                st.session_state.messages.append({"role": "assistant", "content": answer})
            except Exception as e:
                st.error(f"Error during generation: {e}")
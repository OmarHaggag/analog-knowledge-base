graph TD
    %% Project: Analog Devices Knowledge Base (Web Scraper + RAG)
    
    %% Ingestion Pipeline
    subgraph Offline Ingestion Phase
        Web[Analog Devices Website]
        Scraper[Web Scraper\ne.g., BeautifulSoup]
        Markdown[Markdown Files]
        Splitter[Text Splitter]
        EmbedModel((Embedding Model\nOllama))
        Chroma2[(ChromaDB\nAnalog Course)]
        
        Web -->|Crawl| Scraper
        Scraper -->|Convert| Markdown
        Markdown -->|Chunk| Splitter
        Splitter -->|Vectorize| EmbedModel
        EmbedModel -->|Store| Chroma2
    end

    %% Retrieval Pipeline
    subgraph Retrieval Phase
        User2((User))
        ChatUI[Simple Chat UI / CLI]
        RAG[RAG Chain\nLangChain/LlamaIndex]
        LLM2((LLM Provider))

        User2 -->|Ask Circuit Q| ChatUI
        ChatUI --> RAG
        RAG -->|1. Retrieve| Chroma2
        RAG -->|2. Context + Query| LLM2
        LLM2 -->|3. Answer| ChatUI
    end

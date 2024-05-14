Local document loader utilizing OpenAI GPT-4 and document store.

Expects your personal documents to be in folder "data" or "data_en" under this folder.

Embedding model used to vectorize documents: all-MiniLM-L6-v2 or Finnish embbedings from Turku University

**Pre-requisites:**

1. brew install poppler
2. brew install tesseract
3. python -m venv venv
4. source venv/bin/activate
5. pip3 install -r requirements.txt
6. Modify set_api_key.sh with your own OpenAI API key

**Running:**

1. . ./set_api_key.sh
2. echo $OPENAI_API_KEY
3. Running with Finnish Documents:
- python3 index_documents.py - to create ChromaDB from documents in data folder.
- python3 load_documents.py - to load documents and use RAG and OpenAI to generate answer.
  
4. Running with English Documents:
- python3 index_documents_en.py - to create ChromaDB from documents in data_en folder.
- python3 load_documents_en.py - to load documents and use RAG and OpenAI to generate answer.
   





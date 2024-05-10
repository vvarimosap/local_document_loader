Local document loader utilizing OpenAI GPT-4 and document store.

Expects documents to be in folder "data" under this folder.

Embedding model: all-MiniLM-L6-v2

Pre-requisites: 

1. brew install poppler
2. brew install tesseract
3. pip3 install -r requirements.txt
4. Modify set_api_key.sh with your own OpenAI API key

Running:

1. . ./set_api_key.sh
2. echo $OPENAI_API_KEY
3. Finnish Documents:
  3a. python3 index_documents.py - to create ChromaDB from documents in data folder.
  3b. python3 load_documents.py - to load documents and use RAG and OpenAI to generate answer.
4. English Documents:
   4a. python3 index_documents_en.py - to create ChromaDB from documents in data_en folder.
   4b. python3 load_documents_en.py - to load documents and use RAG and OpenAI to generate answer.





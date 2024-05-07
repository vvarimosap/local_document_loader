# import langchain dir loader from document loaders
from langchain_community.document_loaders import DirectoryLoader

# directory path
directory = 'data_en'

# function to load the text docs
def load_docs(directory):
  loader = DirectoryLoader(directory,recursive=True,show_progress=True)
  documents = loader.load()
  return documents

documents = load_docs(directory)
print("Documents loaded: "+str(len(documents)))

# use text splitter to split text in chunks
from langchain.text_splitter import RecursiveCharacterTextSplitter

# split the docs into chunks using recursive character splitter
def split_docs(documents,chunk_size=1000,chunk_overlap=20):
  text_splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
  docs = text_splitter.split_documents(documents)
  return docs

# store the splitte documnets in docs variable
docs = split_docs(documents)

# embeddings using langchain
#from langchain.embeddings import SentenceTransformerEmbeddings
from langchain_community.embeddings import SentenceTransformerEmbeddings
embeddings = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2") 

# using chromadb as a vectorstore and storing the docs in it
#from langchain.vectorstores import Chroma
from langchain_community.vectorstores import Chroma
db = Chroma.from_documents(docs, embeddings, persist_directory="./chroma_db_en")

print("Database created in chroma_db_en folder.")
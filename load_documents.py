from langchain_community.embeddings import SentenceTransformerEmbeddings
#embeddings = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")
embeddings = SentenceTransformerEmbeddings(model_name="TurkuNLP/gpt3-finnish-small")#"all-MiniLM-L6-v2")

# using chromadb as a vectorstore and storing the docs in it
#from langchain.vectorstores import Chroma
from langchain_community.vectorstores import Chroma

db = Chroma(persist_directory="./chroma_db", embedding_function=embeddings)

# load the LLM model
from langchain_community.chat_models import ChatOpenAI
#model_name = "gpt-4-0613" 
model_name = "gpt-4"
llm = ChatOpenAI(model_name=model_name)


# Using q&a chain to get the answer for our query
from langchain.chains.question_answering import load_qa_chain
chain = load_qa_chain(llm, chain_type="stuff",verbose=True)

# write your query and perform similarity search to generate an answer
query = "Milloin takuutarkastus suoritetaan ja mikä oli urakkahinta ilman veroja?"
matching_docs = db.similarity_search(query)
print("DOCS: "+str(matching_docs))
answer =  chain.run(input_documents=matching_docs, question=query)
print("ANSWER: "+str(answer))

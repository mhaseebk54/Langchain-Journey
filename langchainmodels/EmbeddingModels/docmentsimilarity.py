
from langchain_huggingface import HuggingFaceEmbeddings
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

load_dotenv()



embedding = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
documents = [
    "Python is a programming language",
    "Langchain is a framework for developing applications powered by language models"]

query = "tell me about Langchain"

doc_embeddings = embedding.embed_documents(documents)
query_embedding = embedding.embed_query(query)

scores = cosine_similarity([query_embedding], doc_embeddings)[0]

index ,score = sorted(enumerate(scores), key=lambda x:x[1])[-1]

print(query)
print(documents[index])
print("Similarity Score: ", score)
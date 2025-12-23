from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

docs=[
    "Python is a programming language",
    "Langchain is a framework for developing applications powered by language models"
    
]
embedding = OpenAIEmbeddings(model="text-embedding-3-large",dimensions=32)

result = embedding.embed_documents(docs)

print(str(result))
from langchain_huggingface import HuggingFaceEmbeddings


embedding = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

docs=[
    "Python is a programming language",
    "Langchain is a framework for developing applications powered by language models"
]

result = embedding.embed_documents(docs)

print(str(result))
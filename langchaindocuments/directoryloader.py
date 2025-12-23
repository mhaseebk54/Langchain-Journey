from langchain_community.document_loader import DirectoryLoader, PyPDFLoader

loader = DirectoryLoader(
    path ='books',
    glob = '*.pdf',
    loader_cls = PyPDFLoader
)

docs = loader.lazy_load()

print(docs)
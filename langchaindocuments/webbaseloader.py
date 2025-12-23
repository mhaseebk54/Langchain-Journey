from langchain_community.document_loaders import WebBaseLoader
from langchain_ollama import ChatOllama
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate

model = ChatOllama(model="llama3.2:1b")

prompt = PromptTemplate(
    template='Answer the following question \n {question} from the following text - \n {text}',
    input_variables=['question','text']
)

parser = StrOutputParser()

url = 'http://127.0.0.1:8000/latest-url'
loader = WebBaseLoader(url)

docs = loader.load()


chain = prompt | model | parser 

print(chain.invoke({'question':'How to Start A Blog in 2025', 'text':docs[0].page_content}))
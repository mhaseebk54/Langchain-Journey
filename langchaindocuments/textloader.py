from langchain_community.document_loaders import TextLoader
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_ollama import ChatOllama


loader = TextLoader('cricket.txt', encoding='utf8')

documents = loader.load()

# print(documents[0])

# print(documents[0].page_content)

# print(documents[0].metadata)


model = ChatOllama(model="llama3.2:1b")

template = PromptTemplate(
    template='Write a summary for the following poem - \n {poem}',
    input_variables=['poem']
)

parser = StrOutputParser()

chain = template | model | parser


response = chain.invoke({"poem": documents[0].page_content})

print(response)
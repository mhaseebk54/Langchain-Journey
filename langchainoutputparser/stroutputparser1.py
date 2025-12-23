from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser


model = ChatOllama(model="tinyllama")


template1 = PromptTemplate(
    template='Write a detailed report on {topic}',
    input_variable=['topic']
)

template2 = PromptTemplate(
    template='Summarize the following text in a concise manner: {text}',
    input_variable=['text']
)

parser = StrOutputParser()

chain = template1| model| parser | template2 | model | parser

result = chain.invoke({'topic':'black hole'})
print(result)


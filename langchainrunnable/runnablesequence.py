from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableSequence
from langchain_core.output_parsers import StrOutputParser



prompt1 = PromptTemplate(
template="Write a Joke about {topic}",
input_variables=["topic"] 
) 

prompt2 = PromptTemplate(
template="Translate the following text to Urdu: {text}",
input_variables=["text"]    
)

model = ChatOllama(model="llama3.2:1b")

parser = StrOutputParser()

chain = RunnableSequence(prompt1, model, parser, prompt2, model, parser)

result = chain.invoke({"topic": "AI"})

print(result)

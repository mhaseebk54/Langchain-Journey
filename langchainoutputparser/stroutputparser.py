from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate



model = ChatOllama(model="tinyllama")


template1 = PromptTemplate(
    template='Write a detailed report on {topic}',
    input_variable=['topic']
)

template2 = PromptTemplate(
    template='Summarize the following text in a concise manner: {text}',
    input_variable=['text']
)

prompt1 = template1.invoke({'topic':'black hole'})

result = model.invoke(prompt1)

prompt2 = template2.invoke({'text':result.content})

result1 = model.invoke(prompt2)
print(result1.content)


from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableSequence,RunnableParallel, RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser

model = ChatOllama(model="llama3.2:1b")

prompt1 = PromptTemplate(
template = 'Generate a joke about {topic}',
input_variables = ['topic'] 
)

prompt2 = PromptTemplate(
template = 'Translate in to a Urdu: {text}',
input_variables = ['text']    
)

parser = StrOutputParser()


jokechain = RunnableSequence(prompt1, model, parser)

parallelchain = RunnableParallel({
    'joke': RunnablePassthrough(),
    'translate': RunnableSequence(prompt2, model, parser)
})

finalchain = RunnableSequence(
    jokechain,
    parallelchain
)

result = finalchain.invoke({'topic': 'AI'})

print(result)
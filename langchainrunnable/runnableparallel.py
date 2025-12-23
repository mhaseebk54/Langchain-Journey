from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableSequence,RunnableParallel
from langchain_core.output_parsers import StrOutputParser

model = ChatOllama(model="llama3.2:1b")


prompt1 = PromptTemplate(
template = 'Generate a tweet about {topic}',
input_variables = ['topic']
)

prompt2 = PromptTemplate(
template = 'Generate a LinkedIn post about {topic}',
input_variables = ['topic']
)

parser = StrOutputParser()

chain = RunnableParallel({
  'tweet' :  RunnableSequence(prompt1, model, parser),
 'linkedin' : RunnableSequence(prompt2, model, parser)
})

result = chain.invoke({'topic': 'AI'})

print(result['tweet'])
print(result['linkedin'])



from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableSequence,RunnableParallel, RunnablePassthrough,RunnableLambda
from langchain_core.output_parsers import StrOutputParser


def wordcount(str):
    return len(str.split())
    

prompt = PromptTemplate(
template="Write a Joke about {topic}",
input_variables=["topic"] 
)
 


model = ChatOllama(model="llama3.2:1b")

parser = StrOutputParser()

jokechain = RunnableSequence(prompt, model, parser)

parallelchain = RunnableParallel({
    'joke': RunnablePassthrough(),
    'length': RunnableLambda(wordcount)

})

finalchain = RunnableSequence(
    jokechain,
    parallelchain,
)
result = finalchain.invoke({'topic': 'AI'})

final_result = """{} \n word count - {}""".format(result['joke'], result['length'])
print(final_result)
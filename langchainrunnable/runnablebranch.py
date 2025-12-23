from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableSequence,RunnableParallel, RunnablePassthrough,RunnableLambda,RunnableBranch
from langchain_core.output_parsers import StrOutputParser

prompt1 = PromptTemplate(
    template='Write a detailed report on {topic}',
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template='Summarize the following text \n {text}',
    input_variables=['text']
)

model = ChatOllama(model="llama3.2:1b")

parser = StrOutputParser()


report_chain = RunnableSequence(prompt1, model, parser)

branchchain = RunnableBranch(
    (lambda x: len(x.split()) > 500, RunnableSequence(prompt2, model, parser)),
    RunnablePassthrough()
)

finalchain = RunnableSequence(report_chain, branchchain)

result = finalchain.invoke({'topic': 'The impact of AI on modern healthcare systems'})

print(result)
from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

prompt1 = PromptTemplate(
    template="Write a brief story about {topic}",
    input_variables=["topic"],
)


prompt2 = PromptTemplate(
    template = "Summarize the following story:\n\n{story}",
    input_variables = ["story"],

)

model = ChatOllama(model="tinyllama")

parser = StrOutputParser()

chain = prompt1 | model | parser | prompt2 | model| parser

result = chain.invoke({'topic':'cricket'})

print(result)

chain.get_graph().print_ascii()
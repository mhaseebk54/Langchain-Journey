from langchain_core.prompts import ChatPromptTemplate

template = ChatPromptTemplate([
    ("system", "You are a helpful {domain}assistant."),
    ("human", "tell me about {topic}.")

])

prompt = template.invoke({
    "domain": "science ",
    "topic": "quantum computing"
})
print(prompt)
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_ollama import OllamaLLM



model =OllamaLLM(model="tinyllama")


messages = [
    SystemMessage(content='You are a helpful assistant'),
    HumanMessage(content='what is langchain.'),
]

response = model.invoke(messages)

messages.append(AIMessage(content=response))

print(messages)


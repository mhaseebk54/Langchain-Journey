from langchain_ollama import OllamaLLM
from langchain_core.messages import HumanMessage,AIMessage,SystemMessage

model = OllamaLLM(model="tinyllama")

chathistory = [SystemMessage(content="You are a helpful assistant.")]

while True:
    userinput = input("You: ") 
    chathistory.append(HumanMessage(content=userinput))
    if userinput == "exit":
        break
    response = model.invoke(chathistory)
    chathistory.append(AIMessage(content=response.content))
    print("Bot: " + str(response.content))

print(chathistory)    
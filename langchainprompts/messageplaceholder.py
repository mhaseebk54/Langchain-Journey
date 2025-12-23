from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

template = ChatPromptTemplate([
    ("system", "You are a helpful customercare assistant."),
    MessagesPlaceholder(variable_name="chathistory"),
    ("human", "{query}")

])

chat_history = []
with open('chathistory.txt') as f:
    chat_history.extend(f.readlines())

print(chat_history)


prompt = template.invoke({'chathistory':chat_history, 'query':'Where is my refund'})

print(prompt)
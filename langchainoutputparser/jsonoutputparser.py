from langchain_ollama import ChatOllamaLLM
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.prompts import PromptTemplate


llm = ChatOllamaLLM(model="tinyllama")


parser = JsonOutputParser()


prompt = PromptTemplate(
    template="""
Give 5 facts about {topic}.

{format_instructions}
""",
    input_variables=["topic"],
    partial_variables={
        "format_instructions": parser.get_format_instructions()
    }
)

chain = prompt | llm | parser


result = chain.invoke({"topic": "Mars"})
print(result)

from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate

load_dotenv()


llm = ChatGroq(
    model="llama-3.1-8b-instant"
)

template1 = PromptTemplate(
    template= "Provide a text of reserch on {topic}",
    input_variables=["topic"],  
)

template2 = PromptTemplate(
    template ="Provide a summary of the follwing {text}",
    input_variables=["text"]
)

parser = StrOutputParser()

chain = template1 | llm | parser | template2 | llm | parser

result = chain.invoke({"topic":"Black Holes"})

print(result)



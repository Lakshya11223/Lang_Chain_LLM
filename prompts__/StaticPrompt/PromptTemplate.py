from langchain_core.prompts import PromptTemplate
from langchain_groq import ChatGroq
from dotenv import load_dotenv  

load_dotenv()

llm = ChatGroq(
    model  = "llama-3.1-8b-instant"
)

template2 = PromptTemplate(
    template="Greet this person in a friendly manner: {name}",
    input_variables=["name"]
)

result = llm.invoke(template2.invoke({"name":"Alice"}))

print(result.content)



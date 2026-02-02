from langchain_core.prompts import ChatPromptTemplate,MessagesPlaceholder
from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()

llm = ChatGroq( 
    model="llama-3.1-8b-instant"
)

chat = ChatPromptTemplate(
    [
        ("system","You are a customer support assistant. "),
        MessagesPlaceholder(variable_name="chat_history"),
        ("human",'{query}')
    ]
)

chat_history = []

with open("chat_history.txt","r") as file:
   chat_history.extend( file.readlines() )

formatted_prompt = chat.invoke({
    "chat_history": chat_history,
    "query": "when will I get my refund"
})


result = llm.invoke(formatted_prompt)

print(result.content)

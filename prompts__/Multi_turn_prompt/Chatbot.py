from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage
load_dotenv()

# this is basic chatbot implementation simply it querry to groqss and print output main wotk is to understand How we keep responses for history

llm = ChatGroq(
    model="llama-3.1-8b-instant"   
)
chathistory = [
    SystemMessage(content="You are a helpful Ai assistant. ")
]

while True:
    user_input  = input("You: ")
    chathistory.append(HumanMessage(content=user_input))
    if(user_input == "exit" ): break
    result = llm.invoke(user_input)
    chathistory.append(AIMessage(content=result.content))
    print('AI :' , result.content )


print("Chat ended.")
print("Conversation History:")
print(chathistory)

# You see the  message like chat AIMessage(Hii...) , SystemMessage(...) , HumanMessage(..) in output



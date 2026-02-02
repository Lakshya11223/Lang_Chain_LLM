
from langchain_core.runnables import RunnableParallel
from langchain_groq import ChatGroq
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

groq = ChatGroq(model="llama-3.1-8b-instant")
gemini = ChatGoogleGenerativeAI(model="gemini-3-flash-preview")

template1= PromptTemplate(
    template = "Provide the notes of the given {text}",
    input_variables = ["text"]
)

template2 = PromptTemplate(
    template = "Provide the questions answer on the basis of the given {text}",
    input_variables = ["text"]
)

template3 = PromptTemplate(
    template="Merge the following thing : {notes} and {quiz}",
    input_variables=["notes", "quiz"]   
)
parser = StrOutputParser()
parallel = RunnableParallel({
    "notes" : template1 | groq | parser,
    "quiz" : template2 | gemini | parser,
    }
)

chain  = parallel | template3 | gemini |  parser

result = chain.invoke({
    "text" : "The Bhagat Singh"
})
print(result)

# what we do here first we create a template1 for first input and template 2 for second input using Runnable we do parallel processing of both inputs now we move on after parallel processing we go for a merging which is further done by chain 
# Note : chain.invoke gives input to both tamplate1 and template2 simultaneously
from langchain_core.runnables import RunnableParallel, RunnableBranch, RunnableLambda
from langchain_groq import ChatGroq
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
from typing import Literal

load_dotenv()

groq = ChatGroq(model="llama-3.1-8b-instant")
gemini = ChatGoogleGenerativeAI(model="gemini-3-flash-preview")

class feedback(BaseModel):
    sentiment: Literal["positive", "negative"] = Field(
        description="Give the sentiment as positive or negative only"
    )

parser1 = PydanticOutputParser(pydantic_object=feedback)

template1 = PromptTemplate(
    template="""Analyze the sentiment of the following text and respond ONLY with valid JSON. 
    {format_instructions}
    Text: {text}
    Respond with ONLY the JSON object, no additional text or explanation.""",
    input_variables=["text"],
    partial_variables={"format_instructions": parser1.get_format_instructions()},
)

template2 = PromptTemplate(
     template="Provide a response to motivate user for the further feed back so we can improve our product user review is something like this your answer must be within 100 words -> {text}",
    input_variables=["text"]
)

template3 = PromptTemplate(
    template="Provide a response to appologise for the problem facing mentioned in the text within 100 words -> {text}",
    input_variables=["text"]
)

initial_chain = template1 | gemini | parser1

parser = StrOutputParser()

branch_chain = RunnableBranch(
    (lambda x: x.sentiment == "positive", template2 | groq | parser),
    (lambda x: x.sentiment == "negative", template3 | groq | parser),
    RunnableLambda(lambda x: "Could not find sentiment")
)

chain = initial_chain | branch_chain

result = chain.invoke({
    "text": "The mobile was fantastic with stunning visuals and better design."
})

print("Result:", result)
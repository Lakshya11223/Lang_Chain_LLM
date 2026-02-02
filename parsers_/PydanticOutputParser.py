from langchain_core.output_parsers import PydanticOutputParser
from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from pydantic import BaseModel, Field

load_dotenv()

llm = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0
)

class Address(BaseModel):
    street: str = Field(description="The street where the person lives")
    house_number: int = Field(description="The house number where the person lives")

class Person(BaseModel):
    name: str = Field(description="The name of the unknown person")
    age: int = Field(gt=0, description="The age of the unknown person in years")
    address: Address = Field(description="The address of the person")  # Add this!

parser = PydanticOutputParser(pydantic_object=Person)


template1 = PromptTemplate(
    template="Generate a random fictional person with name, age, and address. IMPORTANT: Respond with ONLY the JSON object. Do not include any explanations, code, or markdown formatting. \n{format_instructions}",
    input_variables=[],
    partial_variables={"format_instructions": parser.get_format_instructions()}
)

chain = template1 | llm | parser 


result = chain.invoke({})
print(result)

# if the llm is giving string and formating issues, you can always try to clean the output before parsing
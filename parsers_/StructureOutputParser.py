from langchain.output_parsers import StructuredOutputParser,ResponseSchema
from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
load_dotenv()

llm = ChatGroq(
    model="llama-3.1-8b-instant"
)

schema = [
    ResponseSchema(name="fact1",description="Fact 1 about the topic"),
    ResponseSchema(name="fact2",description="Fact 2 about the topic"),
    ResponseSchema(name="fact3",description="Fact 3 about the topic"),
]
parser = StructuredOutputParser.from_response_schemas(schema)

template1 = PromptTemplate(
    template= "Provide a text of reserch on {topic}/n {format_instruction}",
    input_variables=["topic"],
    partial_variables={"format_instruction": parser.get_format_instructions()}
)

chain = template1 | llm | parser 

print(chain.invoke({"topic":"Artificial Intelligence"}))






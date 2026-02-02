from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()

llm = ChatGroq(
    model="llama-3.1-8b-instant"
)

# Create an instance of JsonOutputParser
parser = JsonOutputParser()

template = PromptTemplate(
    template="Provide information about {text}\n{format_instruction}",
    input_variables=["text"],
    partial_variables={"format_instruction": parser.get_format_instructions()}  
)


prompt = template.invoke({"text": "Python programming"})
result = llm.invoke(prompt)

# Parse the output
parsed_result = parser.parse(result.content)
print(parsed_result)


# it gives output like this

# {'name': 'Python', 'language_type': 'High-Level', 'paradigm': 'Object-Oriented, Imperative', 'development_environment': 'Interpreted, Compiled', 'applications': {'web_development': 'Django, Flask', 'data_analysis': 'Pandas, NumPy, Matplotlib', 'artificial_intelligence': 'TensorFlow, Keras', 'automation': 'General-purpose scripting'}, 'operating_systems': ['Windows', 'macOS', 'Linux'], 'learning_difficulty': 'Easy'}

# Limitation : Not make the structure which is requaired by us. basically in this we have to use the structure which is given by the model.
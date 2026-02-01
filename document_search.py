from langchain_huggingface import HuggingFaceEmbeddings
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

embedding = HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2')

# text = "Delhi is capital of india"

# vector = embedding.embed_query(text)

document  = [
    "Virat Kohli is an Indian cricketer known for his aggressive batting and leadership.",
    "MS Dhoni is a former Indian captain famous for his calm demeanor and finishing skills.",
    "Sachin Tendulkar, also known as the 'God of Cricket', holds many batting records.",
    "Rohit Sharma is known for his elegant batting and record-breaking double centuries.",
    "Jasprit Bumrah is an Indian fast bowler known for his unorthodox action and yorkers."
]

querry = "tell me about virat"

doc_embedding = embedding.embed_documents(document)
querry_embedding = embedding.embed_query(querry)

similarity = cosine_similarity([querry_embedding],doc_embedding)[0] # it take 2D arrays only

# print(similarity)

# print(sorted(list(enumerate(similarity)),key=lambda x:x[1]))
 
index , score = sorted(list(enumerate(similarity)),key=lambda x:x[1])[-1]

print(querry)
print(document[index])
print("similarity score is:", score)







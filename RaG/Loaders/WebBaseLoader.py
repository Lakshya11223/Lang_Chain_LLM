from langchain_community.document_loaders import WebBaseLoader

loader = WebBaseLoader("https://blog.python.org/")
docs = loader.load()

print(docs[0].page_content)

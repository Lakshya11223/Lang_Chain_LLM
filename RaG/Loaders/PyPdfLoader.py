from langchain_community.document_loaders import PyPDFLoader

document = PyPDFLoader("testfile.pdf").load()

print(document)

print(len(document)) # give number of pages loaded

print(document[0].page_content)
print(' ')
print(document[0].metadata)
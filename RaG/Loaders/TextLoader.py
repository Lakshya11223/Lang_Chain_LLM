from langchain_community.document_loaders import TextLoader


loader = TextLoader('text.txt', encoding='utf-8')

documents = loader.load()

print(documents)
print(' ')
print(documents[0].page_content)
print(' ')
print(documents[0].metadata)

# now you can use the documents as needed or you can give it to a chain or an LLM

from langchain_community.document_loaders import DirectoryLoader,PyPDFLoader

loader = DirectoryLoader(
    path = '///',
    glob='.pdf', 
    loader_cls=PyPDFLoader
)
print(len(loader.load())) # give number of pages loaded

# now load take time so you can also run lazy load

documents = loader.lazy_load() 

# it load one document/page at a time 
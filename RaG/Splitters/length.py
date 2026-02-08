from langchain_text_splitters import CharacterTextSplitter


Splitter = CharacterTextSplitter(
    chunk_size=200,
    chunk_overlap=0,
    separator=''
)

text = "This is a long text that needs to be split into smaller chunks. Each chunk will have a maximum length of 200 characters. The splitter will ensure that the chunks do not overlap and will use an empty string as the separator."

chunks = Splitter.split_text(text)

print(chunks)

# In this we devide the text using words and we can also use other separators like new line or comma. The chunk size is set to 200 characters and there is no overlap between the chunks.
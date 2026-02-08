from langchain_text_splitters import RecursiveCharacterTextSplitter

Splitter = RecursiveCharacterTextSplitter(
    chunk_size=100,
    chunk_overlap=0,
    separators=['\n\n', '\n', ' ', '']
)

text = """
Space exploration has led to incredible scientific discoveries. From landing on the Moon to exploring Mars, humanity continues to push the boundaries of whats possible beyond our planet.

These missions have not only expanded our knowledge of the universe but have also contributed to advancements in technology here on Earth. Satellite communications, GPS, and even certain medical imaging techniques trace their roots back to innovations driven by space programs.
"""

chunks = Splitter.split_text(text)

print(chunks[0])
print(chunks[1])

# basically it seprate firest on the basis of paragraph('\n\n') and then it seprate on the basis of new line if now also charachter limit is reached and we have to further split then it seprate on the basis of space and if still charachter limit is not reached then it seprate on the basis of charachter. This way we can ensure that we are not breaking sentences or words in the middle while splitting the text.

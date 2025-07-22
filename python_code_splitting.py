from langchain.text_splitter import RecursiveCharacterTextSplitter , Language

text = """
    def reverse_string(text):
    return text[::-1]

    def main():
        print("Welcome to the String Reverser!")
        user_input = input("Enter a string: ")
        reversed_text = reverse_string(user_input)
        print("Reversed string:", reversed_text)

if __name__ == "__main__":
    main()


"""

splitter = RecursiveCharacterTextSplitter.from_language(
    language = Language.PYTHON ,
    chunk_size = 300 , 
    chunk_overlap = 0
)

chunks = splitter.split_text(text)
print(len(chunks))
print(chunks[1])
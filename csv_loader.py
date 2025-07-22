from langchain_community.document_loaders import CSVLoader

loader = CSVLoader() # loader = CSVLoader(file_path='')  have to pass the file path here

docs = loader.load()

print(len(docs))
print(docs[0])
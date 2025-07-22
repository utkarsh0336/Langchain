from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader()   # give file path to loader(<file_path>)

docs = loader.load()

print(docs)
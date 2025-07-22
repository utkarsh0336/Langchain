from langchain_community.document_loaders import DirectoryLoader , PyPDFLoader

loader = DirectoryLoader(
    path='', # path to your directory,
    glob='', # glob pattern to match files inside the directory
    loader_cls=PyPDFLoader
)

docs = loader.load()

print(len(docs))

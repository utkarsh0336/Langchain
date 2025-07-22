from langchain_community.document_loaders import WebBaseLoader 
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI()

prompt = PromptTemplate(
    template='Answer the following question \n {question} from the following {text} - \n {text}',
    input_variables=['question' , 'text']
)

parser = StrOutputParser()


# url = "#########"   this url will be fetched in the below line
loader = WebBaseLoader()  # loader = WebBaseLoader(url)

docs = loader.load()

chain = prompt | model | parser
result = chain.invoke({'question' : 'What is the product that we are talking about?' , 'text' : docs[0].page_content})
print(result)




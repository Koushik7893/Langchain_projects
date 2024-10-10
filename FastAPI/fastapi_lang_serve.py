from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser
from fastapi import FastAPI
from langserve import add_routes
import os
from dotenv import load_dotenv

load_dotenv()

os.environ['GROQ_API_KEY'] = os.getenv('GROQ_API_KEY')
model = ChatGroq(model='Gemma2-9b-It')

system_message = "Translate the following into {language}"
prompt = ChatPromptTemplate([
    ("system",system_message),("user","{text}")
])

parser = StrOutputParser()
chain = prompt|model|parser

app=FastAPI(title='Langchain Server',
            version='1.0',
            description='A simple API server using Langchain runnable interfaces')

add_routes(app,
           chain,
           path='/chain')

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app,host="127.0.0.1",port=8000)
from fastapi import FastAPI
from langchain.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langserve import add_routes
import uvicorn
import streamlit as st 
import os
from langchain_ollama import OllamaLLM
from dotenv import load_dotenv
load_dotenv()

os.environ['OPENAI_API_KEY'] = os.getenv("OPEN_API_KEY")
os.environ['LANGCHAIN_API_KEY'] = os.getenv("LANGCHAIN_API_KEY") 
os.environ['LANGCHAIN_TRACING_V2'] = "true"

app = FastAPI(
    title="Langchain LLM API",
    version="1.0",
    description="A Multi-LLM API with Langchain"
)

# add_routes(
#     app,
#     OllamaLLM(),
#     path="/api"
# )

# Initialize LLM Models
# model = ChatOpenAI() 
model = ChatOpenAI()

#prompt templates
prompt1 = ChatPromptTemplate.from_template("Give a brief summary on {topic} with 100 words")
prompt2 = ChatPromptTemplate.from_template("Give a brief summary on {topic} with 100 words")

#Create API Routes with Langchain Pipelines
# add_routes(app, prompt1 | model, path="/essay")
add_routes(app, prompt1|model, path="/summary")

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)
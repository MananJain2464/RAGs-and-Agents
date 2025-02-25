from fastapi import FastAPI
from langchain.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI  
from langchain_huggingface import HuggingFaceEndpoint  
from langserve import add_routes
import uvicorn
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Set API keys
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
os.environ["HUGGINGFACEHUB_API_TOKEN"] = os.getenv("HUGGINGFACEHUB_API_TOKEN")

# Initialize FastAPI
app = FastAPI(
    title="Langchain Server",
    version="1.0",
    description="A simple API Server"
)

# Define models
openai_model = ChatOpenAI()

prompt1 = ChatPromptTemplate.from_template("Write me an essay about {topic} with 100 words")
prompt2 = ChatPromptTemplate.from_template("Write me an poem about {topic} in 50 words")

# Add API routes
add_routes(app, prompt1 | openai_model, path="/essay")
add_routes(app, prompt2 | openai_model, path="/poem")

# Run the FastAPI server
if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)

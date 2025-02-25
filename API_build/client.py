import requests
import streamlit as st

# Function to get OpenAI response (for the essay)
def get_openai_response(input_text):
    response = requests.post(
        "http://localhost:8000/essay/invoke",  # Correct endpoint
        json={"input": {"topic": input_text}}  # Correct JSON format
    )
    
    if response.status_code == 200:
        return response.json().get('output', {}).get('content', 'Error: No content found')
    else:
        return f"Error: {response.status_code} - {response.text}"

# Function to get DeepSeek response (for the poem)
def get_llm_response(input_text):
    response = requests.post(
        "http://localhost:8000/poem/invoke",  # Correct endpoint
        json={"input": {"topic": input_text}}  # Correct JSON format
    )
    
    if response.status_code == 200:
        return response.json().get('output', {}).get('content', 'Error: No content found')
    else:
        return f"Error: {response.status_code} - {response.text}"

# Streamlit app setup
st.title('API Integrated Chatbot')

# Input fields for article and poem generation
input_text = st.text_input('Write an article on:')
input_text1 = st.text_input('Write a poem on:')

# When article input is provided, call the OpenAI API
if input_text:
    st.write(get_openai_response(input_text))

# When poem input is provided, call the DeepSeek API
if input_text1:
    st.write(get_llm_response(input_text1))

import requests
import streamlit as st

# def get_openai_response(input_text):
#     response = requests.post(
#         "http://localhost:8000/essay/invoke",
#         json={'input': {'topic': input_text}})
#     return response.json()['output']['content']

def get_ollama_response(input_text):
    response = requests.post(
        "http://localhost:8000/summary/invoke",
        json={'input': {'topic': input_text}})
    return response.json()['output']["content"]

st.title('Langchain LLM Demo')
# input_text = st.text_input("USING OPENAI API: Write an essay on")#interact with openai
input_text1=st.text_input("Write a summary on")#interact with llama2
# if input_text:
#     st.write(get_openai_response(input_text))
if input_text1:
    st.write(get_ollama_response(input_text1))
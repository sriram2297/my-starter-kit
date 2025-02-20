# modules/api_utils.py

import openai



import os
from dotenv import load_dotenv

# Load environment variables from the config file
load_dotenv('config.env')






# Initialize the SambaNova API client
client = openai.OpenAI(
    api_key=os.getenv("api_key"),
    base_url=os.getenv('base_url'),
)

# Function to summarize text
def summarize_text(text):
    response = client.chat.completions.create(
        model='Meta-Llama-3.1-8B-Instruct',
        messages=[
            {"role": "system", "content": "You are an expert text summarizer."},
            {"role": "user", "content": f"Please summarize the following text: {text}"}
        ],
        temperature=0.1,
        top_p=0.1,
        max_tokens=500
    )
    summary = response.choices[0].message.content
    return summary

# Function to call Mistral-7B model API for Q&A
def ask_mistral_question(document_text, user_question):
    response = client.chat.completions.create(
        model='Meta-Llama-3.1-8B-Instruct',
        messages=[
            {"role": "system", "content": "You are a helpful assistant that answers questions based on the following document content."},
            {"role": "user", "content": f"Document Content: {document_text[:4000]} \n\n Question: {user_question}"}
        ],
        temperature=0.1,
        top_p=0.1
    )
    return response.choices[0].message.content

import openai
import os
from dotenv import load_dotenv

load_dotenv()

# Configure OpenRouter
client = openai.OpenAI(
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1"
)

def get_hint(problem_title, user_code):
    prompt = f"Problem Title: {problem_title}\nUser Code:\n{user_code}\n\nGive a hint to help improve or debug this code."
    
    chat = client.chat.completions.create(
        model="mistralai/mistral-7b-instruct",
        messages=[
            {"role": "system", "content": "You are a helpful assistant that gives smart programming hints."},
            {"role": "user", "content": prompt}
        ]
    )
    return chat.choices[0].message.content

def get_solution(problem_title):
    prompt = f"Problem: {problem_title}\n\nWrite a correct and optimized solution for this problem in Python."

    chat = client.chat.completions.create(
        model="mistralai/mistral-7b-instruct",
        messages=[
            {"role": "system", "content": "You are a helpful assistant who writes clean and optimal Python code."},
            {"role": "user", "content": prompt}
        ]
    )
    return chat.choices[0].message.content

def optimize_code(user_code):
    prompt = f"Here's some Python code:\n{user_code}\n\nCan you optimize this code for performance and readability?"

    chat = client.chat.completions.create(
        model="mistralai/mistral-7b-instruct",
        messages=[
            {"role": "system", "content": "You are a helpful assistant who makes code more efficient and readable."},
            {"role": "user", "content": prompt}
        ]
    )
    return chat.choices[0].message.content

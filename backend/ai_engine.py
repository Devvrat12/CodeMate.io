import openai
import os
from dotenv import load_dotenv

load_dotenv()

# Configure OpenRouter client
client = openai.OpenAI(
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1"
)

def get_hint(problem_title, description, user_code):
    prompt = (
        f"Problem Title: {problem_title}\n\n"
        f"Problem Description:\n{description}\n\n"
        f"User's Code:\n{user_code}\n\n"
        f"Give a helpful and constructive hint to improve or debug the above code. "
        f"Don't give the full solution."
    )

    chat = client.chat.completions.create(
        model="mistralai/mistral-7b-instruct",
        messages=[
            {"role": "system", "content": "You are a helpful assistant that gives insightful coding hints."},
            {"role": "user", "content": prompt}
        ]
    )
    return chat.choices[0].message.content


def get_solution(problem_title, description):
    prompt = (
        f"Problem Title: {problem_title}\n\n"
        f"Problem Description:\n{description}\n\n"
        f"Write a correct and optimized solution in Python for this problem."
    )

    chat = client.chat.completions.create(
        model="mistralai/mistral-7b-instruct",
        messages=[
            {"role": "system", "content": "You are a helpful assistant who writes clean and optimal Python code."},
            {"role": "user", "content": prompt}
        ]
    )
    return chat.choices[0].message.content


def optimize_code(user_code):
    prompt = (
        f"Here's some Python code:\n{user_code}\n\n"
        f"Can you optimize this code for both performance and readability without changing its logic?"
    )

    chat = client.chat.completions.create(
        model="mistralai/mistral-7b-instruct",
        messages=[
            {"role": "system", "content": "You are a helpful assistant who improves code quality."},
            {"role": "user", "content": prompt}
        ]
    )
    return chat.choices[0].message.content

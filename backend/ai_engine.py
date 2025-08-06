# backend/ai_engine.py

import openai
import os
from dotenv import load_dotenv

load_dotenv()

# ✅ OpenRouter client setup
client = openai.OpenAI(
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1"
)


def get_hint(problem_title, description, user_code, language="Python"):
    prompt = (
        f"You are a coding assistant. The user is solving a problem in {language}.\n\n"
        f"🔹 Problem Title: {problem_title}\n"
        f"🔹 Description:\n{description}\n\n"
        f"🔹 User Code ({language}):\n{user_code}\n\n"
        f"👉 Give a constructive hint to help the user debug or improve their code — "
        f"but DO NOT give the full solution."
    )

    chat = client.chat.completions.create(
        model="mistralai/mistral-7b-instruct",
        messages=[
            {"role": "system", "content": "You are a helpful assistant that gives insightful and language-specific coding hints."},
            {"role": "user", "content": prompt}
        ]
    )
    return chat.choices[0].message.content


def get_solution(problem_title, description, language="Python"):
    prompt = (
        f"You are a coding assistant.\n\n"
        f"🔹 Problem Title: {problem_title}\n"
        f"🔹 Description:\n{description}\n\n"
        f"👉 Write a correct and optimal solution to this problem in {language}."
    )

    chat = client.chat.completions.create(
        model="mistralai/mistral-7b-instruct",
        messages=[
            {"role": "system", "content": "You are a helpful assistant that writes clean and optimal solutions in various programming languages."},
            {"role": "user", "content": prompt}
        ]
    )
    return chat.choices[0].message.content


def optimize_code(user_code, language="Python"):
    prompt = (
        f"You are a code reviewer.\n\n"
        f"🔹 Language: {language}\n"
        f"🔹 Original Code:\n{user_code}\n\n"
        f"👉 Optimize this code for performance, readability, and best practices in {language}. "
        f"Do not change the logic unless necessary."
    )

    chat = client.chat.completions.create(
        model="mistralai/mistral-7b-instruct",
        messages=[
            {"role": "system", "content": "You are a helpful assistant who improves code quality while respecting language-specific best practices."},
            {"role": "user", "content": prompt}
        ]
    )
    return chat.choices[0].message.content

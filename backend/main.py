# backend/main.py

from fastapi import FastAPI
from pydantic import BaseModel
from ai_engine import get_hint, get_solution, optimize_code


app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to CodeMateAI Backend"}

class CodeRequest(BaseModel):
    problem_title: str
    user_code: str
    action: str #"hint", "solution", "optimize"
    
@app.post("/analyze")
def analyze(request: CodeRequest):
    if request.action == "hint":
        return {"response": get_hint(request.problem_title, request.user_code)}
    elif request.action == "solution":
        return {"response": get_solution(request.problem_title)}
    elif request.action == "optimize":
        return {"response": optimize_code(request.user_code)}
    else:
        return {"error": "Invalid action"}
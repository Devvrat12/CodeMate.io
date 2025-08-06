# backend/main.py

from fastapi import FastAPI
from fastapi import Request
import traceback
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from ai_engine import get_hint, get_solution, optimize_code

app = FastAPI()

# Enable CORS to allow extension communication
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "chrome-extension://hnflmhldncjiinhmgakkjaepmdmmaocm",  # your extension ID
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "Welcome to CodeMateAI Backend"}

# Request schema
class CodeRequest(BaseModel):
    problem_title: str
    description: str
    user_code: str
    action: str  # "hint", "solution", or "optimize"
    language: str = "Python"

@app.post("/analyze")
def analyze(request: CodeRequest):
    try:
        if request.action == "hint":
            return {
                "response": get_hint(request.problem_title, request.description, request.user_code, request.language)
            }
        elif request.action == "solution":
            return {
                "response": get_solution(request.problem_title, request.description, request.language)
            }
        elif request.action == "optimize":
            return {
                "response": optimize_code(request.user_code, request.language)
            }
        else:
            return {"error": "Invalid action"}
    except Exception as e:
        print("❌ Backend Exception:")
        traceback.print_exc()
        return {"error": f"Internal server error: {str(e)}"}
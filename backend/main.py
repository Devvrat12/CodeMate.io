# backend/main.py

from fastapi import FastAPI
from pydantic import BaseModel
from ai_engine import get_hint, get_solution, optimize_code
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Welcome to CodeMateAI Backend"}


# ✅ Updated CodeRequest to include description
class CodeRequest(BaseModel):
    problem_title: str
    description: str
    user_code: str
    action: str  # "hint", "solution", "optimize"


# ✅ Pass description to AI engine functions where applicable
@app.post("/analyze")
def analyze(request: CodeRequest):
    if request.action == "hint":
        return {
            "response": get_hint(request.problem_title, request.description, request.user_code)
        }
    elif request.action == "solution":
        return {
            "response": get_solution(request.problem_title, request.description)
        }
    elif request.action == "optimize":
        return {
            "response": optimize_code(request.user_code)
        }
    else:
        return {"error": "Invalid action"}


# ✅ CORS to allow extension communication
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # or specify: ["chrome-extension://<your-extension-id>"]
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

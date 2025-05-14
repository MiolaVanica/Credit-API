from fastapi import FastAPI
from pydantic import BaseModel
from dotenv import load_dotenv
import os

load_dotenv()

app = FastAPI()

credit_msg = "Made with 💖✨ By @SCDP3"
password = os.getenv("API_PASSWORD", "root")

class EditRequest(BaseModel):
    msg: str
    password: str

@app.get("/get")
async def get_credit():
    return {"message": credit_msg}

@app.post("/edit")
async def edit_credit(request: EditRequest):
    if request.password != password:
        return {"error": "Wrong password"}
    global credit_msg
    credit_msg = request.msg
    return {"message": "Credit updated"}
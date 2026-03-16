from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from model import generate_perfume

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class RequestData(BaseModel):
    ingredients: list
    category: str


@app.post("/generate")
def generate(data: RequestData):

    result = generate_perfume(
        data.ingredients,
        data.category
    )

    return result
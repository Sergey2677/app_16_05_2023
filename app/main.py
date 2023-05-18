# import datetime
from datetime import datetime

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(
    title='Test app'
)


class Question(BaseModel):
    id: int
    question: str
    answer: str
    created_at: datetime


@app.get('/')
async def get_main_page():
    return "Hello world!"


@app.post("/get_question", response_model=Question)
async def get_question_from_quiz():
    return {
        'id': 1,
        'question': 'This strategic peninsula became part of Ukraine in 1954',
        'answer': 'the Crimea',
        'created_at': datetime.strptime('2022-12-30T19:20:08.616Z', "%Y-%m-%dT%H:%M:%S.%fZ")
    }

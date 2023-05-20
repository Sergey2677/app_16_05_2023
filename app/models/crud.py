import logging

from models.db import database, questions
from validation import QuestionResponseFromService


async def create_question(payload: QuestionResponseFromService):
    query = questions.insert().values(payload.dict())
    return await database.execute(query=query)


async def read_question(payload: QuestionResponseFromService):
    query = questions.select().where(questions.c.question_id == payload.question_id)
    return await database.execute(query=query)


async def read_last_question():
    query = questions.select().order_by(questions.c.id.desc()).limit(1)
    result = await database.fetch_one(query=query)
    return result

from pydantic import BaseModel, Field
from typing import List


class QuestionResponseFromService(BaseModel):
    question_id: int = Field(ge=0, alias='id')
    question: str
    answer: str
    created_at: str


class QuestionResponseFromServiceList(BaseModel):
    questions: List[QuestionResponseFromService]


class QuestionRequestFromUser(BaseModel):
    questions_num: int = Field(ge=0)


class QuestionResponseToUser(BaseModel):
    question_id: int
    question: str
    answer: str
    created_at: str


class User(BaseModel):
    user_id: int
    name: str
    uuid: str

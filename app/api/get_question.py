from fastapi import APIRouter
from pydantic import ValidationError
import aiohttp
import logging
import datetime
from typing import Union

from models import crud
from validation import \
    QuestionRequestFromUser, \
    QuestionResponseFromService, \
    QuestionResponseFromServiceList, \
    QuestionResponseToUser

_logger = logging.getLogger('uvicorn')

router = APIRouter()


@router.post("/get_question", response_model=Union[QuestionResponseToUser, list])
async def get_question_from_quiz(payload: QuestionRequestFromUser):
    """The method processes POST request from user and
    make a response with the last loaded entry in questions table if exists, else response with clear list"""
    response_from_service: QuestionResponseFromServiceList = await get_question_from_service(payload.questions_num)
    # Select the last entry in the database
    response_to_user = await crud.read_last_question()
    # Loop through each question received from the service
    # to check if the question is already stored in the database or not,
    # if so, the rec method will be called which will call the service`s API until it receives a unique question.
    for question in response_from_service.questions:
        if await crud.read_question(question):
            question = await rec(question)
        await crud.create_question(question)
    return response_to_user if response_to_user else []


async def get_question_from_service(number: int) -> QuestionResponseFromServiceList:
    """The method makes a request to a third party service to get question(s) from
    quiz in the amount that was received in method`s attribute {number} """
    async with aiohttp.ClientSession() as session:
        url = f'https://jservice.io/api/random?count={number}'
        async with session.get(url) as resp:
            try:
                return QuestionResponseFromServiceList(questions=await resp.json())
            except ValidationError as e:
                _logger.error(f'{datetime.datetime.now()} Error processing API({url}) response: {e}')


async def rec(question: QuestionResponseFromService) -> QuestionResponseFromService:
    """The method calls the quiz`s API until it receives a question that is not stored in the database"""
    while await crud.read_question(question):
        response = await get_question_from_service(10)
        for quest in response.questions:
            if not await crud.read_question(quest):
                question = quest
                break
    return question

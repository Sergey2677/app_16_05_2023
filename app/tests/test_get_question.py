import json
import logging
from validation import QuestionResponseToUser, QuestionResponseFromService
from models import crud

_logger = logging.getLogger('uvicorn')


def test_get_question_from_quiz(test_app, monkeypatch, db):
    response = test_app.post('/get_question', content=json.dumps({"questions_num": 1}))

    async def test_create_question(payload):
        return 1

    monkeypatch.setattr(crud, 'create_question', test_create_question)
    assert response.status_code == 200
    data = response.json()
    assert QuestionResponseToUser(**data)


def test_get_question_from_quiz_invalid_payload(test_app, db):
    response = test_app.post('/get_question', content=json.dumps({"test": 1}))
    assert response.status_code == 422

from fastapi import APIRouter, status

from validation import User

router = APIRouter()


@router.post("/create_user", response_model=User, status_code=status.HTTP_201_CREATED)
def create_user():
    user_id = 1
    name = 'name'
    uuid = 'a5764857-ae35-34dc-8f25-a9c9e73aa898'
    return {'user_id': user_id, 'name': name, 'uuid': uuid}

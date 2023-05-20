from fastapi import APIRouter

router = APIRouter()


@router.post('/add_media')
def add_media():
    return {"status": "200 OK"}

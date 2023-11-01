from typing import List
from fastapi import APIRouter
from fastapi import HTTPException
from fastapi import Body
from machine_learning.predict import sleep_wake_classification


sleep_data_router = APIRouter(
    prefix="/api",
    responses={404: {"description": "Not found"}},
)


@sleep_data_router.post("/sleep/data")
async def receive_subject_id_api(subject_id: int = Body(...)):
    print(subject_id)
    return {"sleep_list" : sleep_wake_classification(subject_id=subject_id)}

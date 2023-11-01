from fastapi import APIRouter
from fastapi import HTTPException
from fastapi import Body
from machine_learning.predict import sleep_wake_classification

watch_data_router = APIRouter(
    prefix="/api",
    responses={404: {"description": "Not found"}},
)

@watch_data_router.post("/watch/data")
async def receive_sleep_counter_api(conuter: int = Body(...)):
    return {"watch_list" : [0] * conuter}
from typing import List
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from fastapi import FastAPI, Request
from fastapi import Body
import json

ai_router = APIRouter()


@ai_router.get("/")
async def root():
    return {"message": "hello world"}


@ai_router.get("/sean")
async def root():
    ###데이터를 반환해주는 함수입니다.
    return "123"


@ai_router.post("/user/id=[30,30,30]")
async def root():
    id = id
    # result = model(id)
    return id


@ai_router.post("/sleepData")
async def receive_data(request: Request, data: List[str] = Body(...)):
    try:
        # 전송된 데이터를 받아옵니다.
        # 리스트 데이터를 사용하려면 json.loads를 사용하여 파싱합니다.
        data_list = data[1]

        # 데이터 처리 로직 작성
        # 예시로 리스트 데이터를 그대로 반환하는 코드입니다.
        print("success")
        return JSONResponse(content=data_list, status_code=200)
    except Exception as e:
        print("fail:", str(e))
        return JSONResponse(content={"message": "Invalid JSON data"}, status_code=400)

    # try:
    #     data = await request.json()
    #     # 전송된 데이터를 받아옵니다.
    #     # 리스트 데이터를 사용하려면 json.loads를 사용하여 파싱합니다.
    #     data_list = json.load(data)

    #     # 데이터 처리 로직 작성
    #     # 예시로 리스트 데이터를 그대로 반환하는 코드입니다.
    #     print('success')
    #     return JSONResponse(content=data_list, status_code=200)
    # except json.JSONDecodeError:
    #     print('fail')
    #     return JSONResponse(content={"message": "Invalid JSON data"}, status_code=400)

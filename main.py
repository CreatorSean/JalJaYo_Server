from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from apis.version1.ai_router import ai_router
from apis.sleep_data_router import sleep_data_router
from apis.watch_data_router import watch_data_router

app = FastAPI()
# cm = cachemanager.CacheManager()

# CORS 설정
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router=ai_router)
app.include_router(router=sleep_data_router)
app.include_router(router=watch_data_router)

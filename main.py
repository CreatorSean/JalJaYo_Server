from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from apis.version1.ai_router import ai_router
from apis.sleep_data_router import sleep_data_router

# import cachemanager
# import database as db
# from routes.flutter_routes import flutter_router
# from routes.patient_routes import patient_router
# from routes.alarm_routes import alarm_router
# from routes.alarmType_routes import alarmType_router
# from routes.room_routes import room_router
# from routes.download_routes import download_router
# from routes.simul_alarm_routes import simulationAlarm_router
# from routes.watch_routes import watch_router
# from constants import absolute_path

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

# 플러터 웹 파일 static file 선언
# app.mount(
#     "/web",
#     StaticFiles(directory=absolute_path + "/web/"),
#     name="web",
# )

# app.include_router(router=flutter_router)
# app.include_router(router=patient_router)
# app.include_router(router=alarm_router)
# app.include_router(router=alarmType_router)
# app.include_router(router=room_router)
# app.include_router(router=download_router)
# app.include_router(router=simulationAlarm_router)
# app.include_router(router=watch_router)
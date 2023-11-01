import uvicorn
from multiprocessing import Process

# from looper.watch_status_overseer import oversee_watch_status
# from time import sleep


def server():
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=7700,
        reload=True,
        workers=9,
    )


if __name__ == "__main__":
    Process(target=server).start()
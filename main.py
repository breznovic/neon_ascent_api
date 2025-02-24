from fastapi import FastAPI
from database import engine
from models import Base
from routers import characters
from fastapi import WebSocket


Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.include_router(characters.router)
@app.get("/")
def read_root():
    return {"message": "Welcome to Neon Ascent RPG!"}


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        await websocket.send_text(f"Message text was: {data}")

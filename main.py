from fastapi import FastAPI, WebSocket
from database import engine
from models import Base
from routers import characters, auth, questions, weapons
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

Base.metadata.create_all(bind=engine)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(characters.router)
app.include_router(auth.router)
app.include_router(questions.router)
app.include_router(weapons.router)


@app.get("/")
def read_root():
    return {"message": "Welcome to Neon Ascent RPG!"}
   


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        await websocket.send_text(f"Message text was: {data}")

from fastapi import FastAPI
from routes.plato import plato

app = FastAPI(
    title = "API Rest con MySQL chachi pistachi"
)

app.include_router(plato)


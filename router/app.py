from fastapi import FastAPI

from .main_router import main_router

app = FastAPI()
app.include_router(main_router)

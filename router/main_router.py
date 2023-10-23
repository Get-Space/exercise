from fastapi import APIRouter

from db.database import *
from models.models import *

db = MockDatabase()

main_router = APIRouter(prefix="/main")


@main_router.get("/")
async def root():
    return {"message": "Hello World"}


@main_router.get("/user/{username}")
def get_users(username):
    user = db.get_user(username)
    return {"user": user}


@main_router.get("/question/{id}")
def get_question(id):
    question = db.get_question(id)
    return {"question": question}


@main_router.post("/github_webhook")
def github_webhook(req: dict):
    available_questions = db.get_all_questions()
    user_responses = db.get_responses_for_user(req["username"])

    for question in available_questions:
        for response in user_responses:
            if question["id"] == response["question_id"]:
                continue
            else:
                return {"next_question": question}

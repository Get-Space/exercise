from fastapi import APIRouter

from db.database import *
from models.schema import *
import random

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
    question_weights = {question_id: available_questions[question_id]['weight'] for question_id in available_questions}
    max_weight = max(question_weights.values())
    highest_weight_questions = [question_id for question_id, weight in question_weights.items() if weight == max_weight]
    question_to_return =  random.choice(highest_weight_questions) if len(highest_weight_questions) > 1 else highest_weight_questions[0]

    for question_id, _ in available_questions.items():
        if not user_responses:
            return {"next_question": available_questions.get(question_to_return)}
        for response in user_responses:
            if question_id == response["question_id"]:
                continue
            else:
                return {"next_question": available_questions.get(question_to_return)}

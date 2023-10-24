import logging

from fastapi import APIRouter

from db.database import *
from models.schema import *

from .depends import get_highest_weight

db = MockDatabase()

main_router = APIRouter(prefix="/main")

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@main_router.get("/")
async def root():
    return {"message": "Hello World"}


@main_router.get("/user/{username}")
def get_users(username):
    logger.info(f"Request started for GET /main/user/{username}")

    user = db.get_user(username)

    logger.info("Request 'get_users' completed.")
    return {"user": user}


@main_router.get("/question/{id}")
def get_question(id):
    logger.info(f"Request started for GET /main/question/{id}")
    question = db.get_question(id)
    logger.info("Request 'get_question' completed.")
    return {"question": question}


@main_router.post("/github_webhook")
def github_webhook(req: dict):
    logger.info("Request started for POST /main/github_webhook")
    available_questions = db.get_all_questions()
    user_responses = db.get_responses_for_user(req["username"])
    question_to_return = get_highest_weight(questions=available_questions)

    for question_id, _ in available_questions.items():
        if not user_responses:
            logger.info("Request completed. User hasn't responded to any questions.")
            return {"next_question": available_questions.get(question_to_return)}
        for response in user_responses:
            if question_id == response["question_id"]:
                continue
            else:
                logger.info("Request completed returning new question.")
                return {"next_question": available_questions.get(question_to_return)}

    logger.info("Request 'github_webhook' completed.")

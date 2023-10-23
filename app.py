from fastapi import FastAPI
from models import *
from database import *

db = MockDatabase()
app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/user/{username}")
def get_users(username):
    user = db.get_user(username)
    return {"user": user}

@app.get("/question/{id}")
def get_question(id):
    question = db.get_question(id)
    return {"question": question}

@app.post("/github_webhook")
def github_webhook(req: dict):
    available_questions = db.get_all_questions()
    user_responses = db.get_responses_for_user(req['username'])

    for question in available_questions:
        for response in user_responses:
            if question['id'] == response['question_id']:
                continue
            else:
                return {"next_question": question}
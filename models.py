from pydantic import BaseModel, Field
from enum import Enum
from typing import List

class QuestionType(str, Enum):
    rating = 'rating'
    multiple_choice = 'multiple_choice'

class User(BaseModel):
    username: str

class QuestionResponse(BaseModel):
    label: str = Field(..., description='The label for the response')
    value: int = Field(..., description='The value for the response')

class Question(BaseModel):
    id: int
    question: str
    type: QuestionType
    available_responses: List[QuestionResponse]

class Response(BaseModel):
    question_id: int
    user: User
    response_question_response: QuestionResponse
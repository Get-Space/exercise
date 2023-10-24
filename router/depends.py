import random


def get_highest_weight(questions: dict) -> str:
    """Returns the id of the question with the highest weight or if it has more than 1 value with the highest weight, returns randomly"""
    question_weights = {
        question_id: questions[question_id]["weight"] for question_id in questions
    }
    max_weight = max(question_weights.values())
    highest_weight_questions = [
        question_id
        for question_id, weight in question_weights.items()
        if weight == max_weight
    ]
    return (
        random.choice(highest_weight_questions)
        if len(highest_weight_questions) > 1
        else highest_weight_questions[0]
    )

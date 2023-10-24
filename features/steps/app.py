import logging

from behave import given, then, when

logger = logging.getLogger(__name__)


@when("I retrieve user {username}")
def step_impl(context, username):
    context.response = context.api.get(f"/user/{username}")


@then("I receive user {username}")
def step_impl(context, username):
    assert context.response.json()["user"]["username"] == username


@when("A GitHub Webhook is received for user {username}")
def step_impl(context, username):
    context.response = context.api.post("/github_webhook", json={"username": username})
    response_content = context.response.text  # Capture response content
    logger.info(f"Response content: {response_content}")


@then("I receive the next question")
def step_impl(context):
    assert "next_question" in context.response.json()

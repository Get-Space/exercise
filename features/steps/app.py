from behave import given, then, when


@when("I retrieve user {username}")
def step_impl(context, username):
    context.response = context.api.get(f"/user/{username}")


@then("I receive user {username}")
def step_impl(context, username):
    assert context.response.json()["user"]["username"] == username


@when("A GitHub Webhook is received for user {username}")
def step_impl(context, username):
    context.response = context.api.post("/github_webhook", json={"username": username})


@then("I receive the next question")
def step_impl(context):
    assert "next_question" in context.response.json()

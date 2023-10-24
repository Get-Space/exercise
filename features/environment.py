from fastapi.testclient import TestClient

from router.app import app


def before_scenario(context, feature):
    context.api = TestClient(app)

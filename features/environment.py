from fastapi.testclient import TestClient

from router.main_router import app


def before_scenario(context, feature):
    context.api = TestClient(app)

from app import app
from fastapi.testclient import TestClient

def before_scenario(context, feature):
    context.api = TestClient(app)

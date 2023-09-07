from fastapi.testclient import TestClient

from python_ground_up.main import app

test_client = TestClient(app)

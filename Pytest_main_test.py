from fastapi.testclient import TestClient
from Pytest_main_test import app


client = TestClient(app)

#Test Home API
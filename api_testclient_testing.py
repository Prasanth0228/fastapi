from fastapi.testclient import TestClient
from fastapi import status
from main import app
client = TestClient(app)
import pytest
def test_partno_get():
    response = client.get('parts/A06')
    print(response.json())
    assert response.status_code == status.HTTP_200_OK
    #assert response.json() == {"message": "welcome to FastAPI!"}

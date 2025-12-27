from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_get_students():
    response = client.get("/students")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert "Иван" in response.json()


def test_get_subjects():
    response = client.get("/subjects")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert "Математика" in response.json()


def test_get_progress():
    response = client.get(
        "/progress",
        params={"student": "Иван", "subject": "Математика"}
    )
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) > 0
    assert "score" in data[0]


def test_get_metrics():
    response = client.get(
        "/metrics",
        params={"student": "Иван", "subject": "Математика"}
    )
    assert response.status_code == 200
    data = response.json()
    assert "average_score" in data
    assert "trend" in data

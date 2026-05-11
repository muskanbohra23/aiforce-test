import json
import pytest
from app import create_app
from app.models import db

@pytest.fixture
def client():
    app = create_app()
    app.config["TESTING"] = True
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"
    db.init_app(app)
    with app.app_context():
        db.create_all()
    yield app.test_client()

def test_create_task(client):
    response = client.post("/api/tasks/", json={"title": "Test Task"})
    assert response.status_code == 201
    data = json.loads(response.data)
    assert data["title"] == "Test Task"

def test_get_tasks(client):
    client.post("/api/tasks/", json={"title": "Task 1"})
    response = client.get("/api/tasks/")
    assert response.status_code == 200
    data = json.loads(response.data)
    assert len(data) == 1

def test_update_task(client):
    client.post("/api/tasks/", json={"title": "Task to update"})
    response = client.put("/api/tasks/1", json={"status": "completed"})
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data["status"] == "completed"

def test_delete_task(client):
    client.post("/api/tasks/", json={"title": "Task to delete"})
    response = client.delete("/api/tasks/1")
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data["message"] == "Task deleted successfully"
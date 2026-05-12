import pytest
from fastapi.testclient import TestClient
from unittest.mock import MagicMock, patch
from web.backend.mission_board_server import MissionBoardServer

@pytest.fixture
def client():
    # Mock MissionBoardStateBuilder to avoid complex blackboard logic
    with patch('web.backend.mission_board_server.MissionBoardStateBuilder') as mock_builder:
        mock_builder.return_value.build_state.return_value = {"status": "ok", "test": True}

        # Instantiate server with a mock instruction handler
        mock_handler = MagicMock()
        server = MissionBoardServer(instruction_handler=mock_handler)

        # TestClient uses the FastAPI app directly
        with TestClient(server._app) as client:
            client.instruction_handler = mock_handler
            yield client

def test_get_state(client):
    response = client.get("/api/state")
    assert response.status_code == 200
    assert response.json() == {"status": "ok", "test": True}

def test_post_chat_success(client):
    response = client.post("/api/chat", json={"message": "move forward"})
    assert response.status_code == 200
    assert response.json() == {"status": "queued"}
    client.instruction_handler.assert_called_once_with("move forward")

def test_post_chat_empty_message(client):
    response = client.post("/api/chat", json={"message": "  "})
    assert response.status_code == 400
    assert "Message is required" in response.json()["detail"]

def test_post_chat_missing_handler():
    # Create server without handler
    server = MissionBoardServer(instruction_handler=None)
    with TestClient(server._app) as client:
        response = client.post("/api/chat", json={"message": "hello"})
        assert response.status_code == 503
        assert "unavailable" in response.json()["detail"]

def test_read_index_not_found(client):
    # This might fail if the file exists, but in a test environment we can mock it
    with patch('pathlib.Path.exists', return_value=False):
        response = client.get("/")
        assert response.status_code == 404

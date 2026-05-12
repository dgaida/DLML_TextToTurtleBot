import pytest
from unittest.mock import MagicMock, patch
from shared.blackboard.blackboard import Blackboard
from shared.blackboard.interfaces.blackboard_data_keys import BlackboardDataKey
from shared.events.interfaces.events import DomainEvent, EventType
from core.commands.user_command import UserCommand

@pytest.fixture
def blackboard():
    # Use a fresh blackboard for each test
    with patch('shared.blackboard.blackboard.EventBus'):
        bb = Blackboard(disable_event_bus_subscription=True)
        bb.data = {}
        return bb

def test_set_get(blackboard):
    blackboard._set("test_key", "test_value")
    assert blackboard.get("test_key") == "test_value"

def test_get_default(blackboard):
    assert blackboard.get("non_existent", "default") == "default"

def test_on_robot_is_turning_updated(blackboard):
    event = DomainEvent(EventType.ROBOT_IS_TURNING_UPDATED, True)
    blackboard._on_robot_is_turning_updated(event)
    assert blackboard.get(BlackboardDataKey.ROBOT_IS_TURNING) is True

def test_serialize_value(blackboard):
    data = {"a": 1, "b": [1, 2, {"c": 3}]}
    serialized = blackboard._serialize_value(data)
    assert serialized == data

    class MockObj:
        def __str__(self):
            return "mock"

    assert blackboard._serialize_value(MockObj()) == "mock"

def test_clear_commands(blackboard):
    blackboard._command_queue.append("cmd1")
    # Need a real UserCommand or mock that behaves like one for cleanup and isinstance check
    mock_cmd = MagicMock(spec=UserCommand)
    mock_cmd.command_id = "test_id"
    blackboard._set(BlackboardDataKey.ACTIVE_COMMAND, mock_cmd)

    blackboard.clear_commands()

    assert len(blackboard._command_queue) == 0
    assert blackboard.get(BlackboardDataKey.ACTIVE_COMMAND) is None

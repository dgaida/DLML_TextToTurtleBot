import pytest
from unittest.mock import MagicMock
from shared.events.event_bus import EventBus
from shared.events.interfaces.events import DomainEvent, EventType

@pytest.fixture(autouse=True)
def reset_event_bus():
    """Reset the EventBus singleton before each test."""
    bus = EventBus()
    bus._subscribers = {}
    bus._queue.clear()
    yield

def test_subscribe_and_publish():
    bus = EventBus()
    callback = MagicMock()
    event = DomainEvent(EventType.COMMAND_RECEIVED, "test_data")

    bus.subscribe(EventType.COMMAND_RECEIVED, callback)
    bus.publish(event)

    callback.assert_called_once_with(event)

def test_unsubscribe():
    bus = EventBus()
    callback = MagicMock()
    event = DomainEvent(EventType.COMMAND_RECEIVED, "test_data")

    bus.subscribe(EventType.COMMAND_RECEIVED, callback)
    bus.unsubscribe(EventType.COMMAND_RECEIVED, callback)
    bus.publish(event)

    callback.assert_not_called()

def test_multiple_subscribers():
    bus = EventBus()
    callback1 = MagicMock()
    callback2 = MagicMock()
    event = DomainEvent(EventType.COMMAND_RECEIVED, "test_data")

    bus.subscribe(EventType.COMMAND_RECEIVED, callback1)
    bus.subscribe(EventType.COMMAND_RECEIVED, callback2)
    bus.publish(event)

    callback1.assert_called_once_with(event)
    callback2.assert_called_once_with(event)

def test_callback_error_handling():
    bus = EventBus()
    error_callback = MagicMock(side_effect=Exception("Test error"))
    success_callback = MagicMock()
    event = DomainEvent(EventType.COMMAND_RECEIVED, "test_data")

    bus.subscribe(EventType.COMMAND_RECEIVED, error_callback)
    bus.subscribe(EventType.COMMAND_RECEIVED, success_callback)

    # Should not raise exception
    bus.publish(event)

    error_callback.assert_called_once()
    success_callback.assert_called_once()

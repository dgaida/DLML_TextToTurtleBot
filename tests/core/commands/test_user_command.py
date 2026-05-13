from core.commands.user_command import UserCommand, CommandType

def test_navigate_factory():
    cmd = UserCommand.navigate(x=1.0, y=2.0, theta=0.5)
    assert cmd.command_type == CommandType.NAVIGATE_TO_POSE
    assert cmd.parameters["pose"]["x"] == 1.0
    assert cmd.parameters["pose"]["y"] == 2.0
    assert cmd.parameters["pose"]["theta"] == 0.5

def test_drive_factory():
    cmd = UserCommand.drive(distance_m=1.5, direction="backward")
    assert cmd.command_type == CommandType.DRIVE
    assert cmd.parameters["distance_m"] == 1.5
    assert cmd.parameters["direction"] == "backward"

def test_rotate_factory():
    cmd = UserCommand.rotate(angle_deg=90.0, direction="left")
    assert cmd.command_type == CommandType.ROTATE
    assert cmd.parameters["angle_deg"] == 90.0
    assert cmd.parameters["direction"] == "left"

def test_find_object_factory():
    cmd = UserCommand.find_object(object_class="bottle")
    assert cmd.command_type == CommandType.FIND_OBJECT
    assert cmd.parameters["object_class"] == "bottle"

def test_dock_undock_factories():
    assert UserCommand.dock().command_type == CommandType.DOCK
    assert UserCommand.undock().command_type == CommandType.UNDOCK

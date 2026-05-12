import sys
from unittest.mock import MagicMock

# Mock ROS 2 and other system dependencies
mock_modules = [
    'rclpy',
    'rclpy.node',
    'std_msgs.msg',
    'geometry_msgs.msg',
    'sensor_msgs.msg',
    'nav2_msgs.action',
    'turtlebot4_msgs.action',
    'py_trees',
    'py_trees.behaviour',
    'py_trees.behaviours',
    'py_trees.common',
    'ultralytics',
    'pyrealsense2',
]

for mod_name in mock_modules:
    sys.modules[mod_name] = MagicMock()

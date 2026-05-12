# Docstring Guide

To ensure high-quality API documentation, we use the **Google Python Style Guide** for all docstrings.

## Basic Structure

Each docstring should contain a brief summary, a detailed description (if necessary), arguments, return values, and exceptions.

### Function Example

```python
def calculate_distance(point_a: Tuple[float, float], point_b: Tuple[float, float]) -> float:
    """Calculates the Euclidean distance between two points.

    This function uses the Pythagorean theorem to calculate the
    distance in a 2D coordinate system.

    Args:
        point_a (Tuple[float, float]): The (x, y) coordinates of the first point.
        point_b (Tuple[float, float]): The (x, y) coordinates of the second point.

    Returns:
        float: The calculated distance as a floating-point number.

    Example:
        >>> calculate_distance((0, 0), (3, 4))
        5.0
    """
    return ((point_a[0] - point_b[0])**2 + (point_a[1] - point_b[1])**2)**0.5
```

### Class Example

```python
class RobotController:
    """Controls the basic movements of the TurtleBot.

    Attributes:
        namespace (str): The robot's ROS namespace.
        is_sim (bool): Flag indicating if the robot is running in simulation.
    """

    def __init__(self, namespace: str, is_sim: bool = False):
        """Initializes the RobotController.

        Args:
            namespace (str): The namespace.
            is_sim (bool): Whether simulation is used. Defaults to False.
        """
        self.namespace = namespace
        self.is_sim = is_sim
```

## Compliance Check

We use **interrogate** to check docstring coverage. A CI step ensures that at least 95% of the code is documented.

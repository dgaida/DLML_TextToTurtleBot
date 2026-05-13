import math
from typing import Optional


class DetectedObject:
    def __init__(self, x1: int, y1: int, x2: int, y2: int, name: str, confidence: float):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.world_x: Optional[float] = None
        self.world_y: Optional[float] = None
        self.world_z: Optional[float] = None
        self.name = name
        self.confidence = confidence

    def has_world_coordinates(self) -> bool:
        return self.world_x is not None and self.world_y is not None and self.world_z is not None

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, DetectedObject):
            return False

        max_pixel_threshold = 10

        return (self.name == other.name and
                abs(self.x1 - other.x1) <= max_pixel_threshold and
                abs(self.y1 - other.y1) <= max_pixel_threshold and
                abs(self.x2 - other.x2) <= max_pixel_threshold and
                abs(self.y2 - other.y2) <= max_pixel_threshold)

    def distance_to_other_object(self, other_object: "DetectedObject") -> float:
        if not isinstance(other_object, DetectedObject):
            return float('inf')

        if not self.has_world_coordinates() or not other_object.has_world_coordinates():
            return float('inf')

        # Use local variables to help Mypy narrow down type to float
        sx, sy, sz = self.world_x, self.world_y, self.world_z
        ox, oy, oz = other_object.world_x, other_object.world_y, other_object.world_z

        if sx is None or sy is None or sz is None or ox is None or oy is None or oz is None:
            return float('inf')

        dx = sx - ox
        dy = sy - oy
        dz = sz - oz
        return math.sqrt(dx*dx + dy*dy + dz*dz)

    def distance_to_world_coordinates(self, world_x: float, world_y: float, world_z: float) -> float:
        if not self.has_world_coordinates():
            return float('inf')

        sx, sy, sz = self.world_x, self.world_y, self.world_z
        if sx is None or sy is None or sz is None:
            return float('inf')

        dx = sx - world_x
        dy = sy - world_y
        dz = sz - world_z
        return math.sqrt(dx*dx + dy*dy + dz*dz)

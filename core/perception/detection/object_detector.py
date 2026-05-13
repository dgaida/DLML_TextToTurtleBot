import math
from typing import Dict, List, Optional
from numpy import ndarray
from ultralytics import YOLO

from shared.events.event_bus import EventBus
from shared.events.interfaces.events import EventType, DomainEvent

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


class ObjectDetector:
    def __init__(self, model_path: str, confidence_threshold: float = 0.3):
        self._model = self._create_custom_yolo_model(model_path)
        self._event_bus = EventBus()
        self._confidence_threshold = confidence_threshold
    

    def _create_custom_yolo_model(self, model_path: str):
        model = YOLO(f"{model_path}/yolov8s-worldv2.pt")

        classes = ["table", "monitor", "closed door", "open door", "chair", "computer",
             "person", "fridge", "fire extinguisher", "window", "blackboard",
             "kitchen cabinet", "wall", "toilet", "towel", "radiator", "desk",
             "bin", "door"
             ]

        model.set_classes(
            classes
        )
        
        model.save(f"{model_path}/yolo_model_custom.pt")

        return model
    
    def detect(self, image: ndarray) -> None:
        results = self._model.predict(image, max_det=20, verbose=False)
        boxes = results[0].boxes
        names = results[0].names
        all_detections: Dict[str, List[DetectedObject]] = {}

        for i, box in enumerate(boxes):
            cls_id = int(boxes.cls[i])
            name = names[cls_id]

            if name.lower() == 'wall':
                continue

            coords = box.xyxy[0]
            x1, y1, x2, y2 = map(int, coords)
            confidence = float(boxes.conf[i])

            if confidence < self._confidence_threshold:
                continue

            detected_object = DetectedObject(x1, y1, x2, y2, name, confidence)

            if name not in all_detections:
                all_detections[name] = []
            all_detections[name].append(detected_object)

        self._event_bus.publish(DomainEvent(EventType.OBJECTS_DETECTED, all_detections))

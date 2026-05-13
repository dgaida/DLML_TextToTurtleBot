from typing import Dict, List, Optional, Union, Sequence
from shared.events.event_bus import EventBus
from shared.events.interfaces.events import EventType, DomainEvent
from shared.blackboard.blackboard import Blackboard
from shared.blackboard.interfaces.blackboard_data_keys import BlackboardDataKey
from core.perception.detection.object_detector import DetectedObject
import time
from rclpy.node import Node

class TemporaryTrackedObject:
    """Represents an object being tracked for consecutive frames before persistence."""
    def __init__(self, detected_object: DetectedObject):
        self.detected_object = detected_object
        self.consecutive_frames = 1
        self.first_seen_timestamp = time.time()
        self.last_seen_timestamp = time.time()
        self.frames_not_seen = 0

    def update(self, detected_object: DetectedObject) -> None:
        self.detected_object = detected_object
        self.consecutive_frames += 1
        self.last_seen_timestamp = time.time()
        self.frames_not_seen = 0

class PersistentTrackedObject:
    """Represents an object that has been confirmed as persistent."""
    def __init__(self, detected_object: DetectedObject):
        self.detected_object = detected_object
        self.first_seen_timestamp = time.time()
        self.last_seen_timestamp = time.time()
        self.total_detections = 1

    def update(self, detected_object: DetectedObject) -> None:
        self.detected_object = detected_object
        self.last_seen_timestamp = time.time()
        self.total_detections += 1

class Map:
    def __init__(self, node: Node):
        self._event_bus = EventBus()
        self._blackboard = Blackboard()

        self.consecutive_frame_threshold = 30
        self.max_processing_distance = 7.5
        self.match_distance_threshold = 0.5
        self.temporary_tracked_object_timeout = 5.0
        
        self.temporary_tracked_objects: List[TemporaryTrackedObject] = []
        self.persistent_tracked_objects: List[PersistentTrackedObject] = []

        self._timer = node.create_timer(0.1, self._process_map)


    def _process_map(self) -> None:
        robot_is_turning = self._blackboard.get(BlackboardDataKey.ROBOT_IS_TURNING, False)

        if robot_is_turning:
            return
        
        detected_objects_with_coordinates: Dict[str, List[DetectedObject]] = self._blackboard.get(BlackboardDataKey.DETECTED_OBJECTS_WITH_COORDINATES, {})
        if not detected_objects_with_coordinates:
            return

        detected_object_classes = set(detected_objects_with_coordinates.keys())

        for temp_object in self.temporary_tracked_objects:
            temp_object.frames_not_seen += 1

        for detected_object_class in detected_object_classes:
            for detected_object in detected_objects_with_coordinates[detected_object_class]:
                self._process_detected_object(detected_object)

        self._cleanup_and_promote_objects()
        self._event_bus.publish(DomainEvent(EventType.MAP_UPDATED, self.persistent_tracked_objects))
       
    
    def _process_detected_object(self, detected_object: DetectedObject) -> None:
        all_objects: List[Union[TemporaryTrackedObject, PersistentTrackedObject]] = []
        all_objects.extend(self.temporary_tracked_objects)
        all_objects.extend(self.persistent_tracked_objects)

        matching_object = self._find_matching_object(detected_object, all_objects)

        robot_position = self._blackboard.get(BlackboardDataKey.ROBOT_POSITION, None)
        if not robot_position:
            return
        
        distance_to_robot = detected_object.distance_to_world_coordinates(robot_position.x, robot_position.y, robot_position.z)

        if distance_to_robot > self.max_processing_distance:
            return

        if matching_object:
            matching_object.update(detected_object)
        else: 
            new_temp_object = TemporaryTrackedObject(detected_object)
            self.temporary_tracked_objects.append(new_temp_object)


    def _find_matching_object(
        self,
        detected_object: DetectedObject,
        object_list: Sequence[Union[TemporaryTrackedObject, PersistentTrackedObject]]
    ) -> Optional[Union[TemporaryTrackedObject, PersistentTrackedObject]]:
        best_match = None
        best_distance = float('inf')

        for obj in object_list:
            if not detected_object.name == obj.detected_object.name:
                continue
                
            distance = obj.detected_object.distance_to_other_object(detected_object)
            if distance < self.match_distance_threshold and distance < best_distance:
                best_distance = distance
                best_match = obj

        return best_match


    def _cleanup_and_promote_objects(self) -> None:
        current_time = time.time()
        objects_to_promote = []
        temporary_objects_to_keep = []

        for temp_object in list(self.temporary_tracked_objects):
            if (current_time - temp_object.last_seen_timestamp) > self.temporary_tracked_object_timeout:
                continue

            if temp_object.consecutive_frames >= self.consecutive_frame_threshold:
                objects_to_promote.append(temp_object)
            else:
                temporary_objects_to_keep.append(temp_object)

        self.temporary_tracked_objects = temporary_objects_to_keep

        for obj in objects_to_promote:
            self._promote_object(obj)


    def _promote_object(self, temp_obj: TemporaryTrackedObject) -> None:
        matching_persistent_object = self._find_matching_object(temp_obj.detected_object, self.persistent_tracked_objects)

        if matching_persistent_object:
            matching_persistent_object.update(temp_obj.detected_object)
        else:
            new_persistent_object = PersistentTrackedObject(temp_obj.detected_object)
            self.persistent_tracked_objects.append(new_persistent_object)

    def __str__(self) -> str:
        lines = ["Persistent Tracked Objects:"]
        for obj in self.persistent_tracked_objects:
            detected = obj.detected_object
            lines.append(
                f"- {detected.name} | "
                f"Detections: {obj.total_detections} | "
                f"Position: ({detected.world_x}, {detected.world_y}, {detected.world_z}) | "
                f"First seen: {time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(obj.first_seen_timestamp))} | "
                f"Last seen: {time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(obj.last_seen_timestamp))}"
            )
        return "\n".join(lines)

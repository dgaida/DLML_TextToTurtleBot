# Operation and Workflows

In this chapter, you will learn how to use TextToTurtleBot in daily operations and which workflows are supported.

## Interaction via the Dashboard

The web dashboard is the primary interface for the user.

1.  **Chat Interface**: Enter your commands here (e.g., "Drive to the kitchen").
2.  **Live Map**: Visualizes the robot's position and detected objects.
3.  **Camera Feed**: Shows the current live image from the TurtleBot camera including YOLO detections.

## Example Commands

Try the following commands:

-   *"Turn around 180 degrees."*
-   *"Drive forward 2 meters."*
-   *"Find a person and drive to them."*
-   *"What do you see right now?"* (Requires a vision-capable model like GPT-4o).

## Behavior with Obstacles

The robot uses the Nav2 stack for path planning. If an obstacle blocks the path:
1.  The robot attempts to navigate around the obstacle.
2.  If no path is found, the robot stops and reports the status in the dashboard.
3.  Recovery behaviors can be triggered via the Behavior Tree.

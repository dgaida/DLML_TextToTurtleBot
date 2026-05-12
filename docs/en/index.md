# TextToTurtleBot

![Interrogate Coverage](assets/interrogate.svg)

Welcome to the **TextToTurtleBot** documentation. This project enables natural language control of a TurtleBot 4 by integrating state-of-the-art LLMs (Large Language Models) and ROS 2.

## Project Overview

TextToTurtleBot bridges the gap between Artificial Intelligence and Robotics. Users can issue natural language commands to the robot, which are then translated into complex behavior trees and executed.

### Key Features

*   **Voice Control**: Direct interaction with the robot via text or speech.
*   **Intelligent Navigation**: Utilizing Nav2 for precise movement and obstacle avoidance.
*   **Object Detection**: Identifying and localizing objects within the environment.
*   **Web Dashboard**: Intuitive user interface for monitoring and control.
*   **Modular Architecture**: Easily extensible through skills and LLM adapters.

## Quickstart

```bash
# Start the simulation
./launch_simulator.sh

# Open the dashboard
# http://localhost:8000
```

For more information, see the [Getting Started Guide](getting-started.md).

# Getting Started

This guide will walk you through the process of setting up TextToTurtleBot in a simulation environment or on physical hardware.

## Prerequisites

Before you begin, ensure the following components are installed:

*   Python 3.10 or newer
*   ROS 2 (Jazzy or Humble recommended)
*   A valid API key for a supported LLM provider (OpenAI, Google Gemini, or local Ollama)

## Installation

Follow the instructions in the [Installation Guide](installation.md).

## Configuration

1.  Create a `core/.env` file with your API key:
    ```env
    OPENAI_API_KEY=sk-proj-...
    ```
2.  Adjust `core/llm_config.json` to select your preferred provider.

## Running in Simulation

For a quick test, using the Gazebo simulation is recommended:

1.  Activate your ROS 2 environment and the Python virtual environment.
2.  Run the simulation script:
    ```bash
    ./launch_simulator.sh
    ```
3.  Wait until Gazebo and RViz are fully loaded.
4.  Access the web dashboard at `http://localhost:8000`.

## Running on Hardware

For use in the CPS Lab:

1.  Place the TurtleBot on the docking station.
2.  Connect to the `cps-labor` Wi-Fi.
3.  Run the launch script with the robot's namespace and IP:
    ```bash
    ./launch.sh robot_1 192.168.0.226 turtlebot4
    ```

Now you can enter voice commands such as "Drive to the nearest chair" or "Find a person" via the dashboard.

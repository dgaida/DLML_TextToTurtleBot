# Troubleshooting

Here you will find solutions to common issues with TextToTurtleBot.

## Connection Issues

### Dashboard does not load
-   Ensure the web backend process is running (`python3 -m web.backend.main`).
-   Check if port 8000 is already in use.

### Robot does not respond to commands
-   Check ROS 2 connectivity using `ros2 topic list`.
-   Ensure the `TextToTurtlebotNode` is running.
-   Verify the namespace parameter.

## LLM Errors

### "API Key not found"
-   Check if the `core/.env` file exists and is correctly formatted.
-   Ensure you have selected the correct provider in `llm_config.json`.

### Model does not respond or is slow
-   Check your internet connection.
-   When using Ollama: Ensure the Ollama server is running locally and the model is loaded.

## Hardware Issues

### Lidar data missing
-   Check the physical connection of the Lidar sensor on the TurtleBot.
-   Restart the `lidar_processor` node.

# Installation

This guide describes the installation of TextToTurtleBot for various scenarios.

## Standard Installation (pip)

If you only want to install the Python dependencies:

```bash
pip install -r requirements.txt
```

## Developer Installation

For active participation in the project, we recommend using a virtual environment:

```bash
# Clone the repository
git clone https://github.com/user/TextToTurtleBot.git
cd TextToTurtleBot

# Create venv
python3 -m venv .venv
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt
pip install -e .  # If a setup.py/pyproject.toml is present
```

## ROS 2 Environment

TextToTurtleBot requires a functioning ROS 2 installation (Jazzy Elpis or Humble Hawksbill). Follow the official [ROS 2 documentation](https://docs.ros.org/) for your operating system.

### Simulation-Specific Dependencies

For the simulation, you also need:
-   Gazebo (GZ Sim)
-   TurtleBot 4 Simulator packages

```bash
sudo apt update
sudo apt install ros-$ROS_DISTRO-turtlebot4-simulator ros-$ROS_DISTRO-turtlebot4-desktop
```

## Documentation Tools

To build the documentation locally, install the additional requirements:

```bash
pip install mkdocs-material mkdocs-i18n mkdocstrings[python] mkdocs-mermaid2 mike interrogate git-cliff
```

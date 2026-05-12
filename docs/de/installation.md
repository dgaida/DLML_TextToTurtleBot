# Installation

Diese Anleitung beschreibt die Installation von TextToTurtleBot für verschiedene Szenarien.

## Standard-Installation (pip)

Wenn Sie nur die Python-Abhängigkeiten installieren möchten:

```bash
pip install -r requirements.txt
```

## Entwickler-Installation

Für die aktive Mitarbeit am Projekt empfehlen wir die Nutzung eines Virtual Environments:

```bash
# Repository klonen
git clone https://github.com/user/TextToTurtleBot.git
cd TextToTurtleBot

# Venv erstellen
python3 -m venv .venv
source .venv/bin/activate

# Abhängigkeiten installieren
pip install -r requirements.txt
pip install -e .  # Falls ein setup.py/pyproject.toml vorhanden ist
```

## ROS 2 Umgebung

TextToTurtleBot benötigt eine funktionierende ROS 2 Installation (Jazzy Elpis oder Humble Hawksbill). Folgen Sie der offiziellen [ROS 2 Dokumentation](https://docs.ros.org/) für Ihr Betriebssystem.

### Simulation-Spezifische Abhängigkeiten

Für die Simulation benötigen Sie zudem:
-   Gazebo (GZ Sim)
-   TurtleBot 4 Simulator Pakete

```bash
sudo apt update
sudo apt install ros-$ROS_DISTRO-turtlebot4-simulator ros-$ROS_DISTRO-turtlebot4-desktop
```

## Dokumentations-Tools

Um die Dokumentation lokal zu bauen, installieren Sie die zusätzlichen Requirements:

```bash
pip install mkdocs-material mkdocs-i18n mkdocstrings[python] mkdocs-mermaid2 mike interrogate git-cliff
```

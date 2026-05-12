# Erste Schritte

Diese Anleitung führt Sie durch den Prozess, TextToTurtleBot in einer Simulationsumgebung oder auf physischer Hardware in Betrieb zu nehmen.

## Voraussetzungen

Bevor Sie beginnen, stellen Sie sicher, dass folgende Komponenten installiert sind:

*   Python 3.10 oder neuer
*   ROS 2 (Jazzy oder Humble empfohlen)
*   Ein gültiger API-Key für einen unterstützten LLM-Provider (OpenAI, Google Gemini oder Ollama lokal)

## Installation

Folgen Sie den Anweisungen in der [Installationsanleitung](installation.md).

## Konfiguration

1.  Erstellen Sie eine `core/.env` Datei mit Ihrem API-Key:
    ```env
    OPENAI_API_KEY=sk-proj-...
    ```
2.  Passen Sie die `core/llm_config.json` an, um Ihren bevorzugten Provider zu wählen.

## Ausführung in der Simulation

Um das System schnell zu testen, wird die Nutzung der Gazebo-Simulation empfohlen:

1.  Aktivieren Sie Ihre ROS 2 Umgebung und das Python Virtual Environment.
2.  Starten Sie das Simulations-Skript:
    ```bash
    ./launch_simulator.sh
    ```
3.  Warten Sie, bis Gazebo und RViz vollständig geladen sind.
4.  Greifen Sie auf das Web-Dashboard unter `http://localhost:8000` zu.

## Ausführung auf Hardware

Für den Einsatz im CPS-Labor:

1.  Positionieren Sie den TurtleBot auf der Docking-Station.
2.  Verbinden Sie sich mit dem `cps-labor` WLAN.
3.  Starten Sie das Launch-Skript mit dem Namespace und der IP des Roboters:
    ```bash
    ./launch.sh robot_1 192.168.0.226 turtlebot4
    ```

Nun können Sie über das Dashboard Sprachbefehle wie "Fahre zum nächsten Stuhl" oder "Suche eine Person" eingeben.

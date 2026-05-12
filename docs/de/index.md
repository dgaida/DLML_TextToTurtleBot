# TextToTurtleBot

![Interrogate Coverage](../assets/interrogate.svg)

Willkommen zur Dokumentation von **TextToTurtleBot**. Dieses Projekt ermöglicht die Steuerung eines TurtleBot 4 mittels natürlicher Sprache durch die Integration modernster LLMs (Large Language Models) und ROS 2.

## Projektübersicht

TextToTurtleBot verbindet die Welt der Künstlichen Intelligenz mit der Robotik. Nutzer können dem Roboter Befehle in natürlicher Sprache geben, die dann in komplexe Verhaltensbäume (Behavior Trees) übersetzt und ausgeführt werden.

### Hauptmerkmale

*   **Sprachsteuerung**: Direkte Interaktion mit dem Roboter über Text oder Sprache.
*   **Intelligente Navigation**: Nutzung von Nav2 für präzise Bewegung und Hindernisumgehung.
*   **Objekterkennung**: Identifizierung und Lokalisierung von Objekten in der Umgebung.
*   **Web-Dashboard**: Intuitive Benutzeroberfläche zur Überwachung und Steuerung.
*   **Modulare Architektur**: Einfache Erweiterbarkeit durch Skills und LLM-Adapter.

## Quickstart

```bash
# Starten der Simulation
./launch_simulator.sh

# Öffnen des Dashboards
# http://localhost:8000
```

Weitere Informationen finden Sie im [Getting Started Guide](getting-started.md).

# Fehlerbehebung

Hier finden Sie Lösungen für häufig auftretende Probleme mit TextToTurtleBot.

## Verbindungsprobleme

### Dashboard lädt nicht
-   Stellen Sie sicher, dass der Web-Backend-Prozess läuft (`python3 -m web.backend.main`).
-   Prüfen Sie, ob Port 8000 bereits belegt ist.

### Roboter reagiert nicht auf Befehle
-   Prüfen Sie die ROS 2 Konnektivität mittels `ros2 topic list`.
-   Stellen Sie sicher, dass der `TextToTurtlebotNode` läuft.
-   Kontrollieren Sie den Namespace-Parameter.

## LLM-Fehler

### "API Key not found"
-   Prüfen Sie, ob die `core/.env` Datei existiert und korrekt formatiert ist.
-   Stellen Sie sicher, dass Sie den richtigen Provider in `llm_config.json` gewählt haben.

### Modell antwortet nicht oder langsam
-   Prüfen Sie Ihre Internetverbindung.
-   Bei Nutzung von Ollama: Stellen Sie sicher, dass der Ollama-Server lokal läuft und das Modell geladen ist.

## Hardware-Probleme

### Lidar-Daten fehlen
-   Prüfen Sie die physische Verbindung des Lidar-Sensors am TurtleBot.
-   Starten Sie den `lidar_processor` Knoten neu.

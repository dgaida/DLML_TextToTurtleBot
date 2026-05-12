# Bedienung und Workflows

In diesem Kapitel erfahren Sie, wie Sie TextToTurtleBot im Alltag einsetzen und welche Workflows unterstützt werden.

## Interaktion über das Dashboard

Das Web-Dashboard ist die primäre Schnittstelle für den Anwender.

1.  **Chat-Interface**: Geben Sie hier Ihre Befehle ein (z.B. "Fahre zur Küche").
2.  **Live-Karte**: Visualisiert die Position des Roboters und erkannte Objekte.
3.  **Kamera-Feed**: Zeigt das aktuelle Live-Bild der TurtleBot-Kamera inklusive YOLO-Detektionen.

## Beispielbefehle

Probieren Sie folgende Befehle aus:

-   *"Drehe dich um 180 Grad."*
-   *"Fahre 2 Meter vorwärts."*
-   *"Suche eine Person und fahre zu ihr."*
-   *"Was siehst du gerade?"* (Benötigt ein Vision-fähiges Modell wie GPT-4o).

## Verhalten bei Hindernissen

Der Roboter nutzt den Nav2 Stack zur Pfadplanung. Wenn ein Hindernis den Weg blockiert:
1.  Der Roboter versucht, das Hindernis zu umfahren.
2.  Falls kein Pfad gefunden wird, stoppt der Roboter und meldet den Status im Dashboard.
3.  Über den Verhaltensbaum (Behavior Tree) können Recovery-Verhalten ausgelöst werden.

# Architektur

TextToTurtleBot ist modular aufgebaut, um eine flexible Integration von KI-Modellen und Robotersteuerung zu ermöglichen.

## Systemübersicht

Die folgende Grafik zeigt die grobe Architektur des Systems:

```mermaid
graph TD
    User((Nutzer)) --> Dashboard[Web Dashboard]
    Dashboard --> Backend[Web Backend / FastAPI]
    Backend --> Blackboard[Shared Blackboard]
    Blackboard --> BT[Behavior Tree / TextToTurtlebotNode]
    BT --> LLM[LLM API / LangChain]
    LLM --> Provider{LLM Provider}
    Provider --> OpenAI[OpenAI]
    Provider --> Gemini[Google Gemini]
    Provider --> Ollama[Local Ollama]
    BT --> ROS2[ROS 2 Ecosystem]
    ROS2 --> Nav2[Nav2 Stack]
    ROS2 --> Perception[Perception Pipeline]
    Perception --> Camera[Kamera / YOLO]
    Perception --> Lidar[Lidar Processor]
```

## Datenfluss

Der Datenfluss bei einem Sprachbefehl sieht wie folgt aus:

```mermaid
sequenceDiagram
    participant U as Nutzer
    participant W as Web Backend
    participant B as Blackboard
    participant T as TextToTurtlebotNode
    participant L as LLM API

    U->>W: Sendet Sprachbefehl
    W->>B: Schreibt Befehl in Queue
    T->>B: Liest Befehl aus Queue
    T->>L: Anforderung zur Analyse
    L-->>T: Strukturierte Kommandos
    T->>T: Führt Behavior Tree aus
    T->>B: Aktualisiert Status
    B-->>W: Status-Update (Polling/Event)
    W-->>U: Zeigt Fortschritt im Dashboard
```

## Komponenten-Lebenszyklus

```mermaid
stateDiagram-v2
    [*] --> Initializing
    Initializing --> Idle: ROS 2 Nodes gestartet
    Idle --> Processing: Sprachbefehl empfangen
    Processing --> Executing: LLM Plan generiert
    Executing --> Processing: Nächster Schritt
    Executing --> Idle: Mission abgeschlossen
    Executing --> Error: Fehler aufgetreten
    Error --> Idle: Recovery/Reset
```

## Kernkomponenten

### core/
Enthält die Hauptlogik des Roboters, einschließlich der Verhaltensbäume, LLM-Integration und ROS 2 Schnittstellen.

### shared/
Beinhaltet gemeinsam genutzten Code wie das Blackboard und den Event-Bus, die die Kommunikation zwischen den Modulen erleichtern.

### web/
Beinhaltet das FastAPI-Backend und das Frontend für das Monitoring-Dashboard.

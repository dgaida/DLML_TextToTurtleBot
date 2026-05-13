# Architecture

TextToTurtleBot is modularly structured to allow flexible integration of AI models and robot control.

## System Overview

The following diagram shows the high-level architecture of the system:

```mermaid
graph TD
    User((User)) --> Dashboard[Web Dashboard]
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
    Perception --> Camera[Camera / YOLO]
    Perception --> Lidar[Lidar Processor]
```

## Data Flow

The data flow for a voice command is as follows:

```mermaid
sequenceDiagram
    participant U as User
    participant W as Web Backend
    participant B as Blackboard
    participant T as TextToTurtlebotNode
    participant L as LLM API

    U->>W: Sends voice command
    W->>B: Writes command to queue
    T->>B: Reads command from queue
    T->>L: Request for analysis
    L-->>T: Structured commands
    T->>T: Executes Behavior Tree
    T->>B: Updates status
    B-->>W: Status update (polling/event)
    W-->>U: Shows progress in dashboard
```

## Component Lifecycle

```mermaid
stateDiagram-v2
    [*] --> Initializing
    Initializing --> Idle: ROS 2 nodes started
    Idle --> Processing: Voice command received
    Processing --> Executing: LLM plan generated
    Executing --> Processing: Next step
    Executing --> Idle: Mission completed
    Executing --> Error: Error occurred
    Error --> Idle: Recovery/Reset
```

## Core Components

### core/
Contains the main logic of the robot, including behavior trees, LLM integration, and ROS 2 interfaces.

### shared/
Includes shared code such as the blackboard and event bus, which facilitate communication between modules.

### web/
Includes the FastAPI backend and the frontend for the monitoring dashboard.

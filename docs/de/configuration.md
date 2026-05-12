# Konfiguration

TextToTurtleBot bietet verschiedene Konfigurationsmöglichkeiten für LLMs und das Systemverhalten.

## LLM Konfiguration

Die zentrale Konfiguration für die LLM-Integration befindet sich in `core/llm_config.json`.

### Beispiel `llm_config.json`

```json
{
  "default_provider": "openai",
  "openai": {
    "model": "gpt-4o",
    "temperature": 0.2
  },
  "gemini": {
    "model": "gemini-1.5-pro"
  },
  "ollama": {
    "model": "llama3",
    "base_url": "http://localhost:11434"
  }
}
```

## Umgebungsvariablen

Sensible Daten wie API-Keys sollten in einer `.env` Datei im `core/` Verzeichnis abgelegt werden.

| Variable | Beschreibung |
|---|---|
| `OPENAI_API_KEY` | API-Key für OpenAI Dienste |
| `GOOGLE_API_KEY` | API-Key für Google Gemini Dienste |
| `LANGCHAIN_TRACING_V2` | Setzen auf `true` für LangSmith Tracing |
| `LANGCHAIN_API_KEY` | API-Key für LangSmith |

## ROS 2 Parameter

Viele Knoten unterstützen Standard ROS 2 Parameter, die beim Start übergeben werden können:

-   `--namespace`: Bestimmt den Namespace des Roboters (Standard: `/robot_1`).
-   `--use_turtlebot_sim`: Flag zur Unterscheidung zwischen Hardware und Simulation.

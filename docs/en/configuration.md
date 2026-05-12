# Configuration

TextToTurtleBot offers various configuration options for LLMs and system behavior.

## LLM Configuration

The central configuration for LLM integration is located in `core/llm_config.json`.

### Example `llm_config.json`

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

## Environment Variables

Sensitive data such as API keys should be stored in a `.env` file in the `core/` directory.

| Variable | Description |
|---|---|
| `OPENAI_API_KEY` | API key for OpenAI services |
| `GOOGLE_API_KEY` | API key for Google Gemini services |
| `LANGCHAIN_TRACING_V2` | Set to `true` for LangSmith tracing |
| `LANGCHAIN_API_KEY` | API key for LangSmith |

## ROS 2 Parameters

Many nodes support standard ROS 2 parameters that can be passed at startup:

-   `--namespace`: Determines the robot's namespace (Default: `/robot_1`).
-   `--use_turtlebot_sim`: Flag to distinguish between hardware and simulation.

# Instructions for AI Agents

## Core Directives
- **Cleanliness**: You MUST delete all temporary files (e.g., coverage reports, logs, temporary test artifacts) before creating a pull request or submitting changes.
- **Documentation**: All new classes and methods must include Google-style docstrings.
- **Language**: German is the authoritative language for documentation. English documentation must be a faithful translation.
- **Testing**: Strive for high test coverage and always verify changes with existing and new tests.

## Development Workflow
- Use `pytest` for testing.
- Follow PEP 8 and use `ruff` for linting.
- Use `mypy` for type checking where applicable.

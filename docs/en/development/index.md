# Developer Guide

Welcome to the TextToTurtleBot Developer Guide. This section contains information for anyone wishing to extend or improve the system.

## Project Structure

-   `core/`: The heart of the system (ROS 2 nodes, BT, LLM).
-   `shared/`: Shared data structures and utilities.
-   `web/`: Web interface and backend.
-   `docs/`: This documentation.

## Local Development Environment

1.  Follow the [Installation Instructions](installation.md) for developers.
2.  Install additional developer tools:
    ```bash
    pip install pytest pytest-cov black isort mypy interrogate
    ```

## Code Style and Guidelines

We place great importance on clean, well-documented code.

-   **Docstrings**: We use the **Google style** for all functions and classes. See the [Docstring Guide](docstring-guide.md).
-   **Type Annotations**: Use Python type hints for all function parameters and return values.
-   **Linting**: Run `black` and `isort` before every commit.

## Running Tests

We use `pytest` for our unit tests:

```bash
pytest tests/
```

## Building Documentation Locally

To see changes to the documentation immediately:

```bash
mkdocs serve
```

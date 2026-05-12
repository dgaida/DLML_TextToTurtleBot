# Entwickler-Leitfaden

Willkommen zum Entwickler-Leitfaden von TextToTurtleBot. Dieser Bereich enthält Informationen für alle, die das System erweitern oder verbessern möchten.

## Projektstruktur

-   `core/`: Das Herzstück des Systems (ROS 2 Knoten, BT, LLM).
-   `shared/`: Gemeinsame Datenstrukturen und Utilities.
-   `web/`: Web-Interface und Backend.
-   `docs/`: Diese Dokumentation.

## Lokale Entwicklungsumgebung

1.  Folgen Sie den [Installationsanweisungen](installation.md) für Entwickler.
2.  Installieren Sie zusätzliche Entwickler-Tools:
    ```bash
    pip install pytest pytest-cov black isort mypy interrogate
    ```

## Code-Stil und Richtlinien

Wir legen großen Wert auf sauberen, gut dokumentierten Code.

-   **Docstrings**: Wir verwenden den **Google-Style** für alle Funktionen und Klassen. Siehe [Docstring-Guide](docstring-guide.md).
-   **Typ-Annotationen**: Nutzen Sie Python Type Hints für alle Funktionsparameter und Rückgabewerte.
-   **Linting**: Vor jedem Commit sollten `black` und `isort` ausgeführt werden.

## Tests ausführen

Wir verwenden `pytest` für unsere Unit-Tests:

```bash
pytest tests/
```

## Dokumentation lokal bauen

Um Änderungen an der Dokumentation sofort zu sehen:

```bash
mkdocs serve
```

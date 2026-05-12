# Docstring Compliance Scan

Die folgenden Symbole im Repository entsprechen aktuell nicht dem Google-Style Standard oder fehlen vollständig.

## Core Module

### `core/commands/user_command.py`
-   **Symbol**: `UserCommand.navigate`
-   **Status**: Fehlende Argumenten-Beschreibung.
-   **Replacement**:
    ```python
    def navigate(cls, x: float, y: float, theta: Optional[float] = None):
        """Erstellt einen Navigationsbefehl zu einer bestimmten Koordinate.

        Args:
            x (float): Die X-Koordinate in Metern.
            y (float): Die Y-Koordinate in Metern.
            theta (Optional[float]): Der Zielwinkel (Yaw) in Radiant. Defaults to None.

        Returns:
            UserCommand: Das konfigurierte Kommando-Objekt.
        """
    ```

### `core/natural_language_processing/llm_api.py`
-   **Symbol**: `LLMAPI.run`
-   **Status**: Unvollständige Beschreibung der Rückgabewerte.
-   **Replacement**:
    ```python
    def run(self, user_input: str, history: Optional[HistoryInput] = None) -> dict:
        """Verarbeitet eine Benutzereingabe über das LLM.

        Args:
            user_input (str): Der Text der Benutzereingabe.
            history (Optional[HistoryInput]): Der bisherige Chat-Verlauf. Defaults to None.

        Returns:
            dict: Das Ergebnis der LLM-Verarbeitung, inklusive generierter Kommandos.
        """
    ```

## Shared Module

### `shared/blackboard/blackboard.py`
-   **Symbol**: `Blackboard.append_chat_message`
-   **Status**: Fehlende Beschreibung der Parameter.
-   **Replacement**:
    ```python
    def append_chat_message(self, role: str, text: str, metadata: Optional[Dict[str, Any]] = None) -> None:
        """Fügt eine neue Nachricht zum Chat-Log im Blackboard hinzu.

        Args:
            role (str): Die Rolle des Absenders (z.B. "user", "assistant").
            text (str): Der Inhalt der Nachricht.
            metadata (Optional[Dict[str, Any]]): Zusätzliche Metadaten zur Nachricht. Defaults to None.
        """
    ```

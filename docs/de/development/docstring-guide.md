# Docstring Leitfaden

Um eine qualitativ hochwertige API-Dokumentation zu gewährleisten, nutzen wir den **Google Python Style Guide** für alle Docstrings.

## Grundstruktur

Jeder Docstring sollte eine kurze Zusammenfassung, eine detaillierte Beschreibung (falls nötig), Argumente, Rückgabewerte und Ausnahmen enthalten.

### Beispiel für eine Funktion

```python
def berechne_distanz(punkt_a: Tuple[float, float], punkt_b: Tuple[float, float]) -> float:
    """Berechnet die euklidische Distanz zwischen zwei Punkten.

    Diese Funktion nutzt den Satz des Pythagoras zur Berechnung der
    Distanz in einem 2D-Koordinatensystem.

    Args:
        punkt_a (Tuple[float, float]): Die (x, y) Koordinaten des ersten Punktes.
        punkt_b (Tuple[float, float]): Die (x, y) Koordinaten des zweiten Punktes.

    Returns:
        float: Die berechnete Distanz als Fließkommazahl.

    Example:
        >>> berechne_distanz((0, 0), (3, 4))
        5.0
    """
    return ((punkt_a[0] - punkt_b[0])**2 + (punkt_a[1] - punkt_b[1])**2)**0.5
```

### Beispiel für eine Klasse

```python
class RoboterSteuerung:
    """Steuert die grundlegenden Bewegungen des TurtleBot.

    Attributes:
        namespace (str): Der ROS-Namespace des Roboters.
        is_sim (bool): Flag, ob der Roboter in der Simulation läuft.
    """

    def __init__(self, namespace: str, is_sim: bool = False):
        """Initialisiert die RoboterSteuerung.

        Args:
            namespace (str): Der Namespace.
            is_sim (bool): Ob Simulation genutzt wird. Defaults to False.
        """
        self.namespace = namespace
        self.is_sim = is_sim
```

## Compliance Check

Wir nutzen **interrogate**, um die Abdeckung von Docstrings zu prüfen. Ein CI-Schritt stellt sicher, dass mindestens 95% des Codes dokumentiert sind.

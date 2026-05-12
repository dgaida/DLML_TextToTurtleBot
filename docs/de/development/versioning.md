# Versionierung mit Mike

Die Dokumentation von TextToTurtleBot unterstützt Versionierung, um Informationen für verschiedene Software-Releases bereitstellen zu können. Hierfür verwenden wir **mike**.

## Deployment neuer Versionen

Um eine neue Version der Dokumentation zu veröffentlichen, nutzen Sie den folgenden Befehl:

```bash
mike deploy --push --update-aliases 1.0 latest
```

Dies baut die Dokumentation und pusht sie in den `gh-pages` Branch. Das Alias `latest` zeigt dabei immer auf die aktuellste stabile Version.

## Standard-Version festlegen

Falls Sie die Standard-Version ändern möchten, die beim Aufruf der Basis-URL angezeigt wird:

```bash
mike set-default --push latest
```

## Lokale Vorschau von Versionen

Sie können eine lokale Vorschau des versionierten Portals starten:

```bash
mike serve
```

Besuchen Sie anschließend `http://localhost:8000`, um den Versions-Selector in Aktion zu sehen.

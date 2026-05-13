# Dokumentations-Metriken

Dieses Dashboard visualisiert die Qualität und Abdeckung unserer Dokumentation.

| Metrik | Quelle | Update-Frequenz |
|---|---|---|
| API-Doku Abdeckung | `interrogate` Badge | Jeder CI-Lauf |
| Defekte Links | `lychee` | Jeder CI-Lauf |
| Markdown Lint Fehler | `markdownlint` | Jeder CI-Lauf |
| Build Warnungen | MkDocs stderr | Jeder CI-Lauf |
| Changelog Frische | Letzter Commit `CHANGELOG.md` | Jeder CI-Lauf |

## Aktuelle Status-Werte

<div id="metrics-dashboard">
  <p>Lade Metriken...</p>
</div>

<script src="../assets/metrics-renderer.js"></script>

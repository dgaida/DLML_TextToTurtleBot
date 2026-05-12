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

<script>
fetch('../assets/metrics.json')
  .then(response => response.json())
  .then(data => {
    const dashboard = document.getElementById('metrics-dashboard');
    dashboard.innerHTML = `
      <ul>
        <li><strong>API Coverage:</strong> ${data.api_coverage}%</li>
        <li><strong>Broken Links:</strong> ${data.broken_links}</li>
        <li><strong>Lint Errors:</strong> ${data.lint_errors}</li>
        <li><strong>Last Updated:</strong> ${data.last_updated}</li>
      </ul>
    `;
  })
  .catch(error => {
    document.getElementById('metrics-dashboard').innerHTML = '<p>Metriken zurzeit nicht verfügbar.</p>';
  });
</script>

fetch('../assets/metrics.json')
  .then(response => response.json())
  .then(data => {
    const dashboard = document.getElementById('metrics-dashboard');
    dashboard.innerHTML = `
      <div class="metrics-grid" style="display: flex; gap: 20px; flex-wrap: wrap;">
        <div class="metric-card" style="border: 1px solid #ccc; padding: 15px; border-radius: 8px; min-width: 150px; text-align: center;">
            <h3>API Abdeckung</h3>
            <span class="value" style="font-size: 2em; font-weight: bold; color: #009688;">${data.api_coverage}%</span>
        </div>
        <div class="metric-card" style="border: 1px solid #ccc; padding: 15px; border-radius: 8px; min-width: 150px; text-align: center;">
            <h3>Defekte Links</h3>
            <span class="value" style="font-size: 2em; font-weight: bold; color: #f44336;">${data.broken_links}</span>
        </div>
        <div class="metric-card" style="border: 1px solid #ccc; padding: 15px; border-radius: 8px; min-width: 150px; text-align: center;">
            <h3>Lint Fehler</h3>
            <span class="value" style="font-size: 2em; font-weight: bold; color: #ff9800;">${data.lint_errors}</span>
        </div>
      </div>
      <p style="margin-top: 20px;">Zuletzt aktualisiert: <code>${data.last_updated}</code></p>
    `;
  })
  .catch(error => {
    document.getElementById('metrics-dashboard').innerHTML = '<p>Metriken zurzeit nicht verfügbar.</p>';
  });

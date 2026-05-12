# Documentation Metrics

This dashboard visualizes the quality and coverage of our documentation.

| Metric | Source | Update Frequency |
|---|---|---|
| API Doc Coverage | `interrogate` Badge | Every CI run |
| Broken Links | `lychee` | Every CI run |
| Markdown Lint Errors | `markdownlint` | Every CI run |
| Build Warnings | MkDocs stderr | Every CI run |
| Changelog Freshness | Last commit to `CHANGELOG.md` | Every CI run |

## Current Status Values

<div id="metrics-dashboard">
  <p>Loading metrics...</p>
</div>

<script>
fetch('assets/metrics.json')
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
    document.getElementById('metrics-dashboard').innerHTML = '<p>Metrics currently unavailable.</p>';
  });
</script>

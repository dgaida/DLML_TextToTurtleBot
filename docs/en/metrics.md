# Documentation Metrics

This dashboard visualizes the quality and coverage of our documentation.

| Metric | Source | Update Frequency |
|---|---|---|
| API Doc Coverage | `interrogate` badge | Every CI run |
| Broken Links | `lychee` | Every CI run |
| Markdown Lint Errors | `markdownlint` | Every CI run |
| Build Warnings | MkDocs stderr | Every CI run |
| Changelog Freshness | Last commit to `CHANGELOG.md` | Every CI run |

## Current Status Values

<div id="metrics-dashboard">
  <p>Loading metrics...</p>
</div>

<script src="../assets/metrics-renderer.js"></script>

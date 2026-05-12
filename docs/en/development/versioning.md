# Versioning with Mike

TextToTurtleBot documentation supports versioning to provide information for different software releases. We use **mike** for this purpose.

## Deploying New Versions

To publish a new version of the documentation, use the following command:

```bash
mike deploy --push --update-aliases 1.0 latest
```

This builds the documentation and pushes it to the `gh-pages` branch. The `latest` alias always points to the most recent stable version.

## Setting the Default Version

If you want to change the default version displayed when the base URL is accessed:

```bash
mike set-default --push latest
```

## Local Preview of Versions

You can start a local preview of the versioned portal:

```bash
mike serve
```

Then visit `http://localhost:8000` to see the version selector in action.

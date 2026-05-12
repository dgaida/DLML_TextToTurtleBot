# Changelog Workflow

We use **git-cliff** to automatically generate meaningful changelogs from our commit messages.

## Conventional Commits

For the changelog to be generated correctly, all commits must follow the [Conventional Commits](https://www.conventionalcommits.org/) standard:

-   `feat`: A new feature for the user.
-   `fix`: A bugfix for the user.
-   `docs`: Documentation changes.
-   `style`: Changes to formatting, missing semicolons, etc. (no code changes).
-   `refactor`: Refactoring of productive code.
-   `test`: Adding or correcting tests.
-   `chore`: Maintenance tasks on the build system or helper programs.

### Example

```bash
feat(navigation): Added support for dynamic obstacle avoidance
```

## Automation

With every push of a tag (e.g., `v1.0.0`), a GitHub Action workflow is executed that:
1.  Runs `git-cliff`.
2.  Updates the `CHANGELOG.md` in the root directory.
3.  Creates a GitHub Release with the corresponding release notes.

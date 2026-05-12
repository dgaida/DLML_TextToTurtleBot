# Changelog Workflow

Wir nutzen **git-cliff**, um automatisch aussagekräftige Changelogs aus unseren Commit-Nachrichten zu generieren.

## Konventionelle Commits

Damit der Changelog korrekt generiert werden kann, müssen alle Commits dem Standard der [Conventional Commits](https://www.conventionalcommits.org/) folgen:

-   `feat`: Ein neues Feature für den Anwender.
-   `fix`: Ein Bugfix für den Anwender.
-   `docs`: Dokumentationsänderungen.
-   `style`: Änderungen am Format, fehlende Semikolons etc. (keine Codeänderung).
-   `refactor`: Refactoring des produktiven Codes.
-   `test`: Hinzufügen oder Korrigieren von Tests.
-   `chore`: Wartungsaufgaben am Build-System oder Hilfsprogrammen.

### Beispiel

```bash
feat(navigation): Unterstützung für dynamische Hindernisumfahrung hinzugefügt
```

## Automatisierung

Bei jedem Push eines Tags (z.B. `v1.0.0`) wird ein GitHub Action Workflow ausgeführt, der:
1.  `git-cliff` ausführt.
2.  Die `CHANGELOG.md` im Root-Verzeichnis aktualisiert.
3.  Einen GitHub Release mit den entsprechenden Release-Notes erstellt.

# Solus Prerelease

Solus is a tabletop RPG project in active development. This repository now centers on one active system-book manuscript built for later conversion into Homebrewery.

The manuscript holds the current rules draft in reader-facing order. Older epic files, rough notes, and playtest material stay in the archive so the source history remains intact.

## Start Here

- [System book manuscript](system-book/solus-system-book.md)
- [Project status](docs/project-status.md)
- [Archived source drafts](archive/epics-and-stories)

## Repository Structure

- [system-book](system-book) holds the active manuscript.
- [docs](docs) holds status, specs, and planning material.
- [archive](archive) holds the older epic drafts, rough notes, and playtest files.
- [.obsidian](.obsidian) holds local vault settings and plugins.

## Current State

The manuscript already carries the stable rules material for Solus, including the core mechanics, character framework, combat structure, NPC ranks, and advancement model. Unfinished systems stay marked with short TODOs so they remain visible without pretending to be done.

Treat [The System Book Document](system-book/solus-system-book.md) as the current source of truth for all rules. Use the archive for source tracing, extraction, and comparison, not for new book prose.

## Obsidian Vault Package

This repository includes a GitHub Actions workflow that builds an Obsidian-ready vault package from the manuscript and archive.

The published package includes:

- the full manuscript
- generated chapter files split from the manuscript
- archive material for source browsing
- small navigation notes for Obsidian
- a rolling prerelease download on GitHub
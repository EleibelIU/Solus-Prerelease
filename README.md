# Solus Prerelease

Solus is a tabletop RPG in active development. This repository holds the rules manuscript, archive material, and build tooling for the game.

## Source of Truth

The active manuscript is **[Homebrewery/Solus-System-Book-Homebrew.md](Homebrewery/Solus-System-Book-Homebrew.md)**. All rules editing happens in this file. It renders directly in [Homebrewery V3](https://homebrewery.naturalcrit.com/) using the 5ePHB theme with Frostmaiden CSS.

The older `system-book/solus-system-book.md` is a prior plaintext draft. It is not maintained. Use the Homebrewery file for all current work.

## Repository Structure

| Folder | Purpose |
|:---|:---|
| [Homebrewery/](Homebrewery) | Active manuscript, theme CSS, cover art, and HTML export. |
| [archive/](archive) | Older epic drafts, rough notes, and playtest files. Source tracing only. |
| [system-book/](system-book) | Legacy plaintext manuscript. Superseded by Homebrewery file. |
| [docs/](docs) | Project status, specs, and planning material. |
| [scripts/](scripts) | Build scripts (Obsidian vault pipeline, tests). |
| [.github/workflows/](.github/workflows) | GitHub Actions for the Obsidian vault build. |

## Manuscript Chapters

1. Welcome to Solus
2. Core Mechanics
3. Character Creation
4. Attributes and Skills
5. Equipment, Armor, and Weapons
6. Magic and Spellcasting
7. Core Gameplay Loop
8. Combat
9. Conditions, Injuries, and Death
10. NPCs, Enemies, and Encounters
11. Advancement, Mastery, and Between-Session Play
12. Running the Game
13. Reference and Playtest Tools (includes glossary)

Unfinished sections are marked with `TODO:` comments addressed from Liz (editor) to Jacob (system designer).

## Local Development Setup

The build scripts require only Python 3.12+ (standard library only — no third-party packages).

**Windows (PowerShell)**

```powershell
# Clone the repo, then from the project root:
.\init.ps1
# Activate the environment for your shell session:
.\.venv\Scripts\Activate.ps1
# Run the build script:
python .\scripts\build_obsidian_vault.py
# Run the tests:
python .\scripts\test_build_obsidian_vault.py
```

**macOS / Linux**

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python scripts/build_obsidian_vault.py
python scripts/test_build_obsidian_vault.py
```

## Obsidian Vault Package

A GitHub Actions workflow builds an Obsidian-ready vault package from the manuscript and archive on each push to `main`.

The published package includes:

- the full manuscript
- generated chapter files split from the manuscript
- archive material for source browsing
- navigation notes for Obsidian
- a rolling prerelease download on GitHub
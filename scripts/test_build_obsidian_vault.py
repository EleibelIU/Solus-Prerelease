from pathlib import Path
import shutil
import subprocess
import sys


repo_root = Path(__file__).resolve().parent.parent
output_root = repo_root / "tmp-test-vault"
zip_path = repo_root / "tmp-test-vault.zip"

if output_root.exists():
    shutil.rmtree(output_root)

if zip_path.exists():
    zip_path.unlink()

subprocess.run(
    [
        sys.executable,
        str(Path(__file__).resolve().parent / "build_obsidian_vault.py"),
        "--output-root",
        str(output_root),
        "--zip-path",
        str(zip_path),
    ],
    check=True,
)

expected_paths = [
    output_root / "Home.md",
    output_root / "System Book.md",
    output_root / "Archive Index.md",
    output_root / "system-book" / "solus-system-book.md",
    output_root / "system-book" / "chapters" / "01 Introduction and Design Goals.md",
    output_root / "system-book" / "chapters" / "02 Core Mechanics.md",
    output_root / "system-book" / "chapters" / "14 Reference and Playtest Tools.md",
    output_root / "archive" / "epics-and-stories",
    output_root / "archive" / "rough-notes",
    output_root / "archive" / "playtest-materials",
]

for path in expected_paths:
    if not path.exists():
        raise SystemExit(f"Missing expected build output: {path}")

home_text = (output_root / "Home.md").read_text(encoding="utf-8")
if "[[System Book]]" not in home_text:
    raise SystemExit("Home.md does not contain the System Book wiki link.")

toc_text = (output_root / "System Book.md").read_text(encoding="utf-8")
if "[[system-book/chapters/09 Combat]]" not in toc_text:
    raise SystemExit("System Book.md does not contain the Combat chapter link.")

chapter_text = (output_root / "system-book" / "chapters" / "02 Core Mechanics.md").read_text(encoding="utf-8")
if not chapter_text.startswith("## Core Mechanics"):
    raise SystemExit("Core Mechanics chapter file does not start with the expected heading.")

if not zip_path.exists():
    raise SystemExit("Vault zip was not created.")

print("Vault build test passed.")
from __future__ import annotations

import argparse
import re
import shutil
import zipfile
from pathlib import Path


ARCHIVE_FOLDERS = (
    "epics-and-stories",
    "rough-notes",
    "playtest-materials",
)


def build_parser() -> argparse.ArgumentParser:
    repo_root = Path(__file__).resolve().parent.parent
    parser = argparse.ArgumentParser()
    parser.add_argument("--output-root", default=str(repo_root / "dist-vault"))
    parser.add_argument("--zip-path", default=str(repo_root / "dist-vault.zip"))
    return parser


def ensure_inputs(repo_root: Path) -> tuple[Path, Path]:
    manuscript_path = repo_root / "system-book" / "solus-system-book.md"
    archive_root = repo_root / "archive"

    if not manuscript_path.exists():
        raise SystemExit(f"Missing manuscript: {manuscript_path}")

    for folder_name in ARCHIVE_FOLDERS:
        folder_path = archive_root / folder_name
        if not folder_path.exists():
            raise SystemExit(f"Missing archive folder: {folder_path}")

    return manuscript_path, archive_root


def sanitize_title(title: str) -> str:
    return re.sub(r'[\\/:*?"<>|]', "", title).strip()


def split_chapters(manuscript_text: str) -> list[tuple[str, str]]:
    matches = re.findall(r"(?ms)^##\s+(.+?)\n(.*?)(?=^##\s+|\Z)", manuscript_text)
    if not matches:
        raise SystemExit("No chapter headings found in manuscript.")
    return [(title.strip(), body.rstrip()) for title, body in matches]


def write_text(path: Path, content: str) -> None:
    path.write_text(content, encoding="utf-8")


def create_navigation_notes(output_root: Path, chapter_titles: list[str]) -> None:
    home_note = "# Solus Vault\n\n- [[System Book]]\n- [[Archive Index]]\n"
    chapter_links = "\n".join(
        f"- [[system-book/chapters/{index:02d} {sanitize_title(title)}]]"
        for index, title in enumerate(chapter_titles, start=1)
    )
    system_book_note = (
        "# System Book\n\n"
        "- [[system-book/solus-system-book]]\n"
        f"{chapter_links}\n"
    )
    archive_index_note = (
        "# Archive Index\n\n"
        "- [[archive/epics-and-stories]]\n"
        "- [[archive/rough-notes]]\n"
        "- [[archive/playtest-materials]]\n"
    )

    write_text(output_root / "Home.md", home_note)
    write_text(output_root / "System Book.md", system_book_note)
    write_text(output_root / "Archive Index.md", archive_index_note)


def create_zip(output_root: Path, zip_path: Path) -> None:
    with zipfile.ZipFile(zip_path, "w", compression=zipfile.ZIP_DEFLATED) as archive:
        for path in sorted(output_root.rglob("*")):
            archive.write(path, path.relative_to(output_root))


def main() -> None:
    args = build_parser().parse_args()
    repo_root = Path(__file__).resolve().parent.parent
    output_root = Path(args.output_root).resolve()
    zip_path = Path(args.zip_path).resolve()
    manuscript_path, archive_root = ensure_inputs(repo_root)

    if output_root.exists():
        shutil.rmtree(output_root)

    if zip_path.exists():
        zip_path.unlink()

    chapters_root = output_root / "system-book" / "chapters"
    (output_root / "system-book").mkdir(parents=True, exist_ok=True)
    chapters_root.mkdir(parents=True, exist_ok=True)
    (output_root / "archive").mkdir(parents=True, exist_ok=True)

    shutil.copy2(manuscript_path, output_root / "system-book" / "solus-system-book.md")

    for folder_name in ARCHIVE_FOLDERS:
        shutil.copytree(archive_root / folder_name, output_root / "archive" / folder_name)

    manuscript_text = manuscript_path.read_text(encoding="utf-8")
    chapters = split_chapters(manuscript_text)
    chapter_titles = [title for title, _ in chapters]

    for index, (title, body) in enumerate(chapters, start=1):
        chapter_path = chapters_root / f"{index:02d} {sanitize_title(title)}.md"
        chapter_text = f"## {title}\n\n{body}\n"
        write_text(chapter_path, chapter_text)

    create_navigation_notes(output_root, chapter_titles)
    create_zip(output_root, zip_path)

    print(f"Vault created at {output_root}")
    print(f"Zip created at {zip_path}")


if __name__ == "__main__":
    main()
"""Build the EPUB for "The Code Kitchen" from the Markdown manuscript.

Run from the project root:

    python build/build_epub.py

Needs Pandoc on the PATH. If build/epubcheck/epubcheck.jar exists and Java is
installed, the finished EPUB is validated with EPUBCheck as well.
"""

import re
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MANUSCRIPT = ROOT / "manuscript"
BUILD = ROOT / "build"
TEMP = BUILD / "tmp"
OUTPUT = ROOT / "dist" / "The-Code-Kitchen.epub"
EPUBCHECK = BUILD / "epubcheck" / "epubcheck.jar"

# The EPUB reader builds its own clickable table of contents, so the
# hand-written one would only show up as a second, non-clickable copy.
SKIP = {"04-table-of-contents.md"}


def chapter_files() -> list[Path]:
    files = []
    for part in sorted(p for p in MANUSCRIPT.iterdir() if p.is_dir()):
        for md in sorted(part.glob("*.md")):
            if md.name not in SKIP:
                files.append(md)
    return files


def title_page(text: str) -> str:
    """Rebuild the title page with one styled block per line.

    Reading apps apply their own alignment to headings, so the subtitle is
    turned into a plain styled block instead of a small heading. The title
    heading stays (it starts the page) but is kept out of the contents.
    """
    title = re.search(r"^# (.+)$", text, re.M).group(1).strip()
    subtitle = re.search(r"^### (.+)$", text, re.M).group(1).strip()
    author = re.search(r"^\*\*(.+)\*\*$", text, re.M).group(1).strip()
    dedication = re.search(r"^\*([^*].+)\*$", text, re.M).group(1).strip()

    return (
        f"# {title} {{.unlisted .front-page}}\n\n"
        f"::: tp-subtitle\n{subtitle}\n:::\n\n"
        f"::: tp-author\n{author}\n:::\n\n"
        f"::: tp-rule\n:::\n\n"
        f"::: tp-dedication\n{dedication}\n:::\n"
    )


def prepare(md: Path) -> Path:
    """Copy a file into build/tmp, adjusting front pages for the EPUB."""
    text = md.read_text(encoding="utf-8")

    if md.name == "00-title-page.md":
        text = title_page(text)
    elif md.name == "01-copyright.md":
        # The copyright page has no heading in the manuscript. Without one,
        # Pandoc would glue it onto the end of the title page.
        text = "# Copyright {.unlisted .copyright-page}\n\n" + text
    elif md.name == "03-thank-you.md":
        # A short page, so it gets larger, centered text.
        text = re.sub(r"^# (.+)$", r"# \1 {.closing-page}", text, count=1, flags=re.M)

    # Keep a signature line together with the paragraph before it, so the
    # author's name never lands alone at the top of the next page.
    text = re.sub(
        r"\n\n([^\n]+)\n\n(\*\*Yora Ji-hun\*\*)\s*$",
        r"\n\n::: signoff\n\1\n\n\2\n:::\n",
        text,
    )

    out = TEMP / f"{md.parent.name}__{md.name}"
    out.write_text(text, encoding="utf-8")
    return out


def main() -> int:
    if shutil.which("pandoc") is None:
        print("Pandoc is not installed. Install it with: winget install --id JohnMacFarlane.Pandoc")
        return 1

    if TEMP.exists():
        shutil.rmtree(TEMP)
    TEMP.mkdir(parents=True)
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)

    inputs = [prepare(md) for md in chapter_files()]

    command = [
        "pandoc",
        "--from=markdown",
        "--to=epub3",
        f"--metadata-file={BUILD / 'metadata.yaml'}",
        "--toc",
        "--toc-depth=1",
        "--split-level=1",
        f"--resource-path={ROOT}",
        f"--output={OUTPUT}",
        *map(str, inputs),
    ]
    print(f"Building {OUTPUT.relative_to(ROOT)} from {len(inputs)} files...")
    result = subprocess.run(command, cwd=ROOT)
    shutil.rmtree(TEMP)
    if result.returncode != 0:
        return result.returncode
    print("EPUB built.")

    if EPUBCHECK.exists() and shutil.which("java"):
        print("Running EPUBCheck...")
        return subprocess.run(["java", "-jar", str(EPUBCHECK), str(OUTPUT)]).returncode

    print("EPUBCheck not found, so the EPUB was not validated.")
    return 0


if __name__ == "__main__":
    sys.exit(main())

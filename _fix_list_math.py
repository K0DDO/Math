"""Fix GitHub math: $$ inside lists does not render. Convert to inline $."""
from __future__ import annotations

import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parent / "02_specrazdely"

# Match a list item line (ordered or unordered) that contains $$...$$
LIST_START = re.compile(r"^(\s*)([-*+]|\d+\.)\s+")


def process_file(text: str) -> str:
    lines = text.splitlines(keepends=True)
    out: list[str] = []
    i = 0
    while i < len(lines):
        line = lines[i]
        # Case A: list marker line that itself contains $$...$$
        if LIST_START.match(line) and "$$" in line:
            # Convert all $$...$$ on this line to $...$
            line = re.sub(r"\$\$(.*?)\$\$", r"$\1$", line)
            out.append(line)
            i += 1
            continue

        # Case B: list item text, then next lines are $$ ... $$ belonging to the item
        m = LIST_START.match(line)
        if m and i + 1 < len(lines) and lines[i + 1].strip().startswith("$$"):
            # Collect display block
            out.append(line.rstrip() + " ")
            i += 1
            block = []
            while i < len(lines):
                block.append(lines[i].rstrip("\n"))
                if lines[i].strip().endswith("$$") and (
                    lines[i].strip() != "$$" or len(block) > 1
                ):
                    # closing — if line is just $$, need content until next $$
                    if lines[i].strip() == "$$" and len(block) == 1:
                        i += 1
                        continue
                    i += 1
                    break
                i += 1
            # Join block into one inline math
            content = " ".join(b.strip() for b in block)
            # Strip outer $$
            content = content.strip()
            if content.startswith("$$"):
                content = content[2:]
            if content.endswith("$$"):
                content = content[:-2]
            content = content.strip()
            # Append to previous list line as inline math
            out[-1] = out[-1].rstrip() + " $" + content + "$\n"
            continue

        out.append(line)
        i += 1

    text = "".join(out)

    # Also: any remaining $$ immediately after ":$" patterns in list context already handled.
    # Convert lone $$ blocks that sit between list items awkwardly — skip.

    # Ensure \, thin spaces: replace problematic \, with \; or nothing if broken
    # Actually double-backslash thin space for GitHub? Try \: 
    # Keep \, for now.

    return text


def main() -> None:
    changed = 0
    for path in sorted(ROOT.rglob("*.md")):
        old = path.read_text(encoding="utf-8")
        new = process_file(old)
        if new != old:
            path.write_text(new, encoding="utf-8", newline="\n")
            changed += 1
            print(f"UPDATED {path.relative_to(ROOT)}")
    print(f"total {changed}")

    p = ROOT / "voprosy" / "01_linejnyj_operator.md"
    for line in p.read_text(encoding="utf-8").splitlines():
        if "Поворот" in line or ("Проверка" in line and "pmatrix" in line):
            print(repr(line[:200]))


if __name__ == "__main__":
    main()

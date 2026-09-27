#!/usr/bin/env python3
"""Fail if any post contains something that looks like an access key.

Runs in the build check for every pull request and every push to main.
Standard library only.
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

PATTERNS = {
    "Mapbox token": r"\b(?:sk|pk)\.eyJ[A-Za-z0-9._-]{20,}",
    "AWS access key": r"\bAKIA[0-9A-Z]{16}\b",
    "GitHub token": r"\bgh[pousr]_[A-Za-z0-9]{36,}\b",
    "Google API key": r"\bAIza[0-9A-Za-z_-]{35}\b",
    "Slack token": r"\bxox[baprs]-[A-Za-z0-9-]{10,}",
    "OpenAI-style key": r"\bsk-[A-Za-z0-9_-]{20,}",
    "Private key": r"-----BEGIN [A-Z ]*PRIVATE KEY-----",
}


def main():
    found = []
    for path in sorted((ROOT / "post").rglob("*")):
        if not path.is_file() or path.suffix.lower() not in (".md", ".ipynb", ".py", ".txt", ".csv", ".json"):
            continue
        text = path.read_text(encoding="utf-8", errors="ignore")
        for name, pattern in PATTERNS.items():
            if re.search(pattern, text):
                found.append(f"{path.relative_to(ROOT)}: looks like a {name}")
    if found:
        print("Remove these before the project can be published:\n" + "\n".join(found))
        sys.exit(1)
    print("No access keys found.")


if __name__ == "__main__":
    main()

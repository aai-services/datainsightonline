#!/usr/bin/env python3
"""Collect post front matter into data/projects.json for the home plot and impact page.

Runs automatically before every `quarto render` (see pre-render in _quarto.yml).
Standard library only, so it works on any machine with Python 3.
"""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# Plot groups, in priority order: the first group that matches a post's
# categories becomes its colour on the home page.
GROUPS = [
    ("Machine learning", {"Machine Learning", "Deep Learning", "NLP"}),
    ("Statistics and time series", {"Statistics", "Time Series"}),
    ("Visualization", {"Visualization"}),
    ("Python and data handling", {"Python", "Pandas", "Data Cleaning", "SQL"}),
    ("Analysis projects", {"Projects", "General"}),
]


def parse_value(raw):
    raw = raw.strip()
    try:
        return json.loads(raw)
    except ValueError:
        pass
    if raw.startswith("[") and raw.endswith("]"):
        return [x.strip().strip("'\"") for x in raw[1:-1].split(",") if x.strip()]
    return raw.strip("'\"")


def front_matter(path):
    text = path.read_text(encoding="utf-8")
    m = re.match(r"---\n(.*?)\n---", text, re.S)
    meta = {}
    if m:
        for line in m.group(1).splitlines():
            if ":" in line and not line.startswith((" ", "-")):
                key, val = line.split(":", 1)
                meta[key.strip()] = parse_value(val)
    return meta


def group_for(categories):
    cats = set(categories if isinstance(categories, list) else [categories])
    for name, members in GROUPS:
        if cats & members:
            return name
    return GROUPS[-1][0]


def main():
    posts = []
    for md in sorted(ROOT.glob("post/*/index.*")):
        if md.suffix not in (".md", ".qmd"):
            continue
        meta = front_matter(md)
        date = str(meta.get("date", ""))[:10]
        if not re.match(r"\d{4}-\d{2}-\d{2}$", date):
            continue
        posts.append({
            "slug": md.parent.name,
            "title": meta.get("title", md.parent.name),
            "author": meta.get("author", ""),
            "date": date,
            "topic": group_for(meta.get("categories", [])),
        })
    posts.sort(key=lambda p: p["date"])
    out = ROOT / "data" / "projects.json"
    out.parent.mkdir(exist_ok=True)
    out.write_text(json.dumps({"groups": [g for g, _ in GROUPS], "posts": posts},
                              ensure_ascii=False, indent=0), encoding="utf-8")
    print(f"projects.json: {len(posts)} posts")


if __name__ == "__main__":
    main()

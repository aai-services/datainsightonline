#!/usr/bin/env python3
"""Write redirect pages for addresses from the old Wix site.

Runs automatically after every `quarto render` (see post-render in _quarto.yml).
Reads redirects.csv and writes one small HTML page per old address into _site/,
for example _site/data-scientist-program.html, which GitHub Pages serves at
/data-scientist-program. Each page redirects at once, tells search engines where
the content moved, and shows a plain link if redirects are blocked.

Standard library only.
"""
import csv
import html
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SITE = ROOT / "_site"
SITE_URL = "https://www.datainsightonline.com/"

PAGE = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>Moved</title>
<meta name="robots" content="noindex">
<link rel="canonical" href="{canonical}">
<meta http-equiv="refresh" content="0; url={target}">
<script>window.location.replace({target_js});</script>
</head>
<body>
<p>This page has moved. <a href="{target}">Continue to the new page</a>.</p>
</body>
</html>
"""


def main():
    rows = []
    with open(ROOT / "redirects.csv", encoding="utf-8") as f:
        lines = [line for line in f if line.strip() and not line.startswith("#")]
    for row in csv.DictReader(lines):
        old, new = row["old"].strip().strip("/"), row["new"].strip()
        if old and new:
            rows.append((old, new))

    written = 0
    for old, new in rows:
        out = SITE / f"{old}.html"
        if out.exists():
            raise SystemExit(f"redirects.csv: {old} would overwrite a real page; remove that line.")
        external = new.startswith(("http://", "https://"))
        if external:
            target, canonical = new, new
        else:
            page = new.split("#")[0]
            if not (SITE / page).exists():
                raise SystemExit(f"redirects.csv: {old} points to {page}, which the site does not have.")
            depth = old.count("/")
            target = "../" * depth + new           # relative, so it works on any host
            canonical = SITE_URL + new.split("#")[0]
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(PAGE.format(target=html.escape(target, quote=True),
                                   target_js=json.dumps(target),
                                   canonical=html.escape(canonical, quote=True)), encoding="utf-8")
        written += 1
    print(f"redirects: wrote {written} pages")


if __name__ == "__main__":
    if (SITE / "index.html").exists():        # skip partial renders such as quarto preview of one page
        main()

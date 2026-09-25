# Data Insight

Source for [datainsightonline.com](https://datainsightonline.com), a free, project-based data science training program. Data Insight is an initiative of [aai-services](https://github.com/aai-services).

The site is built with [Quarto](https://quarto.org) and published to GitHub Pages on every push to `main`.

## Preview locally

Requires Quarto and Python 3.

```bash
quarto preview
```

## Layout

- `post/<slug>/index.md`: fellow projects, one folder per post with its images
- `*.qmd`: site pages
- `styles/`: theme
- `scripts/build_projects_data.py`: builds the data behind the home plot and impact page (runs automatically before each render)

## License

Site code and theme are released under the MIT License (see `LICENSE`). Posts remain the work of their authors and are not covered by that license.

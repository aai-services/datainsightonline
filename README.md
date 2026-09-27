# Data Insight

Source for [datainsightonline.com](https://datainsightonline.com), a free, project-based data science training program. Data Insight is an initiative of [aai-services](https://github.com/aai-services).

The site is built with [Quarto](https://quarto.org) and published to GitHub Pages on every push to `main`.

## Preview locally

Requires Quarto and Python 3.

```bash
quarto preview
```

## Layout

- `post/<slug>/index.md` or `index.ipynb`: fellow projects, one folder per project with its images
- `*.qmd`: site pages
- `styles/`: theme
- `scripts/build_projects_data.py`: builds the data behind the home plot and impact page (runs before each render)
- `scripts/write_redirects.py` and `redirects.csv`: redirect pages for addresses from the old Wix site (runs after each render)
- `scripts/check_secrets.py`: fails the build if a project contains an access key
- `_docs/cutover.md`: checklist for moving datainsightonline.com to this site

Fellows publish projects by pull request; see [Publish a project](https://www.datainsightonline.com/contribute.html).

## License

Site code and theme are released under the MIT License (see `LICENSE`). Posts remain the work of their authors and are not covered by that license.

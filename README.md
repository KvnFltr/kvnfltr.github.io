# Kévin Feltrin — Portfolio

Personal research and engineering portfolio: **https://kvnfltr.github.io/**

Built with Jekyll and hosted on GitHub Pages. English content, responsive layout,
accessible navigation, light/dark themes, and no analytics or third-party scripts.
The site content and links work without JavaScript; JavaScript only adds a theme preference.

## Update

- `_pages/about.md`: introduction, current availability and selected work.
- `_portfolio/*.md`: project pages; `featured` and `order` control the work index.
- `_pages/cv.md`: contact page for the current CV.
- `_layouts/portfolio-page.html`, `assets/css/portfolio.css`: shared presentation.

Keep dates and claims consistent across the homepage and project pages. Scope
benchmark numbers to their datasets, distinguish coursework from research, and
only link repositories that visitors can access without an account.

## Build and verify

```sh
bundle install
bundle exec jekyll build
python scripts/check_site.py _site
```

GitHub Actions builds and checks internal links on pushes and pull requests.
GitHub Pages publishes from the existing configured source branch (`master`).

The original repository was forked from [AcademicPages](https://github.com/academicpages/academicpages.github.io).
Its MIT license is retained in `LICENSE`.

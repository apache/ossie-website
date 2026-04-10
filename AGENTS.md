# AGENTS.md

Guidelines for AI coding agents working on the OSI website. See `README.md` for
full setup instructions and architecture details.

## Project Overview

This is the official website for the Open Semantic Interchange (OSI) initiative.
It is built with [MkDocs](https://www.mkdocs.org/) and
[Material for MkDocs](https://squidfunk.github.io/mkdocs-material/), packaged
in a Docker image, and deployed to GitHub Pages via a GitHub Actions workflow.

## Contribution Workflow

### Fork-and-PR model

Contributors must **fork** this repository and open pull requests from their
forks. Never push branches directly to the upstream repository or commit
directly to `main`.

### Separate code from content

Each branch (and the resulting PR) should be one of:

- **Layout / code changes** — templates (`overrides/`), stylesheets
  (`docs/assets/stylesheets/`), JavaScript (`docs/assets/javascripts/`), hooks
  (`hooks/`), `Dockerfile`, `mkdocs.yml`, or workflow files
  (`.github/workflows/`).
- **Content changes** — Markdown pages (`docs/`), blog posts
  (`docs/blog/posts/`), or data files (`data/`).

Avoid mixing code and content in the same branch. Rare exceptions are acceptable
when tightly coupled (e.g., adding a member logo image alongside its
`data/home.yml` entry), but these should be the exception, not the rule.

### Write for non-developers

Many contributors to this repository are not software engineers. When acting on
their behalf, agents should:

- Write **descriptive commit messages** that explain *why* a change was made,
  not just *what* changed.
- Use **clear, readable branch names** such as `add-blog-post-ai-standard` or
  `fix-hero-gradient` rather than cryptic abbreviations.
- Keep **PR descriptions free of jargon** — explain what the change does in
  plain language.

## Project Structure

```
├── mkdocs.yml                  # Site configuration (theme, nav, plugins, hooks)
├── Dockerfile                  # Dev/build Docker image (source of truth for dependencies)
├── data/
│   └── home.yml                # Landing page content (hero, about, members, etc.)
├── docs/                       # MkDocs content root
│   ├── index.md                # Home page
│   ├── about.md                # About page
│   ├── community.md            # Community page
│   ├── blog/
│   │   ├── .authors.yml        # Blog author definitions
│   │   └── posts/              # Blog post markdown files
│   ├── spec/                   # Spec rendering (TODO)
│   └── assets/
│       ├── stylesheets/
│       │   ├── bootstrap.min.css   # Bootstrap 5.3 (loaded site-wide)
│       │   ├── global.css          # Design tokens, typography, Material palette overrides
│       │   └── home.css            # Landing page section styles
│       ├── javascripts/
│       │   └── home.js             # Landing page scroll animations
│       └── images/                 # Logos, favicon, member logos
├── overrides/                  # Jinja2 template overrides (Material custom_dir)
│   ├── home.html               # Landing page template
│   ├── content.html            # Standard content page template
│   ├── blog-post.html          # Blog post template
│   └── partials/
│       ├── header.html         # Custom single-bar site header
│       ├── post.html           # Blog index excerpt partial
│       └── external-link-icon.html
├── hooks/
│   ├── load_data.py            # Loads data/*.yml and blog metadata into Jinja2 context
│   └── fetch_spec.py           # Spec import hook (currently disabled)
└── .github/workflows/
    └── pages.yml               # GitHub Pages deployment workflow
```

## Key Architecture Notes

- **Landing page text lives in `data/home.yml`**, not in the HTML template.
  To change homepage copy, edit the YAML file — not `overrides/home.html`.
- **CSS design tokens** are defined as custom properties in
  `docs/assets/stylesheets/global.css` under `:root`. The Material for MkDocs
  palette blocks (`[data-md-color-primary=custom]`, `[data-md-color-accent=custom]`)
  must use `var()` references to these tokens so they stay in sync.
- **The GitHub Actions workflow** builds the site using the project's
  `Dockerfile`. This ensures CI uses the same MkDocs version and plugins as
  local development. If you add a plugin, add it to the `Dockerfile` — the
  workflow will pick it up automatically.
- **Blog posts** go in `docs/blog/posts/`. Front matter must include `date`
  and `authors` (referencing IDs from `docs/blog/.authors.yml`). Use
  `<!-- more -->` to define the excerpt shown on the blog index.
- **External blog posts** (articles hosted on partner sites) use the
  `external_url` front-matter field. They appear in the blog index and the
  homepage "Latest Updates" cards with an external-link icon.

## Local Development

**Docker (recommended):**

```bash
docker build -t osi-website .
docker run --rm -p 8000:8000 -v $(pwd):/docs osi-website
```

**Local Python (requires 3.9+):**

```bash
pip install mkdocs-material mkdocs-macros-plugin "mkdocs-include-markdown-plugin[cache]"
mkdocs serve
```

The site will be available at `http://localhost:8000`.

## Common Tasks

### Adding a blog post

1. Create a new `.md` file in `docs/blog/posts/` (filename becomes the URL slug).
2. Add front matter with at least `date` and `authors`.
3. Write content; use `<!-- more -->` to set the excerpt boundary.
4. For external posts, add `external_url` and a brief summary.

### Adding a working group member

1. Place the logo file (PNG or SVG) in `docs/assets/images/logos/`.
2. Add a `name` + `logo` entry under `members.list` in `data/home.yml`.

### Editing landing page text

Open `data/home.yml` and edit the relevant section (`hero`, `about`,
`members`, `get_involved`). Do not edit `overrides/home.html` for text changes.

### Adding a new content page

1. Create a `.md` file in `docs/`.
2. Set front matter: `template: content.html` and `title`.
3. Add the page to the `nav` section in `mkdocs.yml`.

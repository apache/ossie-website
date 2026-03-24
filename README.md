# OSI Website

Official website for the [Open Semantic Interchange (OSI)](https://github.com/open-semantic-interchange/OSI) initiative. Built with [MkDocs](https://www.mkdocs.org/) and [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/).

## Quick Start

### Option 1: Docker (recommended)

Build the image once, then run:

```bash
docker build -t osi-website .
docker run --rm -it -p 8000:8000 -v ${PWD}:/docs osi-website
```

The site will be available at `http://localhost:8000`.

> **Note:** Docker Desktop for Mac does not reliably propagate filesystem events
> into the container, so live-reload may not work. Restart the container to pick
> up changes, or use Option 2 for a native dev experience.

### Option 2: Local Python install

Requires Python 3.9+.

```bash
pip install mkdocs-material mkdocs-macros-plugin
mkdocs serve
```

The site will be available at `http://localhost:8000` with live-reload.

### Building for production

```bash
mkdocs build          # or: docker run --rm -v ${PWD}:/docs osi-website build
```

Output goes to the `site/` directory (gitignored).

---

## Project Structure

```
osi-website/
├── mkdocs.yml                          # Site config: theme, nav, plugins, extensions
├── Dockerfile                          # Docker dev environment (Material + macros plugin)
├── data/
│   └── home.yml                        # Landing page content (text, members, updates)
├── hooks/
│   └── load_data.py                    # MkDocs hook: injects data/*.yml into Jinja2 context
├── overrides/                          # MkDocs template overrides (custom_dir)
│   ├── home.html                       # Landing page template (extends main.html)
│   └── content.html                    # Standard content page template (extends main.html)
└── docs/                               # MkDocs content root
    ├── index.md                        # Home page (uses home.html template)
    ├── community.md                    # Community page (uses content.html template)
    ├── blog/                           # Blog (managed by blog plugin)
    │   └── posts/                      # Individual blog posts go here
    └── assets/
        ├── images/
        │   ├── logo-horizontal.png     # Site logo (header)
        │   ├── favicon.png             # Browser tab icon
        │   └── logos/                  # Member company logos (PNG/SVG)
        ├── stylesheets/
        │   ├── bootstrap.min.css       # Bootstrap 5.3 (full framework)
        │   ├── global.css              # OSI design tokens, typography, color utilities
        │   └── home.css                # Landing page styles (backgrounds, hover effects)
        └── javascripts/
            └── home.js                 # Scroll animations (landing page)
```

---

## Architecture

### Templates

Both templates extend Material for MkDocs' `main.html`, which provides the site
header (logo, navigation tabs, search), footer (social links, copyright), and
all base functionality.

| Template | Purpose | Used by |
|---|---|---|
| `home.html` | Custom landing page with hero, cards, and sections. Overrides the `tabs` block to inject landing page content and hides the default MkDocs content area. | `docs/index.md` |
| `content.html` | Standard content page. Inherits Material's default layout with sidebars, TOC, and content area — no block overrides needed. | `docs/community.md` and any future content pages |

Assign a template to a page via front matter:

```yaml
---
template: content.html
---
```

### CSS Architecture

Stylesheets load in this order (configured in `mkdocs.yml` and templates):

1. **`bootstrap.min.css`** — Full Bootstrap 5.3 framework (loaded site-wide)
2. **`global.css`** — OSI design tokens, typography classes, color utilities, Bootstrap overrides (loaded site-wide)
3. **`home.css`** — Landing page visuals: section backgrounds, hover effects, accent borders (loaded only by `home.html`)

#### Design Tokens

All shared values are defined as CSS custom properties in `global.css`:

| Category | Examples |
|---|---|
| Colors | `--osi-primary-blue`, `--osi-dark-blue`, `--osi-navy`, `--osi-light-blue`, `--osi-ice-blue` |
| Spacing | `--osi-spacing-xs` through `--osi-spacing-xl` |
| Typography | `--osi-font-body`, `--osi-font-lead`, `--osi-font-heading-sm` through `--osi-font-heading-xl` |

Utility classes: `.osi-heading-sm` / `-md` / `-lg` / `-xl`, `.osi-text-dark-blue` / `-dark-gray` / `-gray` / `-primary`, `.osi-lead`.

### Data Loading

Landing page content lives in `data/home.yml`, **not** in `mkdocs.yml`. A custom
MkDocs hook (`hooks/load_data.py`) loads all YAML files from `data/` and injects
them as global Jinja2 template variables. This means `home.html` can reference
variables like `{{ hero.title }}` and `{{ members.list }}` directly.

---

## Editing the Landing Page

**You do not need to edit HTML to change landing page content.** All text,
members, updates, and other content is stored in `data/home.yml`. The template
reads these values and renders them automatically.

### Changing text

Open `data/home.yml` and find the section you want to edit. For example, to
change the hero banner headline:

```yaml
hero:
  title: "Your new headline here"
  subtitle: "Your new subtitle here"
```

### Adding a working group member

1. Place the logo file (PNG or SVG) in `docs/assets/images/logos/`
2. Add an entry to the `members.list` array in `data/home.yml`:

```yaml
members:
  list:
    # ... existing members ...
    - name: "New Company"
      logo: "new-company-logo.png"
```

### Adding a news update

Add an entry to `updates.entries` in `data/home.yml`:

```yaml
updates:
  entries:
    - tag: "News"
      title: "Your update title"
      description: "A brief summary of the update."
      link: "https://example.com/blog-post"
```

### Changing colors

Edit the CSS custom properties in `docs/assets/stylesheets/global.css`:

```css
:root {
  --osi-primary-blue: #29B5E8;
  --osi-dark-blue: #043464;
  /* ... etc ... */
}
```

---

## Adding Content Pages

### Creating a new page

1. Create a `.md` file in `docs/`
2. Add front matter pointing to the `content.html` template:

```yaml
---
template: content.html
title: Page Title
---
```

3. Add it to the `nav:` section in `mkdocs.yml`

The page will automatically get the site header, footer, navigation sidebar,
table of contents, and all global styles.

### Navigation structure

The `nav:` section in `mkdocs.yml` controls the header tabs and sidebar menus:

```yaml
nav:
  - Home: index.md
  - Spec: spec.md
  - Community: community.md
  - GitHub: https://github.com/open-semantic-interchange/OSI
  - Blog: blog/
```

Each top-level item becomes a tab in the header. Nested items appear in the left
sidebar when that tab is active.

### Page metadata (front matter)

```yaml
---
template: content.html        # Which template to use
title: Page Title              # Browser tab title
description: A brief summary   # Search engines and social previews
hide:
  - navigation                 # Hide the left sidebar
  - toc                        # Hide the table of contents sidebar
---
```

---

## Writing Blog Posts

Blog posts live in `docs/blog/posts/`. Each post is a `.md` file with required
front matter:

```yaml
---
date: 2025-06-15
authors:
  - name: Jane Smith
categories:
  - Announcements
---

# Blog Post Title

Your post content here in Markdown...
```

The blog plugin automatically generates index, archive, and category pages.
Posts appear at `/blog/` on the site.

---

## Bootstrap and Material for MkDocs

This site loads the full Bootstrap 5.3 CSS framework alongside Material for
MkDocs. Key things to be aware of:

- **Bootstrap loads globally** — its reboot and utility classes affect all pages,
  not just the landing page.
- **Material for MkDocs scopes its styles** — content typography is inside
  `.md-typeset`, so Bootstrap's reboot generally doesn't conflict with doc/blog
  pages.
- **Button classes** — Bootstrap's `.btn`, `.btn-primary` etc. are used instead
  of custom button styles. OSI brand colors are applied via `--bs-btn-bg` and
  related CSS custom properties in `global.css`.
- **Link styles** — `--bs-link-color` and `--bs-link-decoration` are overridden
  in `global.css` to match the OSI palette and prevent unwanted underlines.

---

## Reference Links

- [MkDocs documentation](https://www.mkdocs.org/)
- [Material for MkDocs documentation](https://squidfunk.github.io/mkdocs-material/)
- [Material for MkDocs — Setting up navigation](https://squidfunk.github.io/mkdocs-material/setup/setting-up-navigation/)
- [Material for MkDocs — Blog plugin](https://squidfunk.github.io/mkdocs-material/plugins/blog/)
- [Material for MkDocs — Customization](https://squidfunk.github.io/mkdocs-material/customization/)
- [Bootstrap 5.3 documentation](https://getbootstrap.com/docs/5.3/)

## License

- Code: Apache 2.0
- Documentation: Creative Commons Attribution (CC BY)

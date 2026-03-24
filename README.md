# OSI Website

Official website for the [Open Semantic Interchange (OSI)](https://github.com/open-semantic-interchange/OSI) initiative. Built with [MkDocs](https://www.mkdocs.org/) and [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/).

## Quick Start

### Option 1: Local Python install

Requires Python 3.9+. Using [pyenv](https://github.com/pyenv/pyenv) for virtual environment management is recommended.

```bash
pip install mkdocs-material mkdocs-macros-plugin
mkdocs serve
```

The site will be available at `http://localhost:8000` with live-reload.

### Option 2: Docker (no Python required)

Build the image once, then run:

```bash
docker build -t osi-website .
docker run --rm -it -p 8000:8000 -v ${PWD}:/docs osi-website
```

Or use the base image directly (without the macros plugin pre-installed):

```bash
docker run --rm -it -p 8000:8000 -v ${PWD}:/docs squidfunk/mkdocs-material
```

### Building for production

```bash
mkdocs build
```

Output goes to the `site/` directory (gitignored).

---

## How This Site Works

This site follows the same architecture as [Apache Iceberg's website](https://github.com/apache/iceberg/tree/main/site): MkDocs with Material for MkDocs, a custom landing page template, and Bootstrap grid for layout.

### Directory Structure

```
osi-website/
├── mkdocs.yml                          # Site config + all landing page content
├── Dockerfile                          # Docker dev environment
├── overrides/
│   └── home.html                       # Landing page template (Jinja2)
└── docs/                               # MkDocs content root
    ├── index.md                        # Home page (triggers home.html)
    ├── spec.md                         # Specification page (create as needed)
    ├── community.md                    # Community page (create as needed)
    ├── blog/                           # Blog (managed by blog plugin)
    │   └── posts/                      # Individual blog posts go here
    └── assets/
        ├── images/
        │   ├── logo-horizontal.png     # Site logo (header)
        │   ├── favicon.png             # Browser tab icon
        │   └── logos/                  # Member company logos
        ├── stylesheets/
        │   ├── home.css                # Landing page styles
        │   └── bootstrap-grid.css      # Responsive grid (landing page)
        └── javascripts/
            └── home.js                 # Scroll animations (landing page)
```

---

## Editing the Landing Page

**You do not need to edit HTML to change landing page content.** All text, members, updates, and other content is stored as YAML key-value pairs in `mkdocs.yml` under the `extra:` section. The template (`overrides/home.html`) reads these values and renders them automatically.

### Changing text

Open `mkdocs.yml` and find the section you want to edit under `extra:`. For example, to change the hero banner headline:

```yaml
extra:
  hero:
    title: "Your new headline here"
    subtitle: "Your new subtitle here"
```

### Adding a new working group member

1. Place the logo file (PNG or SVG) in `docs/assets/images/logos/`
2. Add an entry to the `extra.members.list` array in `mkdocs.yml`:

```yaml
  members:
    list:
      # ... existing members ...
      - name: "New Company"
        logo: "new-company-logo.png"
```

The logo will automatically appear in the grid on the landing page.

### Adding a news update

Add an entry to `extra.updates.items` in `mkdocs.yml`:

```yaml
  updates:
    items:
      - tag: "News"
        title: "Your update title"
        description: "A brief summary of the update."
        link: "https://example.com/blog-post"
```

### Changing colors

Edit the CSS custom properties at the top of `docs/assets/stylesheets/home.css`:

```css
:root {
  --osi-primary-blue: #29B5E8;
  --osi-dark-blue: #043464;
  /* ... etc ... */
}
```

---

## Adding Documentation Pages

### Creating a new page

1. Create a `.md` file in the `docs/` directory (or a subdirectory)
2. Add it to the `nav:` section in `mkdocs.yml`

### Navigation structure

The `nav:` section in `mkdocs.yml` controls the site's navigation tabs and sidebar menus. Nesting is unlimited:

```yaml
nav:
  - Home: index.md
  - Docs:
    - Getting Started:
      - Installation: docs/getting-started/installation.md
      - Configuration:
        - Basic Setup: docs/getting-started/config-basic.md
        - Advanced: docs/getting-started/config-advanced.md
    - API Reference:
      - Overview: docs/api/overview.md
      - Endpoints: docs/api/endpoints.md
  - Community: community.md
  - Blog: blog/
```

Each top-level item becomes a tab in the header. Nested items appear in the left sidebar when that tab is active.

### Page metadata (frontmatter)

Each `.md` file can include YAML frontmatter at the top:

```yaml
---
title: Page Title              # Browser tab title; overrides the first # heading
description: A brief summary   # Used by search engines and social media previews
hide:
  - navigation                 # Hide the left sidebar on this page
  - toc                        # Hide the right table-of-contents sidebar
---
```

### Code blocks

Use fenced code blocks with a language identifier for syntax highlighting:

````markdown
```python
def hello():
    print("Hello, OSI!")
```

```sql
SELECT * FROM metrics WHERE org = 'OSI';
```
````

Material for MkDocs automatically adds a copy button to code blocks.

### Tabbed code blocks

Show the same example in multiple languages using tabs:

````markdown
=== "Python"

    ```python
    import osi
    model = osi.load("model.yaml")
    ```

=== "Java"

    ```java
    OsiModel model = Osi.load("model.yaml");
    ```
````

### Admonitions (callout boxes)

```markdown
!!! note "Important"
    This is a callout box that draws attention to key information.

!!! warning
    This highlights a potential issue.
```

See the full list of admonition types in the [Material for MkDocs docs](https://squidfunk.github.io/mkdocs-material/reference/admonitions/).

---

## Writing Blog Posts

Blog posts live in `docs/blog/posts/`. Each post is a `.md` file with required frontmatter:

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

The blog plugin automatically generates:
- A blog index page listing recent posts
- Archive pages organized by year
- Category pages

Posts appear at `/blog/` on the site.

---

## Reference Links

- [MkDocs documentation](https://www.mkdocs.org/)
- [Material for MkDocs documentation](https://squidfunk.github.io/mkdocs-material/)
- [Material for MkDocs — Setting up navigation](https://squidfunk.github.io/mkdocs-material/setup/setting-up-navigation/)
- [Material for MkDocs — Blog plugin](https://squidfunk.github.io/mkdocs-material/plugins/blog/)
- [Material for MkDocs — Code blocks](https://squidfunk.github.io/mkdocs-material/reference/code-blocks/)
- [Apache Iceberg site (reference implementation)](https://github.com/apache/iceberg/tree/main/site)

## License

- Code: Apache 2.0
- Documentation: Creative Commons Attribution (CC BY)

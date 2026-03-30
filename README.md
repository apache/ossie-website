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
pip install mkdocs-material mkdocs-macros-plugin "mkdocs-include-markdown-plugin[cache]"
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
├── Dockerfile                          # Docker dev environment (Material + plugins)
├── data/
│   └── home.yml                        # Landing page content (text, members, updates)
├── hooks/
│   ├── load_data.py                    # MkDocs hook: injects data/*.yml into Jinja2 context
│   └── fetch_spec.py                   # MkDocs hook: downloads spec.yaml, serves definitions as virtual page
├── overrides/                          # MkDocs template overrides (custom_dir)
│   ├── home.html                       # Landing page template (extends main.html)
│   ├── content.html                    # Standard content page template (extends main.html)
│   └── partials/
│       └── header.html                 # Custom single-bar header (replaces Material default)
└── docs/                               # MkDocs content root
    ├── index.md                        # Home page (uses home.html template)
    ├── community.md                    # Community page (uses content.html template)
    ├── spec/
    │   └── nightly/
    │       └── index.md                # Spec page (pulls spec.md from GitHub at build time)
    ├── blog/                           # Blog (managed by blog plugin)
    │   ├── .authors.yml                # Author definitions (name, description)
    │   └── posts/                      # Individual blog posts go here
    └── assets/
        ├── images/
        │   ├── osi-logos/              # OSI brand logos (SVG)
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
footer (social links, copyright) and all base functionality. The header is
provided by a custom partial (see below).

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

Utility classes: `.osi-text-dark-blue` / `-dark-gray` / `-gray` / `-primary`.

### Custom Header

The site uses a custom header partial (`overrides/partials/header.html`) that
replaces Material for MkDocs' default two-bar layout (header + tabs) with a
single bar:

```
| Logo       Home   Spec   Community   GitHub   Blog       (search) |
```

Key details:

- **`navigation.tabs` is kept in `mkdocs.yml`** but the rendered `.md-tabs` bar
  is hidden with `display: none`. This preserves Material's sidebar scoping
  (subpage sidebars only show children of the active top-level section).
- **`navigation.tabs.sticky` is removed** — it's unnecessary since we own the
  header template entirely.
- The header uses a **frosted-glass effect** (`backdrop-filter: blur(10px)` with
  semi-transparent white background) and a drop shadow.
- Nav links and search icon use **dark-blue** text to contrast with the
  translucent white background.
- On mobile (below Material's `76.25em` breakpoint), the nav links hide and a
  hamburger icon appears, opening Material's built-in drawer/sidebar.
- **Search** is preserved by including `partials/search.html` inside the same
  `<header>` element, which keeps Material's CSS toggle mechanism working.
- Since this fully replaces `header.html`, **upstream Material updates to the
  header will not be inherited automatically**.

### Data Loading

Landing page content lives in `data/home.yml`, **not** in `mkdocs.yml`. A custom
MkDocs hook (`hooks/load_data.py`) loads all YAML files from `data/` and injects
them as global Jinja2 template variables. This means `home.html` can reference
variables like `{{ hero.title }}` and `{{ members.list }}` directly.

### Specification Pages (Remote Fetch)

The spec pages pull content from the
[OSI GitHub repo](https://github.com/open-semantic-interchange/OSI/tree/main/core-spec)
at build time — nothing is stored locally.

| Page | Source | Mechanism |
|---|---|---|
| `spec/nightly/index.md` | `core-spec/spec.md` | `mkdocs-include-markdown-plugin` fetches the remote markdown and inlines it |
| `spec/nightly/definitions.md` | `core-spec/spec.yaml` | `hooks/fetch_spec.py` downloads the YAML, parses it, and serves a virtual page (no file on disk) |

The definitions page is a **virtual file** — it exists only in memory during the
build. The hook uses MkDocs' `on_files` event to inject a `File` object and
`on_page_read_source` to supply its markdown content. Nothing is written to the
`docs/` directory.

The `include-markdown` plugin uses custom delimiters (`{!` / `!}`) instead of the
default `{% %}` to avoid conflicts with the `macros` plugin. When writing
include directives in markdown files, use:

```markdown
{! include-markdown "https://example.com/file.md" !}
```

The plugin caches HTTP responses for 600 seconds during development to avoid
re-fetching on every save.

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
  - Spec:
    - Nightly: spec/nightly/index.md
    - Definitions: spec/nightly/definitions.md
  - Community: community.md
  - GitHub: https://github.com/open-semantic-interchange/OSI
  - Blog: blog/
```

Each top-level item becomes a nav link in the header. Nested items appear in the
left sidebar when that section is active.

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

> **Warning — `hide: [navigation]` and the homepage:** Do **not** use
> `hide: [navigation]` on `docs/index.md`. Material for MkDocs implements this
> by adding an HTML `hidden` attribute to `.md-sidebar--primary`, which removes
> the sidebar from the DOM on **all** screen sizes — including mobile, where it
> serves as the hamburger drawer menu. The homepage template (`home.html`)
> already hides the sidebar on desktop via a CSS media query, so
> `hide: [navigation]` is redundant there and breaks the mobile drawer. Use
> `hide: [toc]` only.

---

## Writing Blog Posts

Blog posts are powered by the Material for MkDocs
[blog plugin](https://squidfunk.github.io/mkdocs-material/plugins/blog/), which
automatically generates the index, archive, and category pages. Posts appear at
`/blog/` on the site.

### Creating a post

1. Create a new `.md` file in `docs/blog/posts/` (the filename becomes the URL
   slug unless overridden)
2. Add the required front matter (see below)
3. Write your content in Markdown

### Front matter

Every post **must** include `date` and `authors`. Other fields are optional but
recommended:

```yaml
---
date: 2025-06-15                # Publication date (YYYY-MM-DD)
authors:
  - ghost                       # One or more author IDs from .authors.yml
categories:
  - Announcements               # Groups the post in a category page
tags:
  - osi                         # Freeform tags
  - open-source
description: >-                 # Used in social previews and search results
  A short summary of the post.
draft: true                     # Set to true to hide the post from production
---
```

### Adding an excerpt

Place an `<!-- more -->` separator in your post. Everything above it becomes the
excerpt shown on the blog index page. If omitted, the full post body is shown.

```markdown
# Post Title

This introductory paragraph appears on the blog index as the excerpt.

<!-- more -->

The rest of the post only appears on the full post page.
```

### Managing authors

Authors are defined in `docs/blog/.authors.yml`. Each entry has an ID (used in
post front matter) and a display name:

```yaml
authors:
  jsmith:
    name: Jane Smith
    description: OSI Working Group Lead
    avatar: https://example.com/jsmith.png
```

The `avatar` field is **required** by the blog plugin — the build will fail
without it. Use a URL to a headshot or a placeholder image.

To add a new author, add an entry to this file and then reference the ID in your
post's `authors` list. See the Material for MkDocs
[authors documentation](https://squidfunk.github.io/mkdocs-material/plugins/blog/#authors)
for additional fields and links to social profiles.

### Blog plugin configuration

The blog plugin is configured in `mkdocs.yml` under `plugins`. Current settings:

| Setting | Value | Effect |
|---|---|---|
| `blog_dir` | `blog` | Posts live under `docs/blog/` |
| `blog_toc` | `true` | Post titles appear in the TOC on the index page |
| `post_date_format` | `long` | Dates render as e.g. "June 15, 2025" |
| `post_url_format` | `{slug}` | Post URLs are `/blog/<slug>/` (no date prefix) |

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
- [mkdocs-include-markdown-plugin](https://github.com/mondeja/mkdocs-include-markdown-plugin)

## License

- Code: Apache 2.0
- Documentation: Creative Commons Attribution (CC BY)

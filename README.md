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
│   └── load_data.py                    # MkDocs hook: injects data/*.yml into Jinja2 context
├── overrides/                          # MkDocs template overrides (custom_dir)
│   ├── home.html                       # Landing page template (extends main.html)
│   ├── content.html                    # Standard content page template (extends main.html)
│   ├── blog-post.html                  # Blog post template (removes author avatars)
│   └── partials/
│       ├── header.html                 # Custom single-bar header (replaces Material default)
│       ├── post.html                   # Blog index post excerpt (external link support)
│       └── external-link-icon.html     # Reusable external-link SVG icon partial
└── docs/                               # MkDocs content root
    ├── index.md                        # Home page (uses home.html template)
    ├── about.md                        # About page (Why OSI, Core Classes)
    ├── community.md                    # Community page (uses content.html template)
    ├── spec/                             # Spec rendering (TODO: re-implement build-time import)
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
| `content.html` | Standard content page. Inherits Material's default layout with sidebars, TOC, and content area — no block overrides needed. | `docs/about.md`, `docs/community.md` and any future content pages |
| `blog-post.html` | Blog post page. Identical to Material's built-in template but with author avatar/profile section removed. | Individual blog post pages |

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
| Colors | `--osi-primary-blue`, `--osi-dark-blue`, `--osi-navy`, `--osi-light-blue`, `--osi-ice-blue`, `--osi-accent-green` |
| Spacing | `--osi-spacing-xs` through `--osi-spacing-xl` |
| Typography | `--osi-font-body`, `--osi-font-lead`, `--osi-font-heading-sm` through `--osi-font-heading-xl` |

Utility classes: `.osi-text-dark-blue` / `-dark-gray` / `-gray` / `-primary`.

#### Material for MkDocs Custom Palette

Material for MkDocs applies its primary and accent colors via `data-md-color-primary`
and `data-md-color-accent` attributes on `<body>`. If no custom palette is
configured, it defaults to indigo — which would override any `:root` CSS variable
overrides because attribute selectors on `body` beat `:root` (on `html`) in the
cascade.

To use our brand colors correctly, `mkdocs.yml` sets:

```yaml
palette:
  scheme: default
  primary: custom
  accent: custom
```

This causes Material to render `data-md-color-primary="custom"` on `<body>`,
which doesn't match any built-in palette rules. Our colors are then defined in
`global.css` under matching attribute selectors:

```css
[data-md-color-primary=custom] {
  --md-primary-fg-color:        #29B5E8;
  --md-primary-fg-color--light: #56C4EF;
  --md-primary-fg-color--dark:  #043464;
  --md-typeset-a-color:         #043464;
  /* ... */
}

[data-md-color-accent=custom] {
  --md-accent-fg-color:              #56C4EF;
  --md-accent-fg-color--transparent: rgba(86, 196, 239, 0.1);
}
```

> **Important:** Do not try to override `--md-primary-fg-color` or
> `--md-typeset-a-color` in `:root` — Material's built-in `[data-md-color-primary]`
> attribute selectors on `<body>` will always win. Use the `[data-md-color-primary=custom]`
> selector instead.

### Custom Header

The site uses a custom header partial (`overrides/partials/header.html`) that
replaces Material for MkDocs' default two-bar layout (header + tabs) with a
single bar:

```
| Logo     Home  About  Spec  Community  Blog  GitHub     (search) |
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

The same hook also scans `docs/blog/posts/` for blog post front matter, sorts by
date (newest first), and injects the top 3 as `latest_posts`. The homepage
"Latest Updates" section renders these cards automatically — both internal posts
and external posts (identified by an `external_url` front matter field) appear
here and on the `/blog/` index.

### Specification Pages

Build-time rendering of the OSI specification is not yet implemented. The `Spec`
nav link currently points directly to the
[spec on GitHub](https://github.com/open-semantic-interchange/OSI/blob/main/core-spec/spec.md).
See `docs/spec/README.md` for the TODO.

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

### Changing colors

OSI design tokens live in `:root` in `docs/assets/stylesheets/global.css`:

```css
:root {
  --osi-primary-blue: #29B5E8;
  --osi-dark-blue: #043464;
  --osi-accent-green: #07A77F;
  /* ... etc ... */
}
```

If you change a color that is also mapped into Material's palette (primary blue,
light blue, dark blue), update the corresponding values in the
`[data-md-color-primary=custom]` and `[data-md-color-accent=custom]` blocks in
the same file. See the "Material for MkDocs Custom Palette" section above.

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
  - About: about.md
  - Spec: https://github.com/open-semantic-interchange/OSI/blob/main/core-spec/spec.md
  - Community: community.md
  - Blog: blog/
  - GitHub: https://github.com/open-semantic-interchange/OSI
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

### External blog posts

Posts published on partner websites (e.g. Snowflake, Databricks) can be
represented as thin markdown files. Add an `external_url` field to the front
matter — this signals to the homepage and blog index that the post links out
to an external site:

```yaml
---
date: 2025-03-12
authors:
  - snowflake
categories:
  - Announcements
description: >-
  A brief summary of the external article.
external_url: https://www.snowflake.com/en/blog/example-post/
---

# Post Title

Brief summary of the article.

<!-- more -->

Read the full post on [Snowflake's blog](https://www.snowflake.com/en/blog/example-post/).
```

External posts appear in the blog index and homepage "Latest Updates" cards with
an external link icon beside the title. The "Continue reading" link on the blog
index points to the external URL.

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
- **Link styles** — `--bs-link-color`, `--bs-link-color-rgb`, and
  `--bs-link-decoration` are overridden in `global.css` to match the OSI palette
  and prevent unwanted underlines. Material link colors are set via the custom
  palette system (see "Material for MkDocs Custom Palette" above).

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

All content in this repository — including code and documentation — is licensed under the [Apache License 2.0](LICENSE).

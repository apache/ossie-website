"""
MkDocs hook that downloads the OSI spec.yaml from GitHub and generates
a virtual definitions page as a markdown definition list.

Uses on_files to inject a virtual File into the build and
on_page_read_source to supply its content — no file is written to disk.
"""

import re
import urllib.request
from datetime import datetime, timezone

from mkdocs.structure.files import File

SPEC_YAML_URL = (
    "https://raw.githubusercontent.com/"
    "open-semantic-interchange/OSI/main/core-spec/spec.yaml"
)

DEFINITIONS_SRC_PATH = "spec/nightly/definitions.md"

SCHEMA_SECTIONS = {
    "semantic_model": "Semantic Model",
    "datasets": "Datasets",
    "relationships": "Relationships",
    "fields": "Fields",
    "metrics": "Metrics",
}

ENUM_KEYS = {"dialects", "vendors"}

_definitions_markdown = None


def _make_front_matter():
    now = datetime.now(timezone.utc)
    date_str = now.strftime("%-d %B %Y")
    time_str = now.strftime("%H:%M UTC")
    return (
        "---\n"
        "template: content.html\n"
        "title: Definitions (Nightly)\n"
        "---\n\n"
        "# OSI Schema Definitions — Nightly\n\n"
        "Field-level reference generated from\n"
        "[`spec.yaml`](https://github.com/open-semantic-interchange/OSI/"
        f"blob/main/core-spec/spec.yaml) on {date_str} at {time_str}.\n\n"
    )


def _download(url):
    with urllib.request.urlopen(url, timeout=30) as resp:
        return resp.read().decode("utf-8")


def _parse_sections(raw_text):
    """Split multi-document YAML into per-section blocks.

    Returns a list of (key, description, field_lines) tuples where
    description comes from the comment block immediately above the key.
    """
    documents = re.split(r"^---\s*$", raw_text, flags=re.MULTILINE)
    sections = []
    for doc in documents:
        lines = doc.strip().splitlines()
        if not lines:
            continue

        top_key = None
        key_index = 0
        for i, line in enumerate(lines):
            stripped = line.strip()
            if stripped.startswith("#") or not stripped:
                continue
            match = re.match(r"^(\w[\w_]*):", stripped)
            if match and match.group(1) in SCHEMA_SECTIONS:
                top_key = match.group(1)
                key_index = i
                break

        if not top_key:
            continue

        desc_parts = []
        for line in reversed(lines[:key_index]):
            stripped = line.strip()
            if stripped.startswith("#"):
                text = stripped.lstrip("# ").rstrip()
                if text and not text.endswith("Schema"):
                    desc_parts.insert(0, text)
            elif not stripped:
                continue
            else:
                break

        description = " ".join(desc_parts) if desc_parts else ""
        sections.append((top_key, description, lines[key_index + 1:]))
    return sections


def _is_example_line(text):
    """Return True if this comment line looks like a YAML example."""
    return bool(re.match(r"^[\[\-]|^\w+:\s*$", text))


def _parse_fields(lines):
    """Extract (field_name, required, description) tuples from comment+key pairs."""
    fields = []
    comment_block = []

    for line in lines:
        stripped = line.strip()

        if stripped.startswith("#"):
            comment_text = stripped.lstrip("# ").rstrip()
            if comment_text:
                comment_block.append(comment_text)
            continue

        if not stripped:
            continue

        match = re.match(r"^-?\s*(\w[\w_]*):", stripped)
        if not match:
            comment_block = []
            continue

        field_name = match.group(1)
        if field_name in SCHEMA_SECTIONS or field_name in ENUM_KEYS or field_name == "version":
            comment_block = []
            continue

        required = False
        desc_parts = []
        for c in comment_block:
            if c.startswith("Required:"):
                required = True
                rest = c[len("Required:"):].strip()
                if rest:
                    desc_parts.append(rest)
            elif c.startswith("Optional:"):
                rest = c[len("Optional:"):].strip()
                if rest:
                    desc_parts.append(rest)
            elif c.startswith("Examples:") or c.startswith("See "):
                break
            elif _is_example_line(c):
                continue
            else:
                desc_parts.append(c)

        description = " ".join(p for p in desc_parts if p)
        if not description:
            inline = re.search(r"#\s*(.+)$", stripped)
            if inline:
                description = inline.group(1).strip()

        fields.append((field_name, required, description))
        comment_block = []

    return fields


def _render_markdown(sections):
    """Produce the full definitions page as a markdown string."""
    parts = [_make_front_matter()]

    for key, description, field_lines in sections:
        title = SCHEMA_SECTIONS.get(key, key)
        parts.append(f"## {title}\n\n")

        if description:
            parts.append(f"{description}\n\n")

        fields = _parse_fields(field_lines)
        for field_name, required, desc in fields:
            marker = "**Required**" if required else "*Optional*"
            suffix = f" — {desc}" if desc else ""
            parts.append(f"`{field_name}`\n")
            parts.append(f":   {marker}{suffix}\n\n")

    return "".join(parts)


def on_files(files, config):
    """Inject a virtual File for the definitions page."""
    global _definitions_markdown

    raw_yaml = _download(SPEC_YAML_URL)
    sections = _parse_sections(raw_yaml)
    _definitions_markdown = _render_markdown(sections)

    definitions_file = File(
        path=DEFINITIONS_SRC_PATH,
        src_dir=config["docs_dir"],
        dest_dir=config["site_dir"],
        use_directory_urls=config["use_directory_urls"],
    )
    files.append(definitions_file)
    return files


def on_page_read_source(page, config):
    """Supply generated markdown for the virtual definitions page."""
    if page.file.src_path == DEFINITIONS_SRC_PATH:
        return _definitions_markdown
    return None

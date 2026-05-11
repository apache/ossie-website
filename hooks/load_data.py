"""
MkDocs hook that loads external YAML data files and blog post metadata,
injecting them as global Jinja2 template variables.

Globals provided:
  - All top-level keys from data/*.yml  (e.g. hero, about, members …)
  - latest_posts: newest blog posts (internal and external), used by
    the homepage "Latest Updates" section.
"""

import os
import re
import yaml
from datetime import date


def _load_data_files(env, config):
    data_dir = os.path.join(os.path.dirname(config.config_file_path), "data")
    if not os.path.isdir(data_dir):
        return
    for filename in sorted(os.listdir(data_dir)):
        if filename.endswith((".yml", ".yaml")):
            with open(os.path.join(data_dir, filename)) as f:
                data = yaml.safe_load(f)
            if isinstance(data, dict):
                env.globals.update(data)


_FRONT_MATTER_RE = re.compile(r"^---\s*\n(.+?)\n---", re.DOTALL)
_H1_RE = re.compile(r"^\s*#\s+(.+)", re.MULTILINE)


def _extract_title(meta, body, fname):
    """Return the post title from front-matter, the first H1, or the filename."""
    if meta.get("title"):
        return meta["title"]
    h1 = _H1_RE.search(body)
    if h1:
        return h1.group(1).strip()
    return fname.replace(".md", "").replace("-", " ").title()


def _load_latest_posts(config, limit=5):
    posts_dir = os.path.join(config["docs_dir"], "updates", "posts")
    if not os.path.isdir(posts_dir):
        return []

    posts = []
    for fname in os.listdir(posts_dir):
        if not fname.endswith(".md"):
            continue
        with open(os.path.join(posts_dir, fname)) as f:
            content = f.read()
        match = _FRONT_MATTER_RE.match(content)
        if not match:
            continue
        meta = yaml.safe_load(match.group(1))
        if not meta or meta.get("draft"):
            continue
        body = content[match.end():]
        posts.append({
            "title": _extract_title(meta, body, fname),
            "description": meta.get("description", ""),
            "date": meta.get("date", date.min),
            "external_url": meta.get("external_url"),
            "slug": fname.replace(".md", ""),
        })

    posts.sort(key=lambda p: p["date"], reverse=True)
    return posts[:limit]


def on_env(env, config, files):
    _load_data_files(env, config)
    env.globals["latest_posts"] = _load_latest_posts(config)
    return env

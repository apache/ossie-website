"""
MkDocs hook that loads external YAML data files and injects them as
global Jinja2 template variables.

This makes variables from data/*.yml available directly in template
overrides (e.g. {{ hero.title }}) without needing config.extra.
"""

import os
import yaml


def on_env(env, config, files):
    data_dir = os.path.join(os.path.dirname(config.config_file_path), "data")
    if not os.path.isdir(data_dir):
        return env

    for filename in sorted(os.listdir(data_dir)):
        if filename.endswith((".yml", ".yaml")):
            filepath = os.path.join(data_dir, filename)
            with open(filepath) as f:
                data = yaml.safe_load(f)
            if isinstance(data, dict):
                env.globals.update(data)

    return env

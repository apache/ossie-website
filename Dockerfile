# =============================================================================
# OSI Website Development Dockerfile
# =============================================================================
# Extends the official Material for MkDocs image with additional plugins.
# See README.md for usage instructions.
#
# Base image docs: https://hub.docker.com/r/squidfunk/mkdocs-material/
# =============================================================================

FROM squidfunk/mkdocs-material

# Install the macros plugin, which enables reading YAML data from mkdocs.yml
# in templates via {{ config.extra.* }} variables.
RUN pip install --no-cache-dir mkdocs-macros-plugin

# MkDocs dev server port
EXPOSE 8000

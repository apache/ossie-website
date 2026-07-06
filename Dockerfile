# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

# =============================================================================
# Apache Ossie Website Development Dockerfile
# =============================================================================
# Extends the official Material for MkDocs image with additional plugins.
# See README.md for usage instructions.
#
# Base image docs: https://hub.docker.com/r/squidfunk/mkdocs-material/
# =============================================================================

FROM squidfunk/mkdocs-material

# Install the macros plugin, which enables reading YAML data from mkdocs.yml
# in templates via {{ config.extra.* }} variables.
RUN pip install --no-cache-dir \
    mkdocs-macros-plugin \
    "mkdocs-include-markdown-plugin[cache]"

# MkDocs dev server port
EXPOSE 8000

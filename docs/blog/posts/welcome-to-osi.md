---
date: 2025-06-15
authors:
  - ghost
categories:
  - Announcements
tags:
  - osi
  - semantic-models
  - open-source
description: Introducing the Open Semantic Interchange initiative — a vendor-neutral standard for semantic model exchange across analytics, AI, and BI platforms.
---

# Welcome to the Open Semantic Interchange Initiative

The Open Semantic Interchange (OSI) initiative is a collaborative, open-source effort to create a universal standard for exchanging semantic models across analytics, AI, and business intelligence platforms. Today we're excited to share our progress and invite you to get involved.

<!-- more -->

## Why a Semantic Model Standard?

Semantic models — the curated layer of metrics, dimensions, relationships, and business logic that sits between raw data and end users — are foundational to modern data platforms. Yet every tool defines them differently. A metric in one platform doesn't translate to another without manual rework, creating drift, duplication, and inconsistency.

OSI addresses this by providing a vendor-neutral specification that any platform can read and write. Think of it as an open interchange format: define your semantic model once, and move it freely between tools.

## What OSI Covers

The specification is organized around a set of core concepts:

- **Data sources** — connections to databases, warehouses, and lakes
- **Entities and relationships** — the logical objects and how they relate to one another
- **Metrics and measures** — quantitative calculations with well-defined semantics
- **Dimensions and hierarchies** — categorical attributes and their drill paths
- **Access policies** — row-level and column-level security definitions

Each concept is expressed as a structured, human-readable YAML document that can be version-controlled, diffed, and reviewed like any other code artifact.

## How to Get Involved

We're building OSI in the open and welcome contributions at every level:

1. **Read the spec** — The current draft is available on [GitHub](https://github.com/open-semantic-interchange/OSI).
2. **Join the discussion** — Share feedback, propose features, and ask questions in [GitHub Discussions](https://github.com/open-semantic-interchange/OSI/discussions).
3. **Contribute** — Submit pull requests for spec changes, converters, or developer tooling.
4. **Spread the word** — Tell your colleagues and community about OSI.

## What's Next

Over the coming months, the working groups will be focusing on several key areas including an expression language for advanced metric calculations, composability primitives that let models reference and extend one another, and integration patterns for data catalogs and governance platforms.

Stay tuned for updates, and thank you for being part of the OSI community.

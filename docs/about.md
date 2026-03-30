---
template: content.html
title: About
---

# About OSI

The Open Semantic Interchange (OSI) is a collaborative, open-source effort dedicated to standardizing and streamlining semantic model definitions across the data analytics, AI, and BI ecosystem.

## Why OSI?

### The Challenge: Semantic Fragmentation

- **Metric Drift:** Inconsistent KPIs across different dashboards.
- **Manual Translation:** Costly, error-prone reconciliation efforts.
- **Hallucinations:** Unreliable AI grounding from conflicting data logic.
- **Integration Debt:** Complex N-to-N custom integrations between proprietary tools.

### The Solution

- **Single Source of Truth:** Unified semantic and metric definitions.
- **Native Interoperability:** Direct exchange between platforms and AI agents.
- **Trusted AI Grounding:** Agents reasoning accurately based on business logic.
- **Reduced TCO:** Lower costs through automated model exchange.

## Core Classes

The OSI specification defines the following core classes:

- **Semantic Model:** The top-level container that represents a complete semantic model, including datasets, relationships, and metrics.
- **Data Sets:** Logical datasets represent business entities or concepts (fact and dimension tables). They contain fields and define the structure of the data.
- **Fields:** Row-level attributes that can be used for grouping, filtering, and in metric expressions.
- **Measures:** Quantitative measures defined on business data, representing key calculations like sums, averages, ratios, etc. Metrics are defined at the semantic model level and can span multiple datasets.
- **Dimensions:** Categorical attributes (Where, When, Who).
- **Relationships:** Relationships define how logical datasets are connected through foreign key constraints. They support both simple and composite keys.

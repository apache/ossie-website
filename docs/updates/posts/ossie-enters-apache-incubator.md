---
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
#
date: 2026-07-10
authors:
  - jklahr
slug: ossie-enters-apache-incubator
title: "Apache Ossie (Incubating): The New Name for Open Semantic Interchange"
description: >-
  The Open Semantic Interchange project has been accepted into the Apache
  Incubator under a new name — Apache Ossie (incubating). The spec, the
  community, and the mission haven't changed, but the name, governance
  home, and long-term trajectory have.
---

# Apache Ossie (Incubating): The New Name for Open Semantic Interchange

*Apache Ossie is currently undergoing incubation at The Apache Software Foundation (ASF).*

If you've been following the Open Semantic Interchange project — the open
specification for semantic layer and ontology — there's an important update.
The project has been accepted into the Apache Incubator under a new name:
**Apache Ossie (Incubating)**.

The spec, the community, and the mission haven't changed, but the name,
governance home, and long-term trajectory have.

<!-- more -->

## Why the new name?

You may know this project as Open Semantic Interchange, or OSI. As the
community prepared for incubation — the next step in the project's open source
journey — they decided to rename the project "Ossie" to avoid confusion with
other projects in the open source ecosystem that share the OSI acronym.

The mascot is a kangaroo carrying semantic metadata in its pouch as it hops
between systems in the data stack.

Going forward:

- The project is **Apache Ossie (Incubating)**
- References to "OSI" as a project name are historical
- The specification and the YAML-based format for defining metrics, dimensions,
  and relationships is unchanged

If you've been building on Open Semantic Interchange, nothing breaks. The name
changed, but the spec didn't.

## What is Ossie?

Ossie is an open specification for both semantic layer and ontology. It defines
a vendor-neutral format for expressing business metrics, dimensions, and their
relationships as well as broader business concepts and rules. It allows any
tool — whether BI platforms, query engines, or AI agents — to consume and
produce semantic definitions without loss of meaning.

The problem it solves is straightforward: the same business concept (say,
"Monthly Active Users") is often defined inconsistently across an
organization's CRM, data warehouse, and BI tools. When a human analyst or an
AI agent runs a query, they shouldn't have to guess which definition is
correct. Ossie provides a shared, machine-readable format that encodes not
just the data but the intent and business meaning behind it.

## Why the Apache Software Foundation?

Incubating Ossie with the Apache Software Foundation ensures that it remains
an open standard with no single controlling entity. Given that the goal of
Ossie is to provide industry-wide standardization of semantic data, ensuring
that it has a vendor-neutral ground to operate in is crucial.

Under incubation, Ossie operates with public mailing lists, GitHub-based
development, a formal discussion-and-vote process for spec changes, and
committership earned through contribution rather than employer affiliation.
Note that as part of this transition, all mailing lists referring to Open
Semantic Interchange will be retired; community members should use the
ASF-provided project resources linked below instead.

## The community behind Ossie

Ossie didn't start as a single-company project, and it already isn't governed
as one. Since the repository opened in November 2025:

- More than **100 commits and 35 merged pull requests** have landed from
  contributors at Snowflake, Dremio, Salesforce, Databricks, dbt Labs,
  RelationalAI, GoodData, and Honeydew
- The participating coalition has grown from **17 launch partners to [more than
  50 organizations](https://ossie.apache.org/#get-involved)**
- Three working groups (Metric Language, Catalog, and Ontology) operate with
  dedicated leads, meetings, and public channels
- Implementations including the Ossie-to-dbt Semantic Layer converters and an
  Apache Polaris™ converter are already merged

## What's next

Snowflake was one of the founding organizations behind Open Semantic
Interchange, and we'll continue as an active contributor to Apache Ossie as
the project grows under ASF governance.

As with any Apache project, the community will decide the direction together.
There is a <a href="https://github.com/apache/ossie/blob/main/ROADMAP.md" target="_blank">large roadmap of potential additions</a>
to Ossie, and there are a few areas we're excited about and hope to work with
the community to contribute proposals for:

- Deepening the spec's expressiveness to accommodate what real enterprise
  models demand, including an expression language spec, advanced metric logic,
  windowing functions, and complex relationships
- Building converters for additional platforms and frameworks so that adopting
  Ossie doesn't require ripping out what you already have
- A standardized semantic query specification that any engine can support
- Integration with Apache Polaris so that semantic models are discoverable
  directly from the catalog

None of this is predetermined. It will go through the same open
discussion-and-vote process as everything else in the project.

## Get involved

Ossie is transitioning to ASF infrastructure as part of incubation. Whether
you're building an AI agent, BI tool, or a query engine that needs to
understand business context, Ossie is the community working to make sure you
don't have to tackle semantic interoperability alone.

- **[View Repository](https://github.com/apache/ossie)** — Browse the spec,
  raise PRs, and contribute code
- **[Start a Discussion](https://github.com/apache/ossie/discussions)** —
  Share ideas, propose features, and ask questions
- **[Join Slack](https://join.slack.com/t/apache-ossie/shared_invite/zt-42zw4rflt-Gpve8_NFJq7AsdAQTY~SCg)** —
  Chat directly with contributors
- **[Subscribe to dev@](mailto:dev-subscribe@ossie.apache.org)** — Main
  development and community discussion list

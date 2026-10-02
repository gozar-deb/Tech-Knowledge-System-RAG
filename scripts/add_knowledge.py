#!/usr/bin/env python3
"""
Systematically add new knowledge nodes that conform to the enhanced schema.
Usage:
  python scripts/add_knowledge.py --path "Artificial_Intelligence/New_Topic" --title "New Topic" --level 3
"""

from __future__ import annotations

import argparse
from datetime import date
from pathlib import Path


ENHANCED_OVERVIEW_TEMPLATE = """NODE_PATH: {node_path}
DOMAIN: {domain}
LEVEL: {level}
VERSION: 2.0
LAST_UPDATED: {today}
CONFIDENCE_SCORE: 0.85
SOURCES: curated-expansion
DIFFICULTY: {difficulty}
ESTIMATED_READ_TIME: 8m
TAGS: {tags}
PREREQUISITES: {prereqs}

RELATED_NODES:
{related}

[CHUNK: DEFINITION]
{definition}

[CHUNK: CORE_CONCEPTS]
{core_concepts}

[CHUNK: SYSTEM_DESIGN_PERSPECTIVE]
{system_design}

[CHUNK: TOOLS_AND_TECH]
{tools}

[CHUNK: REAL_WORLD_USE]
{real_world}

[CHUNK: FAILURE_MODES]
{failure_modes}

[CHUNK: OPTIMIZATION_STRATEGIES]
{optimization}

[CHUNK: SECURITY_IMPLICATIONS]
{security}

[CHUNK: CROSS_DOMAIN_LINKS]
{cross_domain}

[CHUNK: ADVANCED_TOPICS]
{advanced}

[CHUNK: COMMON_MISCONCEPTIONS]
{misconceptions}

[CHUNK: BENCHMARKS_AND_METRICS]
{benchmarks}

[CHUNK: IMPLEMENTATION_CHECKLIST]
{checklist}

[CHUNK: FURTHER_READING]
{further}
"""

ENHANCED_INDEX_TEMPLATE = """# {title}

**Path:** {node_path}
**Difficulty:** {difficulty}
**Time to Learn:** {read_time}
**Version:** 2.0 | **Last Updated:** {today}
**Confidence:** 0.85

## Quick Definition
{definition_short}

## Key Concepts
{key_concepts_md}

## Tools

| Tool | Type | Purpose |
|------|------|---------|
{tools_table}

## Retrieval Keywords
{keywords}

## Related Nodes
{related_md}

## Fast Queries This Node Should Answer
{fast_queries}

## Common Misconceptions
{misconceptions_md}

## Implementation Checklist
{checklist_md}
"""


def create_node(args):
    root = Path(args.root)
    parts = args.path.strip("/").split("/")
    node_dir = root / "Tech_Knowledge_System" / Path(*parts)
    node_dir.mkdir(parents=True, exist_ok=True)

    node_path = "Tech_Knowledge_System/" + "/".join(parts)
    domain = parts[0] if parts else "General"
    today = date.today().isoformat()

    # Placeholder content – replace with real or LLM-generated
    overview = ENHANCED_OVERVIEW_TEMPLATE.format(
        node_path=node_path,
        domain=domain,
        level=args.level,
        today=today,
        difficulty=args.difficulty,
        tags=args.tags or args.title.lower().replace(" ", ", "),
        prereqs=args.prereqs or "None specified",
        related=f"- {node_path.rsplit('/', 1)[0]}: parent",
        definition=f"{args.title} is a key topic within {domain}. [Expand with precise definition.]",
        core_concepts="- Concept 1\n- Concept 2\n- Concept 3",
        system_design="Architectural considerations, integration patterns, and operational concerns for systems involving this topic.",
        tools="Languages: Python\nFrameworks: relevant libraries\nInfrastructure: cloud / edge as applicable",
        real_world="Industry applications and case studies.",
        failure_modes="Common pitfalls, edge cases, and how systems break.",
        optimization="Performance, scaling, and efficiency techniques.",
        security="Attack surfaces, data protection, and compliance notes.",
        cross_domain="- Related domains and bidirectional links",
        advanced="Research frontiers and emerging techniques.",
        misconceptions="- Misconception 1: ...\n- Misconception 2: ...",
        benchmarks="Standard metrics, datasets, and leaderboard references.",
        checklist="1. Understand prerequisites\n2. Implement baseline\n3. Evaluate\n4. Optimize\n5. Secure & monitor",
        further="- Key papers\n- Official documentation\n- Canonical textbooks",
    )

    index = ENHANCED_INDEX_TEMPLATE.format(
        title=args.title,
        node_path=node_path,
        difficulty=args.difficulty,
        read_time="1–2 hours",
        today=today,
        definition_short=f"A concise definition of {args.title}.",
        key_concepts_md="- Key concept A\n- Key concept B",
        tools_table="| Example Tool | Library | Purpose |\n|--------------|---------|---------|",
        keywords=args.tags or args.title.lower(),
        related_md=f"- → Parent node",
        fast_queries=f"- \"What is {args.title}?\"\n- \"How does {args.title} work?\"\n- \"When should I use {args.title}?\"",
        misconceptions_md="- ...",
        checklist_md="1. ...\n2. ...",
    )

    (node_dir / "overview.txt").write_text(overview, encoding="utf-8")
    (node_dir / "index.md").write_text(index, encoding="utf-8")
    print(f"Created node: {node_dir}")
    print("Remember to expand the placeholder content and run build_index.py afterwards.")


def main():
    parser = argparse.ArgumentParser(description="Add a new knowledge node with enhanced schema")
    parser.add_argument("--root", default=".", help="Project root containing knowledge_base/")
    parser.add_argument("--path", required=True, help="Relative path under Tech_Knowledge_System, e.g. Artificial_Intelligence/New_Topic")
    parser.add_argument("--title", required=True, help="Human title")
    parser.add_argument("--level", type=int, default=3)
    parser.add_argument("--difficulty", default="Intermediate")
    parser.add_argument("--tags", default="")
    parser.add_argument("--prereqs", default="")
    args = parser.parse_args()
    create_node(args)


if __name__ == "__main__":
    main()

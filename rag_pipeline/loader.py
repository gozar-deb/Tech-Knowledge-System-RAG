"""Hierarchical knowledge base loader optimized for the Tech Knowledge System schema."""

from __future__ import annotations

import os
import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Dict, Iterator, List, Optional


@dataclass
class Chunk:
    """A single retrievable unit."""
    id: str
    node_path: str
    chunk_type: str          # DEFINITION, CORE_CONCEPTS, etc.
    text: str
    metadata: Dict[str, Any] = field(default_factory=dict)
    parent_context: str = ""  # breadcrumb + summary for hierarchical retrieval


@dataclass
class KnowledgeNode:
    """A full node (directory + overview + index)."""
    path: str
    level: int
    domain: str
    tags: List[str]
    related: List[str]
    difficulty: str = "Intermediate"
    confidence: float = 0.9
    overview_chunks: List[Chunk] = field(default_factory=list)
    index_summary: str = ""
    raw_overview: str = ""
    raw_index: str = ""


class KnowledgeLoader:
    """
    Loads the hierarchical Tech Knowledge System.
    Supports both filesystem and in-memory ZIP-style layouts.
    Produces multi-granularity chunks ready for embedding / hybrid search.
    """

    CHUNK_PATTERN = re.compile(r"\[CHUNK:\s*([A-Z0-9_]+)\](.*?)(?=\[CHUNK:|\Z)", re.DOTALL)
    HEADER_PATTERN = re.compile(r"^([A-Z_]+):\s*(.*)$", re.MULTILINE)

    def __init__(self, root: str | Path):
        self.root = Path(root)
        if not self.root.exists():
            raise FileNotFoundError(f"Knowledge root not found: {self.root}")

    def _parse_header(self, text: str) -> Dict[str, str]:
        headers = {}
        for m in self.HEADER_PATTERN.finditer(text.split("[CHUNK:")[0]):
            headers[m.group(1).strip()] = m.group(2).strip()
        return headers

    def _extract_chunks(self, text: str, node_path: str, headers: Dict[str, str]) -> List[Chunk]:
        chunks = []
        for i, m in enumerate(self.CHUNK_PATTERN.finditer(text)):
            ctype = m.group(1).strip()
            body = m.group(2).strip()
            if not body:
                continue
            # Build parent context breadcrumb
            parts = node_path.strip("/").split("/")
            breadcrumb = " > ".join(parts)
            parent_ctx = f"Node: {breadcrumb}\nDomain: {headers.get('DOMAIN', '')}\nLevel: {headers.get('LEVEL', '')}\n"
            chunk_id = f"{node_path}::{ctype}::{i}"
            meta = {
                "node_path": node_path,
                "chunk_type": ctype,
                "domain": headers.get("DOMAIN", ""),
                "level": int(headers.get("LEVEL", 0) or 0),
                "tags": [t.strip() for t in headers.get("TAGS", "").split(",") if t.strip()],
                "difficulty": headers.get("DIFFICULTY", "Intermediate"),
                "confidence": float(headers.get("CONFIDENCE_SCORE", 0.9) or 0.9),
                "version": headers.get("VERSION", "1.0"),
            }
            chunks.append(Chunk(
                id=chunk_id,
                node_path=node_path,
                chunk_type=ctype,
                text=body,
                metadata=meta,
                parent_context=parent_ctx,
            ))
        return chunks

    def load_node(self, node_dir: Path) -> Optional[KnowledgeNode]:
        overview = node_dir / "overview.txt"
        index_md = node_dir / "index.md"
        if not overview.exists():
            return None

        raw_overview = overview.read_text(encoding="utf-8", errors="replace")
        headers = self._parse_header(raw_overview)
        node_path = headers.get("NODE_PATH") or str(node_dir.relative_to(self.root)).replace("\\", "/")
        level = int(headers.get("LEVEL", 0) or 0)
        domain = headers.get("DOMAIN", node_dir.name)
        tags = [t.strip() for t in headers.get("TAGS", "").split(",") if t.strip()]
        related_raw = headers.get("RELATED_NODES", "")
        related = [r.strip() for r in re.split(r"[,\n]", related_raw) if r.strip() and not r.strip().startswith("-")]

        chunks = self._extract_chunks(raw_overview, node_path, headers)

        index_summary = ""
        raw_index = ""
        if index_md.exists():
            raw_index = index_md.read_text(encoding="utf-8", errors="replace")
            # Take the Quick Definition + Key Concepts as summary
            index_summary = raw_index[:1500]

        return KnowledgeNode(
            path=node_path,
            level=level,
            domain=domain,
            tags=tags,
            related=related,
            difficulty=headers.get("DIFFICULTY", "Intermediate"),
            confidence=float(headers.get("CONFIDENCE_SCORE", 0.9) or 0.9),
            overview_chunks=chunks,
            index_summary=index_summary,
            raw_overview=raw_overview,
            raw_index=raw_index,
        )

    def walk(self) -> Iterator[KnowledgeNode]:
        """Yield every node under the root."""
        for dirpath, dirnames, filenames in os.walk(self.root):
            if "overview.txt" in filenames:
                node = self.load_node(Path(dirpath))
                if node:
                    yield node

    def load_all_chunks(self, include_parent_context: bool = True) -> List[Chunk]:
        """Flatten to a list of chunks, optionally prefixing parent context."""
        all_chunks: List[Chunk] = []
        for node in self.walk():
            for ch in node.overview_chunks:
                if include_parent_context and ch.parent_context:
                    # Create a retrieval-optimized text version
                    enriched = Chunk(
                        id=ch.id,
                        node_path=ch.node_path,
                        chunk_type=ch.chunk_type,
                        text=f"{ch.parent_context}\n\n[{ch.chunk_type}]\n{ch.text}",
                        metadata=ch.metadata,
                        parent_context=ch.parent_context,
                    )
                    all_chunks.append(enriched)
                else:
                    all_chunks.append(ch)
            # Also add a node-level summary chunk from index
            if node.index_summary:
                summary_chunk = Chunk(
                    id=f"{node.path}::SUMMARY::0",
                    node_path=node.path,
                    chunk_type="SUMMARY",
                    text=node.index_summary,
                    metadata={
                        "node_path": node.path,
                        "chunk_type": "SUMMARY",
                        "domain": node.domain,
                        "level": node.level,
                        "tags": node.tags,
                        "difficulty": node.difficulty,
                        "confidence": node.confidence,
                    },
                    parent_context=f"Node: {node.path}",
                )
                all_chunks.append(summary_chunk)
        return all_chunks

    def get_taxonomy_tree(self) -> Dict[str, Any]:
        """Build a nested dict representing the hierarchy."""
        tree: Dict[str, Any] = {}
        for node in self.walk():
            parts = node.path.strip("/").split("/")
            current = tree
            for p in parts:
                current = current.setdefault(p, {})
            current["_meta"] = {
                "level": node.level,
                "domain": node.domain,
                "tags": node.tags,
                "difficulty": node.difficulty,
            }
        return tree

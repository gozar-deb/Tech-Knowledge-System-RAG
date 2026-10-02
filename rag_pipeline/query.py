"""RAG Query Engine - combines retrieval with simple generation / synthesis."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Dict, List, Optional

from .loader import KnowledgeLoader
from .retriever import HierarchicalRetriever, RetrievalResult


@dataclass
class RAGResponse:
    query: str
    answer: str
    sources: List[RetrievalResult]
    metadata: Dict[str, Any]


class RAGQueryEngine:
    """
    End-to-end query engine.
    In production replace the simple synthesizer with an LLM call
    (OpenAI, local GGUF, vLLM, etc.).
    """

    def __init__(self, knowledge_root: str):
        self.loader = KnowledgeLoader(knowledge_root)
        self.retriever = HierarchicalRetriever(self.loader)

    def _synthesize(self, query: str, results: List[RetrievalResult]) -> str:
        """Deterministic extractive + templated synthesis (no LLM required)."""
        if not results:
            return (
                "I could not find relevant information in the knowledge base for that query. "
                "Try rephrasing, lowering filters, or expanding the knowledge base."
            )

        parts = [f"Query: {query}\n", "Retrieved knowledge:\n"]
        for r in results:
            meta = r.chunk.metadata
            parts.append(
                f"--- [{r.rank}] {r.chunk.node_path} ({r.chunk.chunk_type}) "
                f"score={r.score:.3f} method={r.retrieval_method}\n"
                f"{r.chunk.text[:800]}{'...' if len(r.chunk.text) > 800 else ''}\n"
            )

        parts.append(
            "\n---\nSynthesis guidance: The above chunks are ordered by relevance. "
            "Use DEFINITION and CORE_CONCEPTS for explanations, FAILURE_MODES for pitfalls, "
            "IMPLEMENTATION_CHECKLIST for practical steps, and CROSS_DOMAIN_LINKS for related topics."
        )
        return "\n".join(parts)

    def query(
        self,
        question: str,
        top_k: int = 6,
        method: str = "hybrid",
        domain: Optional[str] = None,
        difficulty: Optional[str] = None,
        **filters,
    ) -> RAGResponse:
        results = self.retriever.retrieve(
            query=question,
            top_k=top_k,
            method=method,
            domain=domain,
            difficulty=difficulty,
            **filters,
        )
        answer = self._synthesize(question, results)
        return RAGResponse(
            query=question,
            answer=answer,
            sources=results,
            metadata={
                "num_chunks_searched": len(self.retriever.chunks),
                "method": method,
                "filters": {"domain": domain, "difficulty": difficulty, **filters},
            },
        )

    def explain_node(self, node_path: str) -> str:
        """Return a structured explanation of a specific node."""
        for node in self.loader.walk():
            if node.path == node_path or node.path.endswith(node_path):
                lines = [
                    f"# {node.path}",
                    f"Domain: {node.domain} | Level: {node.level} | Difficulty: {node.difficulty}",
                    f"Tags: {', '.join(node.tags)}",
                    f"Confidence: {node.confidence}",
                    "",
                    "## Index Summary",
                    node.index_summary[:2000],
                    "",
                    "## Key Chunks",
                ]
                for ch in node.overview_chunks[:6]:
                    lines.append(f"### {ch.chunk_type}\n{ch.text[:600]}\n")
                return "\n".join(lines)
        return f"Node not found: {node_path}"

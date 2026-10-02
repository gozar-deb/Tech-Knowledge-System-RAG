"""Hierarchical + hybrid retriever for the Tech Knowledge System."""

from __future__ import annotations

import math
import re
from collections import Counter, defaultdict
from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Tuple

import numpy as np

from .loader import Chunk, KnowledgeLoader


@dataclass
class RetrievalResult:
    chunk: Chunk
    score: float
    rank: int
    retrieval_method: str  # "bm25", "vector", "hybrid", "graph"


class SimpleBM25:
    """Lightweight BM25 implementation (no external deps)."""

    def __init__(self, corpus: List[str], k1: float = 1.5, b: float = 0.75):
        self.k1 = k1
        self.b = b
        self.corpus_size = len(corpus)
        self.avgdl = 0.0
        self.doc_freqs: List[Counter] = []
        self.idf: Dict[str, float] = {}
        self.doc_len: List[int] = []
        self._initialize(corpus)

    def _tokenize(self, text: str) -> List[str]:
        return re.findall(r"\w+", text.lower())

    def _initialize(self, corpus: List[str]):
        nd = defaultdict(int)  # number of documents containing term
        total_len = 0
        for doc in corpus:
            tokens = self._tokenize(doc)
            self.doc_len.append(len(tokens))
            total_len += len(tokens)
            freqs = Counter(tokens)
            self.doc_freqs.append(freqs)
            for term in freqs:
                nd[term] += 1
        self.avgdl = total_len / self.corpus_size if self.corpus_size else 0
        for term, df in nd.items():
            self.idf[term] = math.log((self.corpus_size - df + 0.5) / (df + 0.5) + 1.0)

    def get_scores(self, query: str) -> List[float]:
        tokens = self._tokenize(query)
        scores = [0.0] * self.corpus_size
        for i, freqs in enumerate(self.doc_freqs):
            dl = self.doc_len[i]
            for term in tokens:
                if term not in freqs:
                    continue
                tf = freqs[term]
                idf = self.idf.get(term, 0.0)
                denom = tf + self.k1 * (1 - self.b + self.b * dl / self.avgdl)
                scores[i] += idf * (tf * (self.k1 + 1)) / denom
        return scores


class HierarchicalRetriever:
    """
    Multi-strategy retriever:
    - BM25 keyword search
    - Dense vector search (placeholder / numpy cosine; plug in real embeddings)
    - Hierarchical expansion (retrieve leaf → promote parent context)
    - Related-node graph hops
    - Metadata filters (domain, level, tags, difficulty)
    """

    def __init__(self, loader: KnowledgeLoader, use_parent_context: bool = True):
        self.loader = loader
        self.chunks: List[Chunk] = loader.load_all_chunks(include_parent_context=use_parent_context)
        self.chunk_texts = [c.text for c in self.chunks]
        self.bm25 = SimpleBM25(self.chunk_texts) if self.chunk_texts else None
        # Simple in-memory vector store (random for demo; replace with real embeddings)
        self.embeddings: Optional[np.ndarray] = None
        self._build_simple_vectors()

    def _build_simple_vectors(self, dim: int = 64):
        """Deterministic hash-based vectors for offline demo (replace with real model)."""
        if not self.chunks:
            return
        vecs = []
        for text in self.chunk_texts:
            # Simple bag-of-chars / hash projection for reproducibility without models
            v = np.zeros(dim, dtype=np.float32)
            for i, tok in enumerate(re.findall(r"\w+", text.lower())[:200]):
                h = hash(tok) % dim
                v[h] += 1.0 + (i % 5) * 0.1
            norm = np.linalg.norm(v) + 1e-8
            vecs.append(v / norm)
        self.embeddings = np.stack(vecs) if vecs else None

    def _filter_chunks(
        self,
        domain: Optional[str] = None,
        min_level: Optional[int] = None,
        max_level: Optional[int] = None,
        tags: Optional[List[str]] = None,
        difficulty: Optional[str] = None,
    ) -> List[int]:
        indices = list(range(len(self.chunks)))
        if domain:
            indices = [i for i in indices if domain.lower() in self.chunks[i].metadata.get("domain", "").lower()]
        if min_level is not None:
            indices = [i for i in indices if self.chunks[i].metadata.get("level", 0) >= min_level]
        if max_level is not None:
            indices = [i for i in indices if self.chunks[i].metadata.get("level", 99) <= max_level]
        if tags:
            tagset = {t.lower() for t in tags}
            indices = [
                i for i in indices
                if tagset & {t.lower() for t in self.chunks[i].metadata.get("tags", [])}
            ]
        if difficulty:
            indices = [i for i in indices if self.chunks[i].metadata.get("difficulty", "").lower() == difficulty.lower()]
        return indices

    def retrieve(
        self,
        query: str,
        top_k: int = 8,
        method: str = "hybrid",
        domain: Optional[str] = None,
        min_level: Optional[int] = None,
        max_level: Optional[int] = None,
        tags: Optional[List[str]] = None,
        difficulty: Optional[str] = None,
        expand_parents: bool = True,
    ) -> List[RetrievalResult]:
        candidate_idx = self._filter_chunks(domain, min_level, max_level, tags, difficulty)
        if not candidate_idx:
            candidate_idx = list(range(len(self.chunks)))

        scores = np.zeros(len(self.chunks), dtype=np.float32)

        if method in ("bm25", "hybrid") and self.bm25:
            bm25_scores = self.bm25.get_scores(query)
            for i in candidate_idx:
                scores[i] += bm25_scores[i]

        if method in ("vector", "hybrid") and self.embeddings is not None:
            # Query vector (same simple method)
            qv = np.zeros(self.embeddings.shape[1], dtype=np.float32)
            for i, tok in enumerate(re.findall(r"\w+", query.lower())[:50]):
                h = hash(tok) % self.embeddings.shape[1]
                qv[h] += 1.0
            qv /= (np.linalg.norm(qv) + 1e-8)
            sims = self.embeddings @ qv
            for i in candidate_idx:
                scores[i] += float(sims[i]) * (1.5 if method == "hybrid" else 1.0)

        # Rank
        ranked = sorted(
            [(i, scores[i]) for i in candidate_idx],
            key=lambda x: x[1],
            reverse=True,
        )[: top_k * 2]  # over-retrieve for expansion

        results: List[RetrievalResult] = []
        seen_nodes = set()
        for rank, (idx, score) in enumerate(ranked[:top_k], 1):
            ch = self.chunks[idx]
            results.append(RetrievalResult(chunk=ch, score=float(score), rank=rank, retrieval_method=method))
            seen_nodes.add(ch.node_path)

        # Hierarchical expansion: if we hit a deep node, also surface parent summary if available
        if expand_parents:
            for r in list(results):
                parts = r.chunk.node_path.rstrip("/").split("/")
                if len(parts) > 2:
                    parent_path = "/".join(parts[:-1])
                    if parent_path not in seen_nodes:
                        # Find a SUMMARY or DEFINITION chunk of the parent
                        for i, ch in enumerate(self.chunks):
                            if ch.node_path == parent_path and ch.chunk_type in ("SUMMARY", "DEFINITION"):
                                results.append(RetrievalResult(
                                    chunk=ch,
                                    score=r.score * 0.7,
                                    rank=len(results) + 1,
                                    retrieval_method="hierarchical",
                                ))
                                seen_nodes.add(parent_path)
                                break

        # Re-sort and truncate
        results = sorted(results, key=lambda x: x.score, reverse=True)[:top_k]
        for i, r in enumerate(results, 1):
            r.rank = i
        return results

    def related_nodes(self, node_path: str, max_hops: int = 1) -> List[str]:
        """Simple related-node lookup from metadata (can be extended to full graph)."""
        related = set()
        for ch in self.chunks:
            if ch.node_path == node_path:
                # RELATED_NODES are stored in original headers; approximate via tags/domain for now
                related.update(ch.metadata.get("tags", [])[:5])
        return list(related)[:10]

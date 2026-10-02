#!/usr/bin/env python3
"""Build retrieval indexes from the knowledge base."""

import argparse
import json
import pickle
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from rag_pipeline.loader import KnowledgeLoader
from rag_pipeline.retriever import HierarchicalRetriever


def main():
    parser = argparse.ArgumentParser(description="Build indexes for Tech Knowledge System RAG")
    parser.add_argument("--root", default="knowledge_base/Tech_Knowledge_System", help="Path to knowledge root")
    parser.add_argument("--out", default="indexes", help="Output directory for indexes")
    args = parser.parse_args()

    root = Path(args.root)
    out = Path(args.out)
    out.mkdir(parents=True, exist_ok=True)

    print(f"Loading knowledge base from {root} ...")
    loader = KnowledgeLoader(root)
    chunks = loader.load_all_chunks(include_parent_context=True)
    print(f"Loaded {len(chunks)} chunks from hierarchy")

    # Taxonomy
    tree = loader.get_taxonomy_tree()
    with open(out / "taxonomy.json", "w", encoding="utf-8") as f:
        json.dump(tree, f, indent=2)
    print(f"Wrote taxonomy.json")

    # Chunk catalog
    catalog = [
        {
            "id": c.id,
            "node_path": c.node_path,
            "chunk_type": c.chunk_type,
            "text_preview": c.text[:200],
            "metadata": c.metadata,
        }
        for c in chunks
    ]
    with open(out / "chunk_catalog.json", "w", encoding="utf-8") as f:
        json.dump(catalog, f, indent=2)
    print(f"Wrote chunk_catalog.json ({len(catalog)} entries)")

    # Build retriever (includes BM25 + simple vectors)
    retriever = HierarchicalRetriever(loader)
    with open(out / "retriever.pkl", "wb") as f:
        pickle.dump({
            "chunk_ids": [c.id for c in retriever.chunks],
            "embeddings_shape": retriever.embeddings.shape if retriever.embeddings is not None else None,
        }, f)
    print("Built in-memory retriever (BM25 + hash vectors)")
    print("Done. Use rag_pipeline.query.RAGQueryEngine for queries.")


if __name__ == "__main__":
    main()

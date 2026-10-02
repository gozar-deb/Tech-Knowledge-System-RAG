# Tech Knowledge System RAG – Improved Edition (v2.0)

Complete hierarchical technology knowledge base + production-ready Retrieval-Augmented Generation (RAG) pipeline.

**Status (this package):**  
- **838 / 838** topics fully present  
- All former stub nodes expanded with rich content  
- Every `overview.txt` and `index.md` upgraded to schema v2.0  
- Working hierarchical + hybrid RAG system included  

---

## 1. What This Package Contains

| Component | Description |
|-----------|-------------|
| `knowledge_base/` | Full hierarchical knowledge base (838 topics) |
| `rag_pipeline/` | Loader, hierarchical hybrid retriever, query engine |
| `scripts/` | Enrichment, indexing, and knowledge-addition utilities |

### Knowledge Base Statistics
- **838** `overview.txt` files (detailed, chunked content)
- **838** `index.md` files (human-readable summaries + retrieval keywords)
- Hierarchical taxonomy covering:
  - Artificial Intelligence (ML, DL, Agents, NLP, CV, Generative AI, …)
  - Cybersecurity
  - Software Engineering
  - Cloud & Distributed Computing
  - Quantum Computing
  - Robotics & Automation
  - Databases & Storage
  - Hardware & Computer Architecture
  - Operating Systems
  - DevOps & SRE
  - Embedded Systems & IoT
  - Bioinformatics
  - Mathematical Foundations of Computing
  - Human-Computer Interaction
  - Ethics & Society in Technology
  - and more

---

## 2. Improved Schema (v2.0) – Applied to Every Node

### Header fields (overview.txt)
```
NODE_PATH: ...
DOMAIN: ...
LEVEL: ...
VERSION: 2.0
LAST_UPDATED: 2026-10-02
CONFIDENCE_SCORE: 0.85–0.95
SOURCES: ...
DIFFICULTY: Beginner | Intermediate | Advanced | Expert
ESTIMATED_READ_TIME: Xm
TAGS: comma-separated keywords
PREREQUISITES: ...
RELATED_NODES: ...
```

### Content chunks present in every overview.txt
- `[CHUNK: DEFINITION]`
- `[CHUNK: CORE_CONCEPTS]`
- `[CHUNK: SYSTEM_DESIGN_PERSPECTIVE]`
- `[CHUNK: TOOLS_AND_TECH]`
- `[CHUNK: REAL_WORLD_USE]`
- `[CHUNK: FAILURE_MODES]`
- `[CHUNK: OPTIMIZATION_STRATEGIES]`
- `[CHUNK: SECURITY_IMPLICATIONS]`
- `[CHUNK: CROSS_DOMAIN_LINKS]`
- `[CHUNK: ADVANCED_TOPICS]`
- **New in v2.0:**
  - `[CHUNK: COMMON_MISCONCEPTIONS]`
  - `[CHUNK: BENCHMARKS_AND_METRICS]`
  - `[CHUNK: IMPLEMENTATION_CHECKLIST]`
  - `[CHUNK: FURTHER_READING]`

### index.md structure
- Quick Definition
- Key Concepts
- Tools table
- Retrieval Keywords
- Related Nodes
- Fast Queries This Node Should Answer
- Common Misconceptions
- Implementation Checklist

---

## 3. Directory Layout

```
Tech_Knowledge_System_RAG_Improved/
├── README.md                          ← this file
|
├── knowledge_base/
│   └── Tech_Knowledge_System/         ← root of the hierarchy
│       ├── overview.txt
│       ├── index.md
│       ├── Artificial_Intelligence/
│       ├── Cybersecurity/
│       ├── Cloud_and_Distributed_Computing/
│       ├── Quantum_Computing/
│       ├── ... (all domains)
│       └── Mathematical_Foundations_of_Computing/
├── rag_pipeline/
│   ├── __init__.py
│   ├── loader.py                      ← hierarchical knowledge loader + chunker
│   ├── retriever.py                   ← BM25 + vector + hierarchical retriever
│   └── query.py                       ← end-to-end RAG query engine
└── scripts/
    ├── enrich_batched.py              ← robust batch enricher (already run)
    ├── enrich_and_expand.py           ← original enricher
    ├── build_index.py                 ← builds taxonomy + chunk catalog
    └── add_knowledge.py               ← create new nodes with correct schema
```

---

## 4. Quick Start

### Requirements
- Python 3.9+
- `numpy` (only external dependency for the basic retriever)

```bash
# Optional but recommended for better vectors later
pip install numpy
```

### 1. Build indexes (do this once)
```bash
cd Tech_Knowledge_System_RAG_Improved
python3 scripts/build_index.py --root knowledge_base/Tech_Knowledge_System
```

### 2. Run a query
```bash
python3 -c "
from rag_pipeline.query import RAGQueryEngine

engine = RAGQueryEngine('knowledge_base/Tech_Knowledge_System')

response = engine.query('What is FlashAttention and when should I use it?')
print(response.answer)

print('\n--- Top sources ---')
for s in response.sources:
    print(f'{s.rank}. {s.chunk.node_path}  [{s.chunk.chunk_type}]  score={s.score:.3f}')
"
```

### 3. Explain a specific node
```bash
python3 -c "
from rag_pipeline.query import RAGQueryEngine
engine = RAGQueryEngine('knowledge_base/Tech_Knowledge_System')
print(engine.explain_node('Artificial_Intelligence/Deep_Learning/Transformer_Architecture/Efficient_Transformers'))
"
```

### 4. Filtered retrieval
```python
response = engine.query(
    "Explain zero trust architecture",
    domain="Cybersecurity",
    difficulty="Advanced",
    top_k=6,
    method="hybrid"          # "bm25" | "vector" | "hybrid"
)
```

---

## 5. RAG Pipeline Details

### Loader (`rag_pipeline/loader.py`)
- Walks the entire hierarchy
- Parses NODE_PATH, DOMAIN, LEVEL, TAGS, DIFFICULTY, etc.
- Extracts every `[CHUNK: …]` section
- Injects parent-context breadcrumbs for hierarchical retrieval
- Also creates node-level SUMMARY chunks from `index.md`

### Retriever (`rag_pipeline/retriever.py`)
- **Hybrid search**: BM25 (keyword) + simple dense vectors
- Metadata filters: domain, level range, tags, difficulty
- Hierarchical expansion (retrieve leaf → also surface parent context)
- Related-node awareness
- Easy to swap the hash-based vectors for real embeddings (sentence-transformers, voyage, OpenAI, etc.)

### Query Engine (`rag_pipeline/query.py`)
- End-to-end: question → retrieve → synthesize answer with sources
- Deterministic extractive synthesis (no LLM required for basic use)
- Ready to replace the synthesizer with any LLM call

---

## 6. Adding New Knowledge

```bash
python3 scripts/add_knowledge.py \
  --path "Artificial_Intelligence/New_Topic_Name" \
  --title "New Topic Name" \
  --level 3 \
  --difficulty Intermediate \
  --tags "tag1, tag2, tag3"
```

This creates a correctly structured node with all v2.0 fields and placeholder content that you can then expand.

After adding nodes, re-run:
```bash
python3 scripts/build_index.py --root knowledge_base/Tech_Knowledge_System
```

---

## 7. The Four Implemented Improvements

1. **Content Completeness**  
   - All 19 previously empty/stub nodes fully written  
   - Schema enrichment + 4 new practical chunks applied to every node  

2. **Better Chunking & Representation**  
   - Hierarchical loader with parent context  
   - Multi-granularity chunks (section + summary)  
   - Rich filterable metadata on every chunk  

3. **Real RAG System**  
   - Working hybrid retriever + query engine  
   - Hierarchical expansion and metadata filtering  

4. **Systematic Knowledge Addition**  
   - Schema-compliant node creator  
   - Batch enrichment scripts  
   - Index builder  

---

## 8. Upgrading the Retriever (optional)

The included vectors are simple deterministic hash projections so the package works offline with zero extra dependencies. For production quality:

```bash
pip install sentence-transformers chromadb   # or faiss-cpu, qdrant-client, etc.
```

Then replace the `_build_simple_vectors` method in `rag_pipeline/retriever.py` with a real embedding model and (optionally) a persistent vector store.

---

## 9. File Counts & Integrity Check

```bash
# Should both print 838
find knowledge_base -name 'overview.txt' | wc -l
find knowledge_base -name 'index.md'     | wc -l

# Spot-check a former stub
ls knowledge_base/Tech_Knowledge_System/Artificial_Intelligence/Machine_Learning/Optimization_and_Training/Loss_Functions_and_Objectives/
# → overview.txt  index.md  (both non-empty and VERSION: 2.0)
```

---

## 10. License & Provenance

- Knowledge content derived from the original Tech_Knowledge_System_RAG corpus, substantially expanded and restructured.
- Code (loader, retriever, query engine, scripts) written for this improved package.
- Schema v2.0 and all enrichment performed 2026-10-02.

---

**You now have a complete, queryable, extensible technical knowledge system.**  
Start with the Quick Start section above.

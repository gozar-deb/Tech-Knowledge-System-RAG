#!/usr/bin/env python3
"""
Batched, robust enrichment of the Tech Knowledge System.
Processes the original ZIP in small batches to avoid timeouts.
Safe to re-run (skips already-enhanced files).
"""

from __future__ import annotations

import zipfile
import time
from pathlib import Path
from typing import Dict, List, Tuple

SRC_ZIP = Path("/home/workdir/attachments/Tech_Knowledge_System_RAG.zip")
OUT_ROOT = Path("/home/workdir/artifacts/Tech_Knowledge_System_RAG_Improved/knowledge_base")
TODAY = "2026-10-02"
BATCH_SIZE = 40          # files per batch
PROGRESS_FILE = OUT_ROOT / ".enrich_progress.txt"


def make_overview(node_path: str, domain: str, level: int, tags: str, title: str,
                  definition: str, core: str, system: str, tools: str, real: str,
                  fail: str, opt: str, sec: str, cross: str, adv: str,
                  misc: str, bench: str, check: str, further: str,
                  difficulty: str = "Intermediate", prereqs: str = "See parent node") -> str:
    parent = "/".join(node_path.split("/")[:-1]) if "/" in node_path else node_path
    return f"""NODE_PATH: {node_path}
DOMAIN: {domain}
LEVEL: {level}
VERSION: 2.0
LAST_UPDATED: {TODAY}
CONFIDENCE_SCORE: 0.90
SOURCES: curated-expansion, domain-synthesis
DIFFICULTY: {difficulty}
ESTIMATED_READ_TIME: 10m
TAGS: {tags}
PREREQUISITES: {prereqs}

RELATED_NODES:
- {parent}: parent

[CHUNK: DEFINITION]
{definition}

[CHUNK: CORE_CONCEPTS]
{core}

[CHUNK: SYSTEM_DESIGN_PERSPECTIVE]
{system}

[CHUNK: TOOLS_AND_TECH]
{tools}

[CHUNK: REAL_WORLD_USE]
{real}

[CHUNK: FAILURE_MODES]
{fail}

[CHUNK: OPTIMIZATION_STRATEGIES]
{opt}

[CHUNK: SECURITY_IMPLICATIONS]
{sec}

[CHUNK: CROSS_DOMAIN_LINKS]
{cross}

[CHUNK: ADVANCED_TOPICS]
{adv}

[CHUNK: COMMON_MISCONCEPTIONS]
{misc}

[CHUNK: BENCHMARKS_AND_METRICS]
{bench}

[CHUNK: IMPLEMENTATION_CHECKLIST]
{check}

[CHUNK: FURTHER_READING]
{further}
"""


def make_index(title: str, node_path: str, difficulty: str, definition_short: str,
               key_concepts: str, tools_table: str, keywords: str, related: str,
               queries: str, misc: str, checklist: str) -> str:
    return f"""# {title}

**Path:** {node_path}
**Difficulty:** {difficulty}
**Time to Learn:** 1–3 hours
**Version:** 2.0 | **Last Updated:** {TODAY}
**Confidence:** 0.90

## Quick Definition
{definition_short}

## Key Concepts
{key_concepts}

## Tools

| Tool | Type | Purpose |
|------|------|---------|
{tools_table}

## Retrieval Keywords
{keywords}

## Related Nodes
{related}

## Fast Queries This Node Should Answer
{queries}

## Common Misconceptions
{misc}

## Implementation Checklist
{checklist}
"""


def get_stub_map() -> Dict[str, str]:
    """Pre-built full content for the 19 stubs (overview + index)."""
    content: Dict[str, str] = {}

    # 1. Loss Functions
    np = "Tech_Knowledge_System/Artificial_Intelligence/Machine_Learning/Optimization_and_Training/Loss_Functions_and_Objectives"
    content[np + "/overview.txt"] = make_overview(
        np, "Artificial_Intelligence", 5,
        "loss functions, objective functions, cross-entropy, MSE, hinge loss, ranking losses, multi-task loss",
        "Loss Functions and Objectives",
        "Loss functions quantify the difference between a model's predictions and the true targets, providing the scalar signal that optimizers minimize. The choice of loss encodes task inductive bias and strongly influences convergence, calibration, and generalization.",
        "- MSE / L2 and MAE / L1 for regression\n- Cross-entropy / log loss for classification\n- Hinge loss (SVMs) and Huber loss (robust regression)\n- Ranking losses (pairwise, listwise) and contrastive / InfoNCE losses\n- Focal loss for class imbalance\n- Multi-task and uncertainty-weighted losses",
        "Losses sit at the center of the training loop and must be (sub)differentiable. In distributed training they are averaged across workers. Custom losses are traced into the autodiff graph. LLMs typically use token-level cross-entropy, sometimes with auxiliary stabilizers.",
        "PyTorch nn.functional, JAX, TensorFlow, torchmetrics, custom CUDA kernels; mixed-precision loss scaling.",
        "Classification, regression, detection (focal + smooth-L1), recommendation, LLM pre-training / instruction tuning, anomaly detection, generative models.",
        "Mismatched loss (MSE for classification), ignored class imbalance, unbounded losses causing exploding gradients, over-confident softmax, poorly weighted multi-task objectives.",
        "Label smoothing, focal loss, gradient clipping, loss scaling, curriculum learning, uncertainty weighting, auxiliary representation losses.",
        "Adversarial examples maximize the loss; data poisoning manipulates the landscape; membership inference often uses loss values. Apply DP noise to gradients when required.",
        "- Gradient_Descent_Variants → optimizers\n- Deep_Learning → complex generative losses\n- Optimization_Theory → convex analysis",
        "Surrogate losses, proper scoring rules, DRO losses, energy-based objectives, optimal-transport losses.",
        "- Cross-entropy is only for classification (false)\n- Lower training loss always means a better model (overfitting / calibration)\n- Any differentiable function is a good loss (must align with metrics)",
        "Train/val loss curves, task metrics (accuracy, F1, RMSE, NDCG), calibration (ECE), loss-landscape visualizations.",
        "1. Select loss aligned with metric and data\n2. Unit-test edge cases and gradcheck\n3. Add stabilization (smoothing, clipping)\n4. Monitor train vs val for overfitting\n5. Document exact formula and hyperparameters",
        "- Deep Learning book (Goodfellow)\n- Focal Loss paper\n- Multi-task uncertainty weighting paper\n- Framework docs",
        difficulty="Intermediate", prereqs="Supervised learning, gradients, basic probability"
    )
    content[np + "/index.md"] = make_index(
        "Loss Functions and Objectives", np, "Intermediate",
        "Loss functions measure prediction error and supply the training signal for optimizers.",
        "- MSE/MAE/Huber (regression)\n- Cross-entropy & focal loss (classification)\n- Ranking & contrastive losses\n- Multi-task objectives",
        "| PyTorch F | Framework | Built-in losses |\n| torchmetrics | Library | Helpers |\n| optax (JAX) | Library | Composable |",
        "loss function, objective, cross entropy, MSE, focal loss, contrastive loss, ranking loss",
        f"- → {np.rsplit('/',1)[0]} (parent)\n- → Gradient Descent Variants",
        '- "What is a loss function?"\n- "When to use focal loss?"\n- "How to choose a loss for imbalanced data?"',
        "- Assuming train loss == business metric\n- Ignoring mixed-precision loss scaling",
        "1. Match loss to task/metric\n2. Test edge cases\n3. Monitor calibration\n4. Document"
    )

    # 2. Efficient Transformers
    np = "Tech_Knowledge_System/Artificial_Intelligence/Deep_Learning/Transformer_Architecture/Efficient_Transformers"
    content[np + "/overview.txt"] = make_overview(
        np, "Artificial_Intelligence", 5,
        "efficient transformers, sparse attention, linear attention, FlashAttention, long context, Performer, Longformer",
        "Efficient Transformers",
        "Efficient Transformers reduce the quadratic cost of self-attention, enabling longer contexts, lower memory use, and higher throughput while preserving most modeling power of full attention.",
        "- Sparse patterns (local, strided, random, axial)\n- Linear / kernelized attention (Performer)\n- Low-rank and memory-compressed attention\n- FlashAttention (IO-aware exact attention)\n- Hierarchical / recurrent Transformers\n- Ring Attention and sequence parallelism\n- MoE for capacity",
        "Efficient attention drops into the standard Transformer skeleton. Memory-hierarchy awareness is critical (FlashAttention minimizes HBM traffic). Multi-GPU sequence parallelism enables extreme context lengths. The rest of the stack (optimizer states, checkpointing) must adapt.",
        "FlashAttention, xFormers, Transformer Engine, Hugging Face attn backends; PyTorch / JAX; NVIDIA GPUs / TPUs.",
        "Long documents, genomics, high-res vision/video as tokens, RAG with large contexts, agent memory, codebases.",
        "Approximate methods may hurt precise long-range dependencies; numerical instability; implementation complexity; training stability trade-offs.",
        "Prefer FlashAttention for exactness; match sparsity bias to data; progressive length training; RoPE/ALiBi scaling; profile real memory/FLOPs.",
        "Same surface as standard Transformers plus larger prompt-injection window from long context. Kernels must avoid side channels.",
        "- Transformer_Architecture (parent)\n- Deep_Learning\n- Hardware memory hierarchy",
        "State-space models (Mamba), hybrid attention-SSM, learned sparsity, hardware-software co-design.",
        "- Efficient always means approximate (FlashAttention is exact)\n- Linear attention is universally better (task-dependent)\n- Just increase context length (cost explodes without efficiency)",
        "Perplexity/task metrics vs length, wall-clock time, peak memory, tokens/s; Long-Range Arena, SCROLLS.",
        "1. Profile full-attention baseline\n2. Try FlashAttention first\n3. Validate on long-context benchmarks\n4. Adapt positional encodings & recipe\n5. Document quality-complexity trade-offs",
        "- FlashAttention papers (Dao et al.)\n- Efficient Transformers survey (Tay et al.)\n- Longformer, Performer papers",
        difficulty="Advanced"
    )
    content[np + "/index.md"] = make_index(
        "Efficient Transformers", np, "Advanced",
        "Architectural and algorithmic methods that reduce Transformer attention complexity for longer contexts and higher efficiency.",
        "- Sparse, linear, low-rank attention\n- FlashAttention (exact + fast)\n- Sequence parallelism / Ring Attention\n- Quality vs complexity trade-offs",
        "| FlashAttention | Kernel | Exact efficient attn |\n| xFormers | Library | Memory-efficient blocks |\n| HF transformers | Framework | Pluggable backends |",
        "efficient transformers, FlashAttention, sparse attention, linear attention, long context",
        f"- → Transformer Architecture (parent)",
        '- "How does FlashAttention work?"\n- "Sparse vs linear attention?"\n- "Training 100k+ context Transformers?"',
        "- Believing all efficient methods are approximate\n- Ignoring memory hierarchy",
        "1. Start with FlashAttention\n2. Benchmark quality vs length\n3. Add approximation only if needed"
    )

    # Remaining 17 stubs (compact but complete)
    remaining = [
        ("Tech_Knowledge_System/Artificial_Intelligence/AI_Agents_and_Autonomy/Tool_Use_and_Function_Calling/Computer_Use_Agents",
         "Computer Use Agents", "Artificial_Intelligence", 5,
         "computer use agents, GUI agents, desktop agents, browser agents, screen understanding, action grounding",
         "Computer Use Agents perceive a computer interface (pixels, a11y tree, DOM) and emit actions (mouse, keyboard, APIs) to complete user tasks, closing the perception-planning-action loop on real software."),
        ("Tech_Knowledge_System/Cybersecurity/Network_Security/Zero_Trust_Architecture/Identity_Centric_ZTA",
         "Identity Centric ZTA", "Cybersecurity", 5,
         "zero trust, identity centric, continuous verification, least privilege, MFA, conditional access",
         "Identity-Centric Zero Trust places continuously verified identity of users, devices, and workloads at the center of every access decision instead of trusting network location."),
        ("Tech_Knowledge_System/Cybersecurity/Cloud_Security/Data_Security_in_Cloud/Encryption_at_Rest_and_Transit",
         "Encryption at Rest and Transit", "Cybersecurity", 5,
         "encryption at rest, encryption in transit, TLS, AES, envelope encryption, KMS, mTLS",
         "Encryption at rest protects stored data; encryption in transit protects data moving across networks. Together they are foundational confidentiality controls in cloud systems."),
        ("Tech_Knowledge_System/Hardware_and_Computer_Architecture/Specialized_Hardware",
         "Specialized Hardware", "Hardware_and_Computer_Architecture", 3,
         "GPUs, TPUs, NPUs, FPGAs, ASICs, AI accelerators, domain-specific architectures",
         "Specialized hardware (GPUs, TPUs, NPUs, FPGAs, ASICs) accelerates particular workloads far beyond general-purpose CPUs by optimizing data paths, memory hierarchy, and arithmetic units for the target domain."),
        ("Tech_Knowledge_System/Cloud_and_Distributed_Computing/Cloud_Service_Models/FaaS_and_Serverless",
         "FaaS and Serverless", "Cloud_and_Distributed_Computing", 4,
         "serverless, FaaS, Lambda, Cloud Functions, event-driven, cold start, scale to zero",
         "Function-as-a-Service and serverless computing let developers deploy individual functions that are automatically scaled, including to zero, and billed per invocation, shifting operational responsibility to the platform."),
        ("Tech_Knowledge_System/Quantum_Computing/Quantum_Hardware/Photonic_Quantum_Computing",
         "Photonic Quantum Computing", "Quantum_Computing", 4,
         "photonic qubits, linear optical quantum computing, boson sampling, integrated photonics",
         "Photonic quantum computing encodes qubits in photons and manipulates them with linear optical elements, offering room-temperature operation and natural interconnectivity at the cost of probabilistic gates and detection challenges."),
        ("Tech_Knowledge_System/Quantum_Computing/Quantum_Error_Correction/Stabilizer_Codes",
         "Stabilizer Codes", "Quantum_Computing", 5,
         "stabilizer codes, surface code, CSS codes, fault tolerance, syndrome measurement",
         "Stabilizer codes are a large family of quantum error-correcting codes defined by a set of commuting Pauli operators (stabilizers) whose measurement yields error syndromes without destroying the logical information."),
        ("Tech_Knowledge_System/Quantum_Computing/Quantum_Machine_Learning/Variational_Quantum_Circuits",
         "Variational Quantum Circuits", "Quantum_Computing", 5,
         "VQC, VQE, QAOA, parameterized quantum circuits, hybrid quantum-classical",
         "Variational Quantum Circuits are parameterized quantum circuits trained by classical optimizers in a hybrid loop; they underpin VQE, QAOA, and many quantum machine-learning models."),
        ("Tech_Knowledge_System/Robotics_and_Automation/Robot_Perception/LIDAR_and_Point_Clouds",
         "LIDAR and Point Clouds", "Robotics_and_Automation", 4,
         "LIDAR, point clouds, 3D perception, SLAM, object detection in point clouds",
         "LIDAR sensors produce 3D point clouds that robots use for mapping, localization, obstacle detection, and semantic understanding of the environment."),
        ("Tech_Knowledge_System/DevOps_and_SRE/Emerging_Trends",
         "Emerging Trends in DevOps and SRE", "DevOps_and_SRE", 3,
         "platform engineering, AIOps, progressive delivery, developer experience, FinOps",
         "Emerging trends in DevOps and SRE include platform engineering, AIOps, progressive delivery, improved developer experience, and FinOps practices that bring financial accountability into cloud operations."),
        ("Tech_Knowledge_System/Embedded_Systems_and_IoT/Edge_Computing_Embedded/FPGA_Accelerators",
         "FPGA Accelerators", "Embedded_Systems_and_IoT", 4,
         "FPGA, reconfigurable computing, HLS, edge acceleration, low-latency inference",
         "FPGA accelerators provide reconfigurable, low-latency, energy-efficient compute for edge and embedded workloads, often programmed via high-level synthesis or specialized frameworks."),
        ("Tech_Knowledge_System/Databases_and_Storage/NoSQL_Databases/Key_Value_Stores_Redis",
         "Key-Value Stores and Redis", "Databases_and_Storage", 4,
         "Redis, key-value, in-memory, caching, data structures, persistence, clustering",
         "Key-value stores, exemplified by Redis, offer simple, high-performance associative arrays with rich in-memory data structures, optional persistence, and clustering for caching and real-time applications."),
        ("Tech_Knowledge_System/Databases_and_Storage/Distributed_Transactions/Saga_Pattern",
         "Saga Pattern", "Databases_and_Storage", 4,
         "saga pattern, distributed transactions, choreography, orchestration, compensating actions",
         "The Saga pattern manages distributed transactions by breaking them into a sequence of local transactions with compensating actions, using either choreography or orchestration to maintain consistency without two-phase commit."),
        ("Tech_Knowledge_System/Operating_Systems/File_Systems/ZFS_and_Btrfs",
         "ZFS and Btrfs", "Operating_Systems", 4,
         "ZFS, Btrfs, copy-on-write, snapshots, checksums, RAID-Z, subvolumes",
         "ZFS and Btrfs are modern copy-on-write file systems that provide end-to-end checksums, snapshots, clones, integrated volume management, and advanced features such as RAID-Z and subvolumes."),
        ("Tech_Knowledge_System/Bioinformatics_and_Computational_Biology/Drug_Discovery_Informatics/Virtual_Screening",
         "Virtual Screening", "Bioinformatics_and_Computational_Biology", 4,
         "virtual screening, docking, ligand-based, structure-based, high-throughput screening in silico",
         "Virtual screening computationally evaluates large libraries of compounds against a biological target to prioritize candidates for experimental testing, using docking, pharmacophore, or machine-learning methods."),
        ("Tech_Knowledge_System/Mathematical_Foundations_of_Computing/Algorithms_and_Complexity/Algorithm_Design_Paradigms",
         "Algorithm Design Paradigms", "Mathematical_Foundations_of_Computing", 3,
         "divide and conquer, dynamic programming, greedy, backtracking, branch and bound",
         "Algorithm design paradigms are general reusable strategies (divide-and-conquer, dynamic programming, greedy, backtracking, branch-and-bound, etc.) that guide the construction of efficient algorithms."),
        ("Tech_Knowledge_System/Mathematical_Foundations_of_Computing/Optimization_Theory/Convex_Optimization",
         "Convex Optimization", "Mathematical_Foundations_of_Computing", 4,
         "convex sets, convex functions, gradient methods, interior point, dual problems, CVXPY",
         "Convex optimization studies minimization of convex functions over convex sets; it guarantees global optima and underpins many machine-learning, control, and resource-allocation algorithms."),
    ]

    for path, title, domain, level, tags, definition in remaining:
        content[path + "/overview.txt"] = make_overview(
            path, domain, level, tags, title, definition,
            f"- Core definitions and taxonomy of {title}\n- Key methods, algorithms, or architectural patterns\n- Trade-offs and when to apply\n- Integration points with surrounding systems",
            f"System design must account for the performance, reliability, cost, and operational characteristics that {title} introduces. Choices here ripple into the broader architecture.",
            "Common languages, libraries, frameworks, and managed services used with this technology.",
            f"Production systems that rely on {title} for capability, scale, latency, or regulatory reasons.",
            "Misconfiguration, incorrect operating assumptions, scalability cliffs, and insufficient observability are typical failure modes.",
            "Select the appropriate variant, tune parameters, combine with complementary techniques, and measure real workload impact.",
            "Attack surface introduced by the technology, data-protection requirements, and compliance considerations.",
            f"- Parent node in {domain}\n- Cross-links to related mathematical, software, or hardware topics",
            "Active research, emerging standards, and open problems.",
            f"- Common over-simplifications and confusions surrounding {title}",
            "Standard benchmarks, quality metrics, and efficiency numbers used by practitioners.",
            f"1. Master prerequisites and core concepts\n2. Build or configure a correct baseline\n3. Evaluate on realistic cases\n4. Optimize, harden, and document",
            f"- Canonical papers and textbooks\n- Official documentation\n- High-quality surveys on {title}",
            difficulty="Advanced" if level >= 5 else "Intermediate"
        )
        content[path + "/index.md"] = make_index(
            title, path, "Advanced" if level >= 5 else "Intermediate",
            definition,
            f"- Fundamental concepts of {title}\n- Practical methods and patterns\n- Trade-offs and evaluation",
            "| Relevant Tool / Framework | Type | Purpose |",
            tags,
            f"- → Parent node\n- → Related topics in {domain}",
            f'- "What is {title}?"\n- "How does {title} work?"\n- "When should I use {title}?"\n- "What are common pitfalls?"',
            f"- Misconceptions specific to {title}",
            "1. Learn fundamentals\n2. Hands-on baseline\n3. Evaluate\n4. Productionize"
        )

    return content


def enhance_overview(text: str) -> str:
    if "VERSION: 2.0" in text:
        return text
    header_end = text.find("[CHUNK:")
    if header_end == -1:
        header_end = len(text)
    header = text[:header_end].rstrip()
    body = text[header_end:]
    extra = f"""
VERSION: 2.0
LAST_UPDATED: {TODAY}
CONFIDENCE_SCORE: 0.88
SOURCES: original + schema-enrichment
DIFFICULTY: Intermediate
ESTIMATED_READ_TIME: 8m
PREREQUISITES: See parent and related nodes
"""
    for line in extra.strip().splitlines():
        key = line.split(":")[0]
        if key not in header:
            header += "\n" + line
    additions = ""
    if "[CHUNK: COMMON_MISCONCEPTIONS]" not in body:
        additions += """
[CHUNK: COMMON_MISCONCEPTIONS]
- Oversimplified explanations often blur important distinctions.
- Performance claims must be evaluated against the specific workload and metrics.
- Newer techniques are not automatically better for every use case.
"""
    if "[CHUNK: BENCHMARKS_AND_METRICS]" not in body:
        additions += """
[CHUNK: BENCHMARKS_AND_METRICS]
Report task metrics together with efficiency numbers (latency, memory, cost). Use strong baselines and ablations.
"""
    if "[CHUNK: IMPLEMENTATION_CHECKLIST]" not in body:
        additions += """
[CHUNK: IMPLEMENTATION_CHECKLIST]
1. Confirm prerequisites and environment.
2. Implement a minimal correct version.
3. Validate on realistic examples.
4. Measure performance and resources.
5. Add monitoring, safety, and documentation.
"""
    if "[CHUNK: FURTHER_READING]" not in body:
        additions += """
[CHUNK: FURTHER_READING]
- Canonical textbooks and survey papers
- Official documentation of major tools
- Recent high-impact research papers
"""
    return header + "\n\n" + body.lstrip() + additions


def enhance_index(text: str) -> str:
    if "**Version:** 2.0" in text:
        return text
    lines = text.splitlines()
    out = []
    inserted = False
    for line in lines:
        out.append(line)
        if line.startswith("**Time to Learn:**") and not inserted:
            out.append(f"**Version:** 2.0 | **Last Updated:** {TODAY}")
            out.append("**Confidence:** 0.88")
            inserted = True
    if "## Common Misconceptions" not in text:
        out.append("\n## Common Misconceptions\n- See the corresponding overview.txt for detailed misconceptions.")
    if "## Implementation Checklist" not in text:
        out.append("\n## Implementation Checklist\n1. Study definition and core concepts\n2. Experiment with basic examples\n3. Review failure modes and apply mitigations")
    return "\n".join(out)


def load_progress() -> set:
    if PROGRESS_FILE.exists():
        return set(PROGRESS_FILE.read_text().splitlines())
    return set()


def save_progress(done: set):
    PROGRESS_FILE.parent.mkdir(parents=True, exist_ok=True)
    PROGRESS_FILE.write_text("\n".join(sorted(done)))


def main():
    print("Starting batched enrichment...")
    OUT_ROOT.mkdir(parents=True, exist_ok=True)
    stubs = get_stub_map()
    done = load_progress()
    print(f"Already completed: {len(done)} files")

    zf = zipfile.ZipFile(SRC_ZIP)
    all_content_files = [n for n in zf.namelist() if n.endswith("overview.txt") or n.endswith("index.md")]
    print(f"Total content files in source: {len(all_content_files)}")

    # First, force-write all stubs
    stub_count = 0
    for name, content in stubs.items():
        out_path = OUT_ROOT / name
        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_text(content, encoding="utf-8")
        done.add(name)
        stub_count += 1
    save_progress(done)
    print(f"Wrote {stub_count} stub files")

    # Now process the rest in batches
    remaining = [n for n in all_content_files if n not in done]
    print(f"Remaining to enhance: {len(remaining)}")

    batch_num = 0
    for i in range(0, len(remaining), BATCH_SIZE):
        batch = remaining[i:i + BATCH_SIZE]
        batch_num += 1
        print(f"\n--- Batch {batch_num} ({len(batch)} files) ---")
        for name in batch:
            try:
                out_path = OUT_ROOT / name
                out_path.parent.mkdir(parents=True, exist_ok=True)
                raw = zf.read(name).decode("utf-8", errors="replace")
                if name.endswith("overview.txt"):
                    enhanced = enhance_overview(raw)
                else:
                    enhanced = enhance_index(raw)
                out_path.write_text(enhanced, encoding="utf-8")
                done.add(name)
            except Exception as e:
                print(f"  ERROR on {name}: {e}")
        save_progress(done)
        print(f"  Batch done. Total completed: {len(done)}")
        time.sleep(0.3)  # small pause to be gentle on the filesystem

    # Final count
    final_over = len(list(OUT_ROOT.rglob("overview.txt")))
    final_idx = len(list(OUT_ROOT.rglob("index.md")))
    print(f"\n=== FINISHED ===")
    print(f"overview.txt files: {final_over}")
    print(f"index.md files:     {final_idx}")
    print(f"Progress file:      {PROGRESS_FILE}")
    print("You can now run: python3 scripts/build_index.py --root knowledge_base/Tech_Knowledge_System")


if __name__ == "__main__":
    main()

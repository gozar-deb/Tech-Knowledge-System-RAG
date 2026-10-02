# NUMA Architecture

**Path:** Tech_Knowledge_System/Hardware_and_Computer_Architecture/CPU_Architecture/Cache_Hierarchy/NUMA_Architecture
**Difficulty:** Advanced
**Time to Learn:** 1-2 weeks
**Version:** 2.0 | **Last Updated:** 2026-10-02
**Confidence:** 0.88

## Quick Definition
Non-Uniform Memory Access (NUMA) is a computer memory design used in multiprocessing, where the memory access time depends on the memory location relative to the processor. Processors can access their local memory faster than memory attached to other processors, leading to variable memory access latencies across the system.

## Key Concepts
- **NUMA Node** → A group of processors and their directly attached local memory.
- **Local Memory** → Memory directly connected to a processor within the same NUMA node, offering faster access.
- **Remote Memory** → Memory attached to a different NUMA node, accessed by a processor via an interconnect, resulting in slower access.
- **Memory Locality** → The principle that a processor should primarily access memory within its own NUMA node to maximize performance.
- **Interconnect** → The communication fabric (e.g., Intel QPI, AMD Infinity Fabric) that links different NUMA nodes, enabling access to remote memory.
- **NUMA Awareness** → Operating systems and applications designed to recognize and optimize for NUMA architectures by scheduling processes and allocating memory to maintain locality.

## Tools

| Tool | Type | Purpose |
|------|------|---------|
| `numactl` | Utility | Control NUMA policy for processes or shared memory |
| `hwloc` | Library/Tool | Discover hardware topology, including NUMA nodes |
| VMware vSphere | Virtualization | Optimize virtual machine placement and memory allocation on NUMA hardware |
| Linux Kernel | OS Feature | Provides NUMA scheduling and memory management policies |

## Retrieval Keywords
NUMA, Non-Uniform Memory Access, memory architecture, multiprocessing, CPU architecture, cache hierarchy, memory locality, NUMA node, local memory, remote memory, interconnect, QPI, Infinity Fabric, memory access time, performance optimization, system design, distributed memory, shared memory, `numactl`, `hwloc`, virtualization, operating system scheduling

## Related Nodes
- → Tech_Knowledge_System/Hardware_and_Computer_Architecture/CPU_Architecture/Cache_Hierarchy (Parent)
- → Tech_Knowledge_System/Hardware_and_Computer_Architecture/CPU_Architecture/Multiprocessing (Related Concept)
- → Tech_Knowledge_System/Operating_Systems/Memory_Management (Related Concept)

## Fast Queries This Node Should Answer
- "What is NUMA?"
- "How does NUMA work?"
- "When should I use NUMA?"
- "What are the main tools for NUMA?"
- "What are common failures in NUMA?"

## Common Misconceptions
- See the corresponding overview.txt for detailed misconceptions.

## Implementation Checklist
1. Study definition and core concepts
2. Experiment with basic examples
3. Review failure modes and apply mitigations
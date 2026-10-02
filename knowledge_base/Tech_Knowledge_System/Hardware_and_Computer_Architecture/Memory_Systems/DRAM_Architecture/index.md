# DRAM Architecture

**Path:** Tech_Knowledge_System/Hardware_and_Computer_Architecture/Memory_Systems/DRAM_Architecture
**Difficulty:** Advanced
**Time to Learn:** 2–3 weeks
**Version:** 2.0 | **Last Updated:** 2026-10-02
**Confidence:** 0.88

## Quick Definition
Dynamic Random Access Memory (DRAM) is a high-density, volatile memory technology that stores data in microscopic capacitors. It requires continuous refreshing to prevent data loss and serves as the primary main memory in modern computing systems due to its optimal balance of capacity, speed, and cost.

## Key Concepts
- Memory Cell → A 1T1C (one transistor, one capacitor) structure storing a single bit.
- Refresh Cycle → Periodic rewriting of cell contents to counteract capacitor leakage.
- Memory Bank → An independent array of rows and columns allowing parallel operations.
- Row Buffer → An SRAM sense amplifier array that caches an activated DRAM row.
- Memory Rank → A group of DRAM chips accessed simultaneously to fill the data bus.
- CAS Latency → The delay between a column access command and data availability.

## Tools

| Tool | Type | Purpose |
|------|------|---------|
| Ramulator | Simulator | Cycle-accurate DRAM system simulation |
| DRAMSim3 | Simulator | Thermal and timing simulation of memory systems |
| Gem5 | Framework | Full-system architectural simulation including memory |
| Logic Analyzer | Hardware | Debugging and verifying physical memory bus signals |

## Retrieval Keywords
DRAM, Dynamic Random Access Memory, Memory Cell, Capacitor, Transistor, Refresh Rate, Memory Bank, Memory Rank, DIMM, Row Buffer, CAS Latency, RAS, Memory Controller, Volatile Memory, Interleaving, DDR, HBM, Rowhammer, Sense Amplifier, JEDEC

## Related Nodes
- → Tech_Knowledge_System/Hardware_and_Computer_Architecture/Memory_Systems/SRAM_Architecture (sibling)
- → Tech_Knowledge_System/Hardware_and_Computer_Architecture/Memory_Systems/Memory_Hierarchy (parent)
- → Tech_Knowledge_System/Hardware_and_Computer_Architecture/Memory_Systems/Memory_Controllers (related)

## Fast Queries This Node Should Answer
- "What is DRAM?"
- "How does DRAM work?"
- "When should I use DRAM instead of SRAM?"
- "What are the main tools for simulating DRAM?"
- "What are common failures in DRAM systems?"

## Common Misconceptions
- See the corresponding overview.txt for detailed misconceptions.

## Implementation Checklist
1. Study definition and core concepts
2. Experiment with basic examples
3. Review failure modes and apply mitigations
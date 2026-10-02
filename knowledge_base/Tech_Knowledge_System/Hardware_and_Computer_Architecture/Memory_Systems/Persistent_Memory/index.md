# Persistent Memory

**Path:** Tech_Knowledge_System/Hardware_and_Computer_Architecture/Memory_Systems/Persistent_Memory
**Difficulty:** Advanced
**Time to Learn:** 2-4 weeks
**Version:** 2.0 | **Last Updated:** 2026-10-02
**Confidence:** 0.88

## Quick Definition
Persistent Memory (PMEM) is a non-volatile, byte-addressable memory technology that offers DRAM-like performance with data persistence. It integrates into the memory hierarchy, allowing applications to directly access data that survives power cycles, bridging the gap between traditional RAM and storage.

## Key Concepts
- Non-Volatile → Data persists across power cycles.
- Byte-Addressable → Fine-grained data access at the byte level.
- Memory Bus Integration → Direct CPU access via DIMM slots.
- Storage Class Memory (SCM) → A category of memory between DRAM and NAND flash.
- Data Durability → Guarantees data integrity and recoverability.
- Direct Access (DAX) → Bypassing page cache for direct application access.

## Tools

| Tool | Type | Purpose |
|------|------|---------|
| Intel Optane Persistent Memory | Hardware | Commercial PMEM module |
| PMDK (Persistent Memory Development Kit) | Software Library | Simplifies PMEM programming |
| DAX (Direct Access) | File System Feature | Enables direct access to PMEM regions |
| SNIA NVM Programming Model | Standard | Defines PMEM programming interfaces |

## Retrieval Keywords
persistent memory, PMEM, non-volatile memory, NVM, byte-addressable, storage class memory, SCM, Intel Optane, memory hierarchy, data persistence, low latency, high bandwidth, DAX, PMDK, memory bus, system performance, data integrity, memory technology, computer architecture, hardware, memory systems

## Related Nodes
- → Tech_Knowledge_System/Hardware_and_Computer_Architecture/Memory_Systems/DRAM (comparison)
- → Tech_Knowledge_System/Hardware_and_Computer_Architecture/Storage_Systems/SSD (comparison)

## Fast Queries This Node Should Answer
- "What is Persistent Memory?"
- "How does Persistent Memory work?"
- "When should I use Persistent Memory?"
- "What are the main tools for Persistent Memory?"
- "What are common failures in Persistent Memory?"
- "What are the benefits of Persistent Memory?"
- "How does PMEM differ from DRAM and SSD?"
- "What is the SNIA NVM Programming Model?"

## Common Misconceptions
- See the corresponding overview.txt for detailed misconceptions.

## Implementation Checklist
1. Study definition and core concepts
2. Experiment with basic examples
3. Review failure modes and apply mitigations
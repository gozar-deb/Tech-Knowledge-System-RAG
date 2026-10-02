# RAID and Erasure Coding

**Path:** Tech_Knowledge_System/Hardware_and_Computer_Architecture/Storage_Architecture/RAID_and_Erasure_Coding
**Difficulty:** Advanced
**Time to Learn:** 2-3 weeks
**Version:** 2.0 | **Last Updated:** 2026-10-02
**Confidence:** 0.88

## Quick Definition
RAID (Redundant Array of Independent Disks) combines multiple drives for performance and/or redundancy. Erasure Coding is a data protection method that fragments and encodes data with redundant pieces across storage locations, enabling reconstruction from partial data loss.

## Key Concepts
- RAID Levels → Different configurations balancing performance, redundancy, and cost.
- Striping → Distributing data across disks for improved I/O performance.
- Mirroring → Duplicating data across disks for high availability and redundancy.
- Parity → Redundant data used to reconstruct lost information from failed disks.
- Reed-Solomon Codes → A widely used type of erasure code for distributed storage systems.
- Data Reconstruction → The process of rebuilding lost data using redundant information.

## Tools

| Tool | Type | Purpose |
|------|------|---------|
| mdadm | Software | Linux software RAID management |
| ZFS | Filesystem/Volume Manager | Advanced storage management with RAID-Z |
| Ceph | Distributed Storage | Provides object, block, and file storage with erasure coding |
| Hardware RAID Controller | Hardware | Dedicated hardware for managing RAID arrays |

## Retrieval Keywords
RAID, Erasure Coding, data redundancy, fault tolerance, storage systems, data integrity, distributed storage, parity, striping, mirroring, RAID levels, Reed-Solomon codes, data recovery, storage efficiency, data availability, disk failure, hot spares, storage architecture, data resilience, block storage, object storage, data protection, storage array

## Related Nodes
- → Tech_Knowledge_System/Hardware_and_Computer_Architecture/Storage_Architecture (parent)
- → Tech_Knowledge_System/Hardware_and_Computer_Architecture/Storage_Architecture/SSD_and_HDD_Technologies (sibling)
- → Tech_Knowledge_System/Software_Engineering/Distributed_Systems/Fault_Tolerance (broader context)

## Fast Queries This Node Should Answer
- "What is RAID and Erasure Coding?"
- "How do RAID levels differ?"
- "When should I use Erasure Coding instead of RAID?"
- "What are the main tools for implementing RAID?"
- "What are common failures in RAID arrays?"

## Common Misconceptions
- See the corresponding overview.txt for detailed misconceptions.

## Implementation Checklist
1. Study definition and core concepts
2. Experiment with basic examples
3. Review failure modes and apply mitigations
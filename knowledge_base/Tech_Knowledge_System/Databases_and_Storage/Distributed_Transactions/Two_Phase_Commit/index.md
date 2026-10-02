# Two Phase Commit

**Path:** Tech_Knowledge_System/Databases_and_Storage/Distributed_Transactions/Two_Phase_Commit
**Difficulty:** Advanced
**Time to Learn:** 1-2 weeks
**Version:** 2.0 | **Last Updated:** 2026-10-02
**Confidence:** 0.88

## Quick Definition
The Two-Phase Commit (2PC) protocol is a distributed algorithm that ensures atomicity in distributed transactions across multiple participating nodes. It coordinates all participants to either collectively commit or abort a transaction, preventing partial updates and maintaining data consistency.

## Key Concepts
- Coordinator → The node responsible for orchestrating the 2PC protocol.
- Participants → The nodes involved in the distributed transaction, performing local operations.
- Prepare Phase → The first phase where the coordinator asks participants to prepare for commit and vote.
- Commit Phase → The second phase where the coordinator, based on votes, instructs participants to either commit or abort.
- Atomicity → Guarantees that all operations in a transaction either complete successfully or are entirely rolled back.
- Distributed Transaction → A transaction that involves multiple independent data stores or services.
- Blocking → A state where participants wait indefinitely for the coordinator, often due to coordinator failure.
- Write-Ahead Log (WAL) → Used by participants to record actions before applying them, enabling recovery.

## Tools

| Tool | Type | Purpose |
|------|------|---------|
| XA (eXtended Architecture) | Standard | API for distributed transaction processing |
| JTA (Java Transaction API) | API | Java standard for managing distributed transactions |
| Microsoft Distributed Transaction Coordinator (MSDTC) | Service | Windows service for coordinating distributed transactions |
| Atomikos | Library | Commercial transaction manager for Java applications |
| Narayana | Library | Open-source transaction manager for Java applications |
| PostgreSQL (with 2PC support) | Database | Relational database supporting distributed transactions |

## Retrieval Keywords
Two-Phase Commit, 2PC, distributed transactions, atomic commit, distributed database, transaction coordinator, prepare phase, commit phase, abort phase, distributed consistency, fault tolerance, blocking problem, distributed systems, transaction management, XA, JTA, MSDTC, distributed consensus, ACID properties, distributed commit protocol, distributed data integrity, distributed transaction recovery

## Related Nodes
- Tech_Knowledge_System/Databases_and_Storage/Distributed_Transactions/Three_Phase_Commit (alternative protocol)
- Tech_Knowledge_System/Databases_and_Storage/Distributed_Transactions/Saga_Pattern (alternative approach)
- Tech_Knowledge_System/Databases_and_Storage/Distributed_Databases (foundational concept)
- Tech_Knowledge_System/Databases_and_Storage/ACID_Properties (core database principles)

## Fast Queries This Node Should Answer
- "What is the Two-Phase Commit protocol?"
- "How does 2PC ensure atomicity in distributed transactions?"
- "When should I use the Two-Phase Commit protocol?"
- "What are the main tools and technologies for implementing 2PC?"
- "What are common failure modes and disadvantages of 2PC?"
- "What are the two phases of 2PC?"
- "How does 2PC handle coordinator failures?"
- "What are alternatives to Two-Phase Commit?"

## Common Misconceptions
- See the corresponding overview.txt for detailed misconceptions.

## Implementation Checklist
1. Study definition and core concepts
2. Experiment with basic examples
3. Review failure modes and apply mitigations
# Google Spanner

**Path:** Tech_Knowledge_System/Databases_and_Storage/NewSQL_Distributed_RDBMS/Google_Spanner
**Difficulty:** Expert
**Time to Learn:** 2–4 weeks
**Version:** 2.0 | **Last Updated:** 2026-10-02
**Confidence:** 0.88

## Quick Definition
Google Spanner is a unique globally-distributed, strongly-consistent, and horizontally scalable relational database service. It provides ACID transactions and SQL semantics across multiple data centers and continents, leveraging its innovative TrueTime API for global transactional consistency.

## Key Concepts
- TrueTime → Google's global clock API for synchronized time across servers.
- External Consistency → Guarantees transactions appear to execute in a global serial order.
- Paxos → Consensus algorithm for data replication and consistency within shards.
- Two-Phase Commit → Protocol for ensuring atomicity of distributed transactions.
- Hierarchical Scaling → Data sharding into tablets and spans for fine-grained distribution.
- MVCC → Allows concurrent reads of older data versions without blocking writes.

## Tools

| Tool | Type | Purpose |
|------|------|---------|
| Google Cloud Platform | Platform | Hosting and management of Spanner instances |
| GoogleSQL | Language | Primary SQL dialect for querying and data manipulation |
| Client Libraries | SDKs | Programmatic interaction with Spanner from various languages |
| IAM | Security | Access control and authentication for Spanner resources |

## Retrieval Keywords
Google Spanner, distributed SQL, NewSQL, globally distributed database, strong consistency, relational database, ACID transactions, horizontal scalability, TrueTime, fault tolerance, multi-region database, high availability, RDBMS, cloud database, Paxos, 2PC, external consistency, schema design, DML best practices, Google Cloud

## Related Nodes
- → Tech_Knowledge_System/Databases_and_Storage/NewSQL_Distributed_RDBMS (parent)
- → Tech_Knowledge_System/Cloud_Computing/Google_Cloud_Platform (platform provider)

## Fast Queries This Node Should Answer
- "What is Google Spanner?"
- "How does Google Spanner achieve global consistency?"
- "When should I use Google Spanner?"
- "What are the main tools for Google Spanner?"
- "What are common failures in Google Spanner?"

## Common Misconceptions
- See the corresponding overview.txt for detailed misconceptions.

## Implementation Checklist
1. Study definition and core concepts
2. Experiment with basic examples
3. Review failure modes and apply mitigations
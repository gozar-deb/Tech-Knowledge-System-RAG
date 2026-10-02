# NewSQL Distributed RDBMS

**Path:** Tech_Knowledge_System/Databases_and_Storage/NewSQL_Distributed_RDBMS
**Difficulty:** Advanced
**Time to Learn:** 2-4 weeks
**Version:** 2.0 | **Last Updated:** 2026-10-02
**Confidence:** 0.88

## Quick Definition
NewSQL Distributed RDBMS are modern relational databases that offer the ACID guarantees and SQL interface of traditional RDBMS, combined with the horizontal scalability and high performance of NoSQL systems, specifically designed for high-volume OLTP workloads.

## Key Concepts
- ACID Compliance → Ensures data integrity and reliability across distributed transactions.
- Horizontal Scalability → Ability to expand database capacity by adding more machines to a cluster.
- Distributed Transactions → Operations spanning multiple database nodes while maintaining atomicity.
- Sharding → Data partitioning technique to distribute rows across different database instances.
- Replication → Copying data for fault tolerance and high availability.
- Strong Consistency → Guarantees that all nodes see the same data at the same time.

## Tools

| Tool | Type | Purpose |
|------|------|---------|
| CockroachDB | Database | Cloud-native, distributed SQL database for global applications |
| YugabyteDB | Database | Open-source, high-performance distributed SQL database |
| TiDB | Database | Open-source, cloud-native distributed SQL database compatible with MySQL protocol |
| VoltDB | Database | In-memory, ACID-compliant NewSQL database for high-velocity data |

## Retrieval Keywords
NewSQL, Distributed RDBMS, ACID, horizontal scalability, relational, SQL, OLTP, high performance, low latency, sharding, replication, distributed transactions, consistency, fault tolerance, database architecture, data distribution, concurrency control, cluster, shared-nothing, real-time, transactional, database management systems

## Related Nodes
- → Tech_Knowledge_System/Databases_and_Storage/NoSQL_Databases (contrasts)
- → Tech_Knowledge_System/Databases_and_Storage/Relational_Databases (foundational concepts)
- → Tech_Knowledge_System/Distributed_Systems/Consensus_Algorithms (underlying mechanisms)

## Fast Queries This Node Should Answer
- "What is NewSQL Distributed RDBMS?"
- "How does NewSQL achieve horizontal scalability?"
- "When should I use a NewSQL database over a traditional RDBMS or NoSQL?"
- "What are the main tools for NewSQL databases?"
- "What are common failures in NewSQL systems?"

## Common Misconceptions
- See the corresponding overview.txt for detailed misconceptions.

## Implementation Checklist
1. Study definition and core concepts
2. Experiment with basic examples
3. Review failure modes and apply mitigations
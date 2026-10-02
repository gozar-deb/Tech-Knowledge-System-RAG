# DAG Based Ledgers

**Path:** Tech_Knowledge_System/Blockchain_and_Distributed_Ledger/Consensus_Mechanisms/DAG_Based_Ledgers
**Difficulty:** Advanced
**Time to Learn:** 2-4 weeks
**Version:** 2.0 | **Last Updated:** 2026-10-02
**Confidence:** 0.88

## Quick Definition
DAG-based ledgers are a novel class of Distributed Ledger Technologies (DLT) that use a Directed Acyclic Graph structure for transaction recording, offering an alternative to traditional linear blockchains. This architecture facilitates asynchronous transaction processing, aiming for higher scalability and throughput, particularly suitable for micro-transactions and IoT applications.

## Key Concepts
- DAG Structure → Transactions form a graph where each validates multiple previous ones.
- Asynchronous Consensus → Transactions are added independently, without global block creation.
- Scalability → Achieved through parallel processing of transactions across the network.
- Immutability → Confirmed transactions are permanently recorded and tamper-proof.
- Tip Selection → Algorithm for choosing which unconfirmed transactions to validate.
- Transaction Ordering → Mechanisms to establish a consistent sequence of events in the graph.

## Tools

| Tool | Type | Purpose |
|------|------|---------|
| IOTA Tangle | Protocol/Network | IoT data and value transfer |
| Nano Block Lattice | Protocol/Network | Feeless, instant digital cash |
| Hedera Hashgraph | DLT Platform | Enterprise-grade distributed applications |
| Go/Rust | Programming Language | Core development of DLT systems |

## Retrieval Keywords
Directed Acyclic Graph, DAG, DLT, distributed ledger, asynchronous consensus, scalability, transaction throughput, immutability, tip selection, IOTA, Nano, Hedera Hashgraph, blockchain alternative, cryptoeconomics, distributed systems, ledger technology, decentralized, IoT, micro-transactions, graph theory, consensus mechanisms

## Related Nodes
- → Tech_Knowledge_System/Blockchain_and_Distributed_Ledger/Consensus_Mechanisms/Proof_of_Work (related_concept)
- → Tech_Knowledge_System/Blockchain_and_Distributed_Ledger/Consensus_Mechanisms/Proof_of_Stake (related_concept)

## Fast Queries This Node Should Answer
- "What is a DAG-based ledger?"
- "How does asynchronous consensus work in DAGs?"
- "When should I use a DAG-based ledger instead of a blockchain?"
- "What are the main tools and platforms for DAGs?"
- "What are common failure modes in DAG-based systems?"

## Common Misconceptions
- See the corresponding overview.txt for detailed misconceptions.

## Implementation Checklist
1. Study definition and core concepts
2. Experiment with basic examples
3. Review failure modes and apply mitigations